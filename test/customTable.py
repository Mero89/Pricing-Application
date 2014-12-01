# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.data.AppModel import AppModel, ObligationMd, PanierMd
from math import *


class MyTable(QTableWidget):

    def __init__(self):
        QTableWidget.__init__(self)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        policy.setHorizontalStretch(1)
        self.setSizePolicy(policy)
        self.session = AppModel().get_session()
        self.itemChanged.connect(self.evaluate)
        # self.set_headers(self.headers)

    def set_headers(self, h_list):
        self.setColumnCount(len(h_list))
        header_list = QtCore.QStringList(h_list)
        self.setHorizontalHeaderLabels(header_list)

    def insert_row(self, data, row_pos, offset=0):
        for el in data:
            idx = data.index(el)
            item = QTableWidgetItem(str(el))
            self.setItem(row_pos, idx+offset, item)

    def insert_data(self, data, offset=0):
        for el in data:
            rw_idx = data.index(el)
            self.insertRow(rw_idx)
            self.insert_row(el, rw_idx, offset)

    def evaluate(self):
        """
        :param idx:
        :return:
        """
        idx = self.currentIndex()
        inputed = unicode(self.itemFromIndex(idx).text())
        expr = inputed.split('=')[1].strip()
        value = eval(expr)
        self.itemFromIndex(idx).setText(str(value))


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
        if el in db_dico:
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

if __name__ == '__main__':
    # import swampy.Lumpy as Lumpy
    # lumpy = Lumpy.Lumpy()
    # lumpy.make_reference()
    ap = QApplication(sys.argv)
    # row = ['data-'+str(i) for i in range(len(headers))]
    # data = [row for i in range(5)]
    table = MyTable()
    session = table.session
    result = session.query(PanierMd).all()
    # headers = ['isin', 'nom', 'nominal']
    keys = ['p_isin', 'isin', 'quantite']
    h = [u"ISIN Portefeuille", u"ISIN de l'Actif", u"Quantite de l'actif dans le protefeuille"]
    table.set_headers(h)
    put_result_set(table, keys, result)
    # hed = [unicode(table.horizontalHeaderItem(i).text()) for i in range(table.columnCount())]
    # print hed
    table.show()
    ap.exec_()
    # lumpy.object_diagram@rouane
    
    # lumpy.class_diagram()
