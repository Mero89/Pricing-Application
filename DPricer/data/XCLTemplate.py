# coding=utf-8
__author__ = 'F.Marouane'

import xlwt
import os


def create_template(path, filename='Template.xls'):
    """
    Exporte le modèle d'importation des actifs.
    Le modèles est sous format Excel.
    :param path: str
    :param filename: str
    :return:
    """
    w = xlwt.Workbook(encoding='utf-8')
    s = w.add_sheet('Exemple')
    row = s.row(0)
    style = xlwt.easyxf('font: name Menlo, bold True, height 280, colour blue;')
    warning = xlwt.easyxf('font: name Menlo, bold True, height 320, colour red;'
                          'alignment: vertical top, wrap True')

    row.write(0, 'Code ISIN', style)
    row.write(1, 'NOM', style)
    row.write(2, 'Nominal', style)
    row.write(3, 'Taux Facial', style)
    row.write(4, 'Spread', style)
    row.write(5, 'Date emission', style)
    row.write(6, 'Date de jouissance', style)
    row.write(7, 'Date echeance', style)
    row.write(8, 'Type', style)
    s.write_merge(0, 4, 10, 14,
                  'Pour le type mettre sans faute un des choix suivants: < N >, < AMC >, <REV>, < AMCRev >', warning)
    final_path = os.path.join(path, filename)
    w.save(final_path)

create_template('/Users/mar/Desktop')
