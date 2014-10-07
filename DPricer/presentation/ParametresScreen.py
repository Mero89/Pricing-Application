# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.Parametres import Ui_Parametres

class Parametre(QDialog, Ui_Parametres):
    def __init__(self, parent=None):
        super(Ui_Parametres, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_Parametres()
        self.ui.setupUi(self)
        pass


    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = Parametre()
    form.show()
    ap.exec_()