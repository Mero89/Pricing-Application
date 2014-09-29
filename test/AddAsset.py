# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from AddAssetDialog import Ui_AddAsset


class AddAsset(QDialog, Ui_AddAsset):
    def __init__(self):
        super(Ui_AddAsset, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_AddAsset()
        self.ui.setupUi(self)


    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = AddAsset()
    form.show()
    ap.exec_()