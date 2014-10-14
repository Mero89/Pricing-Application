# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.data.AppModel import AppModel, ObligationMd


class MyTable(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        policy.setHorizontalStretch(1)
        self.setSizePolicy(policy)
        self.session = AppModel().get_session()
        ob = ObligationMd()
        self.headers = ob._sa_class_manager.keys()
        print self.headers
        self.set_headers(self.headers)
        self.insertRow(0)

    def set_headers(self, h_list):
        self.setColumnCount(len(h_list))
        header_list = QtCore.QStringList(h_list)
        self.setHorizontalHeaderLabels(header_list)

    def insert_row(self, data, row_pos):
        for el in data:
            idx = data.index(el)
            item = QTableWidgetItem(str(el))
            self.setItem(row_pos, idx, item)

    def insert_data(self, data):
        for el in data:
            rw_idx = data.index(el)
            self.insertRow(rw_idx)
            self.insert_row(el, rw_idx)

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    # row = ['data-'+str(i) for i in range(len(headers))]
    # data = [row for i in range(5)]
    table = MyTable()
    # table.insert_data(data)
    table.show()
    ap.exec_()