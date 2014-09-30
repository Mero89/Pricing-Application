# coding=utf-8
__author__ = 'F.Marouane'

import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore

from DPricer.presentation.Echeancier import Ui_Dialog


class EcheancierDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    @QtCore.pyqtSignature("")
    def on_pushButtonAjouter_clicked(self):
        num = self.ui.tableWidget.rowCount()
        dd = QTableWidgetItem()
        ff = QTableWidgetItem()
        self.ui.tableWidget.insertRow(num)
        self.ui.tableWidget.setItem(num, 0, dd)
        self.ui.tableWidget.setItem(num, 1, ff)

    @QtCore.pyqtSignature("")
    def on_pushButtonSupprimer_clicked(self):
        itm = self.ui.tableWidget.currentItem()
        idx = self.ui.tableWidget.indexFromItem(itm)
        self.ui.tableWidget.removeRow(idx.row())

if __name__ == '__main__':
    # sip.setapi('Qstring',2 )
    # YM = YieldManager()
    # YM.import_auto()
    # form = Calculette()
    ap = QApplication(sys.argv)
    form = EcheancierDialog()
    form.show()
    ap.exec_()