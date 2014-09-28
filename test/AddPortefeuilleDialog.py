# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from AddPFDialog import Ui_AddPFDialog
from PyQt4 import QtCore
from DPricer.data.AppModel import AppModel, PortefeuilleMd


class PortefeuilleDialog(QDialog, Ui_AddPFDialog):
    def __init__(self):
        super(Ui_AddPFDialog, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_AddPFDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Ajout de Portefeuilles')
        self.connect(self, QtCore.SIGNAL('accepted()'), self.save_portefeuille)
        self.connect(self.ui.pushButtonAjouter_2, QtCore.SIGNAL('clicked()'), self.Ajouter_clicked)
        self.connect(self.ui.pushButtonSupprimer_2, QtCore.SIGNAL('clicked()'), self.Supprimer_clicked)

    @QtCore.pyqtSlot()
    def save_portefeuille(self):
        num = self.ui.tableWidget.rowCount()
        ma_liste = list()
        if num >= 1:
            for i in range(num):
                isin = self.ui.tableWidget.item(i, 0).text()
                nom = self.ui.tableWidget.item(i, 1).text()
                if isin != str and nom != str:
                    ma_liste.append(PortefeuilleMd(p_isin=str(isin), nom=str(nom)))
        session = AppModel().get_session()
        session.add_all(ma_liste)
        # for el in ma_liste:
        #     session.add(el)
        # else:
        try:
            session.commit()
        except Exception as e:
            print e.message

    @QtCore.pyqtSlot()
    def Ajouter_clicked(self):
        num = self.ui.tableWidget.rowCount()
        dd = QTableWidgetItem()
        ff = QTableWidgetItem()
        self.ui.tableWidget.insertRow(num)
        self.ui.tableWidget.setItem(num, 0, dd)
        self.ui.tableWidget.setItem(num, 1, ff)
        self.ui.tableWidget.setFocus()

    @QtCore.pyqtSlot()
    def Supprimer_clicked(self):
        itm = self.ui.tableWidget.currentItem()
        idx = self.ui.tableWidget.indexFromItem(itm)
        self.ui.tableWidget.removeRow(idx.row())

if __name__ == '__main__':
    # sip.setapi('Qstring',2 )
    # YM = YieldManager()
    # YM.import_auto()
    # form = Calculette()
    ap = QApplication(sys.argv)
    form = PortefeuilleDialog()
    form.show()
    ap.exec_()