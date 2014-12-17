# coding=utf-8
__author__ = 'F.Marouane'

import os
import pandas as pd
import datetime as dt
# import numpy
# import sys
# import xlrd, xlwt

strate_ct = 364
strate_mt = strate_ct * 5
strate_mlt = strate_ct * 10
# strate LT > 10 ans ==> strate LT > max strate MLT
mbi_path = '/Users/mar/Desktop/mbi'
start_file_name = 'MBI_37_12_2013.xlsx'
end_file_path = '/Users/mar/Desktop/output.xls'
start_list_name = 'Feuil1'


def start_list(sheetname='Feuil1'):
    # return the starting list
    xf = pd.ExcelFile(mbi_path+start_file_name)
    df = xf.parse(sheetname)
    return df


def acquire_changes(sheetname='Feuil2'):
    # Return the next changes to apply
    return start_list(sheetname)


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


def main():
    # Execute main scripts.
    pass

if __name__ == '__main__':
    main()
    print 'executed'
    # test()