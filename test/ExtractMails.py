__author__ = 'mar'
from mysql import connector
import mysql
import os
import re
import sys


def main(folder_path):
    mail_list = read_folder(folder_path)
    t = insert_mail_list(mail_list)
    if t:
        print 'Insert Successfull !!!'
    else:
        print 'Insert Failed'


def read_folder_recursive(folder_path=None):
    if folder_path is None:
        fp = '.'
    else:
        fp = folder_path
    final_list = list()
    w = os.walk(fp)
    while True:
        try:
            dir_path, b, file_list = w.next()
            temp = read_folder(dir_path)
            final_list.append(temp)
        except StopIteration:
            return final_list
            break


def read_folder(folder_path=None):
    if folder_path is None:
        fp = '.'
    else:
        fp = folder_path
    l = file_list(fp)
    mail_list = list()
    if l != list():
        for myfile in l:
            pt = os.path.join(fp, myfile)
            mail = extract_mail(pt)
            mail_list.append(mail)
        return mail_list


def insert_mail_list(mail_list):
    if mail_list != list():
        for mail in mail_list:
            insert_mail(mail)
        else:
            return True


def insert_mail(lemail):
    if lemail is not None:
        if len(lemail) > 0:
            muser = 'funphoto_booth'
            mpsswd = '?JR4ZgrU#vT!'
            mdbname = 'funphoto_FunPhotoBooth'
            mhost = 'localhost'
            cnx = connector.connect(user=muser, password=mpsswd, host=mhost, database=mdbname)
            cur = cnx.cursor()
            req = 'INSERT INTO `Mails` (mail) VALUES ("{mail}")'.format(mail=lemail)
            cur.execute(req)
            cnx.commit()


def is_desired(filename):
    pattern = '[0-9]{4}'
    m = re.search(pattern, filename)
    if m is None:
        return False
    else:
        return True


def file_list(folder_path):
    if os.path.exists(folder_path):
        l = os.listdir(folder_path)
        f_list = [f for f in l if is_desired(f) and 'Reprint' not in f]
        return f_list


def extract_mail(pathfile):
    """ read text files and return a dict of (keys:values)"""
    d = dict()
    f = open(pathfile)
    lines = [row.split('\r\n') for row in f.readlines()]
    # we no longer need the file
    f.close()
    # put keys/values on the dict
    for row in lines:
        key, val = row[0].split('\t')
        d[key] = val
    # check if the desired key exists
    if 'EmailAddress' in d.keys():
        return d['EmailAddress']


def write_on_file(mail_list, file_path):
    f = open(file_path, 'w')
    line_sep = '\n'
    for l in mail_list:
        f.write(l + line_sep)
    f.close()


def test(folder_path='.'):
    mail_list = read_folder_recursive(folder_path)
    print mail_list


def recursive_main(folder_path):
    mail_list = read_folder_recursive(folder_path)
    for i in mail_list:
        insert_mail_list(i)
    return 0


if __name__ == '__main__':
    mode = sys.argv[2]
    if mode == 'rec':
        recursive_main(sys.argv[1])
    if mode is None:
        main(sys.argv[1])
