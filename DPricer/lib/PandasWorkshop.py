# coding=utf-8
__author__ = 'F.Marouane'

import os
import pandas as pd
import datetime as dt
# import numpy
# import sys
# import xlrd, xlwt

# Setting options
# adapte l'affichage à la largeur de l'écran disponible
pd.set_option('expand_frame_repr', False)
# nombre max de colonnes à afficher
pd.set_option('max_info_columns', 11)
# truncate the view if numCols is > than max_cols
pd.set_option('large_repr', 'truncate')

strate_ct = 364
strate_mt = strate_ct * 5
strate_mlt = strate_ct * 10
# strate LT > 10 ans ==> strate LT > max strate MLT
mbi_path = '/Users/mar/Desktop/mbi'
start_file_name = 'MBI_37_12_2013.xlsx'
end_file_path = '/Users/mar/Desktop/output.xls'
start_list_name = 'Feuil1'


def import_courbe(sheetname=None):
    if sheetname:
        fichier = pd.ExcelFile('/Users/mar/Desktop/courbe.xls')
        feuil = fichier.parse(sheetname)
    pass


def read_sheet(sheetname):
    xf = pd.ExcelFile(os.path.join(mbi_path, start_file_name))
    df = xf.parse(sheetname)
    return df


def start_list(sheetname='Feuil1'):
    # return the starting list
    df = read_sheet(sheetname)
    df['Mat Residuelle'] = df['DATE_ECHEANCE'] - df['Date']  # - date_observation
    df['Mat Residuelle'] = df['Mat Residuelle'][:].dt.days
    return df


def acquire_changes(sheetname='Feuil2'):
    # Return the next changes to apply
    return read_sheet(sheetname)


def stratifie(that_list, champs, start=None, end=None):
    # Stratifie la liste selon les strates désirées
    strate = pd.DataFrame()
    if start:
        if end:
            strate = that_list[(that_list[champs] > start) & (that_list[champs] <= end)]
        else:
            strate = that_list[that_list[champs] > start]
    else:
        strate = that_list[that_list[champs] <= end]
    return strate


def purge(that_list, judgement_day):
    purge = that_list[that_list['DATE_ECHEANCE'] > judgement_day]
    return purge


def build_indexes(mbi_global):
    # Return a dict containing the appropriate layers of MBI => [MBI CT, MBI MT, MBI MLT, MBI LT].
    # Keys = [CT, MT, MLT, LT]
    indexes = dict()
    indexes['CT'] = stratifie(mbi_global, 'Mat Residuelle', end=strate_ct)
    indexes['MT'] = stratifie(mbi_global, 'Mat Residuelle', start=strate_ct, end=strate_mt)
    indexes['MLT'] = stratifie(mbi_global, 'Mat Residuelle', start=strate_mt, end=strate_mlt)
    indexes['LT'] = stratifie(mbi_global, 'Mat Residuelle', start=strate_mlt)
    return indexes


def move(that_list, move_list, move_date):
    # Applique les mouvements à la liste courante
    # et retourne la moved list
    pass


def save_list(that_list, filename='output.xls', sheetname='Output'):
    writer = pd.ExcelWriter(filename)
    that_list.to_excel(writer, sheet_name=sheetname)
    writer.save()
    writer.close()
    pass


def main():

    pass

if __name__ == '__main__':
    main()

    # test()