# coding=utf-8
__author__ = 'F.Marouane'


import xlwt
import os


def create_template(path, filename='Template'):
    w = xlwt.Workbook()
    s = w.add_sheet('Exemple')
    row = s.row(0)

    row.write(0, 'Code ISIN')
    row.write(1, 'NOM')
    row.write(2, 'Nominal')
    row.write(3, 'Taux Facial')
    row.write(4, 'Spread')
    row.write(5, 'Date emission')
    row.write(6, 'Date de jouissance')
    row.write(7, 'Date echeance')
    row.write(8, 'Type')
    row.write(9, 'Pour le type mettre sans faute un des choix suivants: < N >, < AMC >, <REV>, < AMCRev >')
    final_path = os.join(path, filename)
    w.save(final_path)

create_template('/Users/mar/Desktop')
