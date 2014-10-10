# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4.QtGui import *
from PyQt4 import QtCore
import sys


class MyTable(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)

    def set_headers(self, h_list):
        self.setColumnCount(len(h_list))
        header_list = QtCore.QStringList(h_list)
        self.setHorizontalHeaderLabels(header_list)

    def insert_row(self, data, row_pos):
        if len(data) > self.columnCount():

        pass

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    headers = ['header-'+str(i) for i in range(10, 2, -1)]
    row = ['data-'+str(i) for i in range(len(headers))]
    data = [row for i in range(5)]
    table = MyTable()
    table.set_headers(headers)
    table.show()
    ap.exec_()