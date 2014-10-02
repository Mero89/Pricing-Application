# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.ConfirmDialog import Ui_ConfirmDialog


class ConfirmDialog(QDialog, Ui_ConfirmDialog):
    def __init__(self):
        super(Ui_ConfirmDialog, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)

    def set_message(self, message):
        self.ui.label.setText(message)

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = ConfirmDialog()
    if form.exec_():
        print 'ok pressed'
        form.close()
    ap.exec_()