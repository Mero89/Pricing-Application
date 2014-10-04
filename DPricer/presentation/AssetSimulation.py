# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.Simulation import Ui_Simulation
from DPricer.lib.Obligation import Obligation
from DPricer.data.AppModel import AppModel, ObligationMd

class AssetSimulation(QWidget, Ui_Simulation):
    def __init__(self, parent=None):
        super(Ui_Simulation, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Simulation()
        self.ui.setupUi(self)
        self.parent = parent
        self.session = AppModel().get_session()
        self.data = list()
        self.data = self.session.query(ObligationMd).all()
        self.populate_table()
        self.bag = list()
        pass

    def connect_actions(self):
        self.ui.addTosimulate.clicked.connect(self.add_toolbutton)
        self.ui.removeFromSimulate.clicked.connect(self.remove_toolbutton)
        self.ui.doubleSpinBox.contentChanged.connect(self.update_prices)
        pass

    def add_toolbutton(self):
        selection = self.ui.tableWidgetActifs
        obl=Obligation
        if obl not in self.bag:
            self.bag.append(obl)
        pass

    def remove_toolbutton(self):
        self.bag.remove()
        pass

    def update_prices(self):
        for obl in self.bag:
            obl.tx_actuariel += self.ui.doubleSpinBox.value()/100.
        pass

    def populate_table(self):
        self.ui.tableWidgetActifs.clearContents()
        cur_rows = self.ui.tableWidgetActifs.rowCount()
        if self.data:
            # populate table
            for el in self.data:
                idx = self.data.index(el)
                isin = QTableWidgetItem(el.isin)
                nom = QTableWidgetItem(el.nom)
                nominal = QTableWidgetItem(str(el.nominal))
                tx_facial = QTableWidgetItem(str(el.taux_facial * 100) + ' %')
                spread = QTableWidgetItem(str(el.spread * 100) + ' %')
                d_em = QTableWidgetItem(str(el.date_emission))
                d_j = QTableWidgetItem(str(el.date_jouissance))
                d_ech = QTableWidgetItem(str(el.maturite))
                obl = Obligation(el.nominal, el.taux_facial, el.date_emission, el.date_jouissance, el.maturite,
                                 d_eval=None, spread=el.spread)
                prix = QTableWidgetItem(str(obl.prix()) + ' MAD')
                tx_act = QTableWidgetItem(str(round((obl.tx_actuariel + obl.spread) * 100, 6)) + ' %')
                if idx + 1 >= cur_rows:
                    self.ui.tableWidgetActifs.insertRow(idx)
                    self.ui.tableWidgetActifs.setRowHeight(idx, 25)
                self.ui.tableWidgetActifs.setItem(idx, 0, isin)
                self.ui.tableWidgetActifs.setItem(idx, 1, nom)
                self.ui.tableWidgetActifs.setItem(idx, 2, nominal)
                self.ui.tableWidgetActifs.setItem(idx, 3, tx_facial)
                self.ui.tableWidgetActifs.setItem(idx, 4, spread)
                self.ui.tableWidgetActifs.setItem(idx, 5, d_em)
                self.ui.tableWidgetActifs.setItem(idx, 6, d_j)
                self.ui.tableWidgetActifs.setItem(idx, 7, d_ech)
                self.ui.tableWidgetActifs.setItem(idx, 8, prix)
                self.ui.tableWidgetActifs.setItem(idx, 9, tx_act)

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = AssetSimulation()
    form.show()
    ap.exec_()