# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles import Ui_Simulation
from DPricer.lib.Obligation import Obligation


class AssetSimulation(QWidget, Ui_Simulation):
    def __init__(self, parent=None):
        super(Ui_Simulation, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Simulation()
        self.ui.setupUi(self)
        self.parent = parent
        self.bag = list()
        pass

    def connect_actions(self):
        self.ui.addTosimulate.clicked.connect(self.add_toolbutton)
        self.ui.removeFromSimulate.clicked.connect(self.remove_toolbutton)
        self.ui.doubleSpinBox.contentChanged.connect(self.update_prices)
        pass

    def add_toolbutton(self):
        if obl not in self.bag:
            self.bag.append(obl)
        pass

    def remove_toolbutton(self):
        self.bag.remove(obl)
        pass

    def update_prices(self):
        for obl in self.bag:
            obl.tx_actuariel += self.ui.doubleSpinBox.getValue()/100.
        pass



    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = AssetSimulation()
    form.show()
    ap.exec_()