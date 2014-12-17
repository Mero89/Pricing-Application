#!/usr/bin/env python
# coding=utf-8

__author__ = 'Marouane'

import os
import openpyxl as pxl
import datetime as dt
from sqlalchemy.exc import *
from DPricer.data.AppModel import *

filepath = '/Users/mar/Desktop/courbe-2012.xlsx'


def read_file(filepath):
    if os.path.isfile(filepath):
        wbook = pxl.load_workbook(filepath)
        return wbook


def read_sheet(wbook, pos):
    if 0 <= pos < len(wbook.worksheets):
        wsheet = wbook.worksheets[pos]
        return wsheet
    else:
        wsheet = wbook.worksheets[-1]
        return wsheet


def get_courbe(sheet):
    liste_courbes = list()
    dico = dict()
    try:
        dico['date_req'] = dt.datetime.strptime(sheet.title.strip(), '%d-%m-%Y')
    except ValueError:
        dico['date_req'] = dt.datetime.strptime(sheet.title.strip(), '%d-%m-%y')

    if isinstance(sheet['E4'].value, dt.datetime):
        index = 8
        dico['date_transaction'] = sheet['E4'].value
        if isinstance(sheet['C' + str(index)].value, unicode):
            index += 1
        while sheet['C' + str(index)].value is not None:
            dico['date_valeur'] = sheet['C' + str(index)].value
            dico['date_echeance'] = sheet['D' + str(index)].value
            dico['transactions'] = sheet['E' + str(index)].value
            dico['taux_pondere'] = sheet['F' + str(index)].value
            c = CourbeMd(**dico)
            liste_courbes.append(c)
            index += 1
        return liste_courbes

    elif isinstance(sheet['D4'].value, dt.datetime):
        index = 8
        dico['date_transaction'] = sheet['D4'].value
        if isinstance(sheet['B' + str(index)].value, unicode):
            index += 1
        while sheet['B' + str(index)].value is not None:
            dico['date_valeur'] = sheet['B' + str(index)].value
            dico['date_echeance'] = sheet['C' + str(index)].value
            dico['transactions'] = sheet['D' + str(index)].value
            dico['taux_pondere'] = sheet['E' + str(index)].value
            c = CourbeMd(**dico)
            liste_courbes.append(c)
            index += 1
        return liste_courbes
    elif isinstance(sheet['D5'].value, dt.datetime):
        index = 9
        dico['date_transaction'] = sheet['D5'].value
        while sheet['B' + str(index)].value is not None:
            dico['date_valeur'] = sheet['B' + str(index)].value
            dico['date_echeance'] = sheet['C' + str(index)].value
            dico['transactions'] = sheet['D' + str(index)].value
            dico['taux_pondere'] = sheet['E' + str(index)].value
            c = CourbeMd(**dico)
            liste_courbes.append(c)
            index += 1
        return liste_courbes


def commit_courbe_reuters(wbook, sheet):
    pos = wbook.get_sheet_names().index(sheet)
    ws = read_sheet(wbook, pos)
    la_courbe = get_courbe(ws)
    s = AppModel().get_session()
    _date = la_courbe[1].date_req
    existe = s.query(CourbeMd).filter_by(date_req=_date).first()
    if not existe:
        try:
            s.add_all(la_courbe)
            s.commit()
            print ws.title, 'ADDED'
        except DataError as e:
            print 'Error when adding the curve of {}'.format(_date)
    else:
        print u'la courbe de la date {} existe déjà'.format(_date.date())


def commit_workbook_reuters(filepath):
    wbook = read_file(filepath)
    for sheets in wbook.get_sheet_names():
        commit_courbe_reuters(wbook, sheets)
    print 'DONE'

if __name__ == '__main__':
    # '/Users/mar/Desktop/courbe-2009.xlsx'
    fich = ['/Users/mar/Desktop/courbe-2007.xlsx']
    commit_workbook_reuters(fich[0])