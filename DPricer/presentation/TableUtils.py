# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4.QtGui import *
from PyQt4 import QtCore


def set_headers(table, h_list):
    table.setColumnCount(len(h_list))
    header_list = QtCore.QStringList(h_list)
    table.setHorizontalHeaderLabels(header_list)


def insert_row(table, data, row_pos, offset=0):
    for el in data:
        idx = data.index(el)
        item = QTableWidgetItem(str(el))
        table.setItem(row_pos, idx + offset, item)


def insert_data(table, data, offset=0):
    for el in data:
        rw_idx = data.index(el)
        table.insertRow(rw_idx)
        table.insert_row(el, rw_idx, offset)


def put_row(table, row_pos, keys, db_elmt):
    table.insertRow(row_pos)
    col_pos = 0
    db_dico = dict(db_elmt.__dict__)
    for el in keys:
        if db_dico.has_key(el):
            item = QTableWidgetItem(unicode(db_dico[el]))
            table.setItem(row_pos, col_pos, item)
            col_pos += 1


def put_result_set(table, keys, result_set):
    row = 0
    for el in result_set:
        put_row(table, row, keys, el)
        row += 1


def get_headers(table, start, end):
    cols = table.columnCount()
    fin = end
    if fin > cols:
        fin = cols
    headers = [unicode(table.horizontalHeaderItem(i).text()) for i in range(start, fin)]
    return headers
