# coding=utf-8
__author__ = 'F.Marouane'

# import sip
# from PyQt4.QtCore import *
# from DPricer.lib.YieldManager import YieldManager
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from SandBox import Ui_SandBox
from DPricer.data.AppModel import ObligationMd, AppModel
from DPricer.lib.Obligation import Obligation


class RenderBox(QDialog, Ui_SandBox):
    def __init__(self):
        super(Ui_SandBox, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_SandBox()
        self.ui.setupUi(self)
        md = AppModel()
        session = md.get_session()
        results = session.query(ObligationMd).all()
        for i in range(len(results)):
            el = results[i]
            a = QTableWidgetItem(el.isin)
            nom = QTableWidgetItem(el.nom)
            nominal = QTableWidgetItem(str(el.nominal))
            d_em = QTableWidgetItem(str(el.date_emission))
            d_j = QTableWidgetItem(str(el.date_jouissance))
            d_ech = QTableWidgetItem(str(el.maturite))
            tx_facial = QTableWidgetItem(str(el.taux_facial * 100)+' %')
            spread = QTableWidgetItem(str(el.spread * 100)+' %')
            ttype = QTableWidgetItem(str(el.type))
            obl = Obligation(el.nominal, el.taux_facial, el.date_emission, el.date_jouissance, el.maturite,
                             d_eval='1/9/2014', spread=el.spread)
            prix = QTableWidgetItem(str(obl.prix())+' MAD')
            sensi = QTableWidgetItem(str(obl.sensibilite()))
            dur = QTableWidgetItem(str(obl.duration()))
            tx_act = QTableWidgetItem(str(round(obl.tx_actuariel * 100, 6))+' %')

            self.ui.tableWidget.insertRow(i)
            # self.ui.tableWidget.row()

            self.ui.tableWidget.setRowHeight(i, 20)
            self.ui.tableWidget.setItem(i, 0, a)
            self.ui.tableWidget.setItem(i, 1, nom)
            self.ui.tableWidget.setItem(i, 2, nominal)
            self.ui.tableWidget.setItem(i, 3, d_em)
            self.ui.tableWidget.setItem(i, 4, d_j)
            self.ui.tableWidget.setItem(i, 5, d_ech)
            self.ui.tableWidget.setItem(i, 6, tx_facial)
            self.ui.tableWidget.setItem(i, 7, spread)
            self.ui.tableWidget.setItem(i, 8, ttype)
            self.ui.tableWidget.setItem(i, 9, tx_act)
            self.ui.tableWidget.setItem(i, 10, prix)
            self.ui.tableWidget.setItem(i, 11, dur)
            self.ui.tableWidget.setItem(i, 12, sensi)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    # YM = YieldManager()
    # YM.import_auto()
    # form = Calculette()
    ap = QApplication(sys.argv)
    form = RenderBox()
    form.show()
    ap.exec_()