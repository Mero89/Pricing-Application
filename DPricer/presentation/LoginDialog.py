# coding=utf-8
__author__ = 'F.Marouane'

import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.Login import Ui_Login
from DPricer.lib.User import User


class MyDialog(QDialog, Ui_Login):
    def __init__(self):
        super(Ui_Login, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.connect(self, QtCore.SIGNAL('accepted()'), self, QtCore.SLOT('check_user()'))
        self.connect(self, QtCore.SIGNAL('rejected()'), self, QtCore.SLOT('check_user()'))
        self.user = None

    # @QtCore.pyqtSignature("")
    # # Call a function when a certain action is triggered
    # # on_[wigetName]_[action]
    # def on_pushButtonSupprimer_clicked(self):
    #     pass

    @QtCore.pyqtSlot()
    def check_user(self):
        usr = str(self.ui.userNameLineEdit.text())
        pwd = str(self.ui.motDePasseLineEdit.text())
        U = User(uname=usr, password=pwd)
        U.check()
        self.user = U
        if not U.logged:
            exit()

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MyDialog()
    form.show()
    ap.exec_()