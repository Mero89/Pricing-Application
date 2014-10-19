# coding=utf-8
__author__ = 'F.Marouane'

import os
import sys
import urllib2
import multiprocessing as mp


def save_into_file(number):
    target_path = '/Users/mar/Downloads/asfim'
    asfim_url = 'http://www.asfim.ma/upload/MoDUle_26/'
    filename_header = 'File_26_{n}.pdf'
    filename = filename_header.format(n=number)
    url = asfim_url + filename
    target_file = os.path.join(target_path, filename)
    try:
        u = urllib2.urlopen(url)
        f = open(target_file, 'wb')
        f.write(u.read())
        f.close()
        u.close()
        print 'success'
    except urllib2.HTTPError:
        print 'error'


if __name__ == '__main__':
    # process = mp.Process()
    ncpu = mp.cpu_count()
    pool = mp.Pool(processes=ncpu)
    maxf = 2396
    last_stop = 1241
    minf = 1201
    for i in range(minf, maxf+1):
        res = pool.apply_async(save_into_file, (i,))
        res.get(timeout=50)

