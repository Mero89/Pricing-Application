# coding=utf-8
from PyQt4.QtCore import SIGNAL

__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from MDI import Ui_MDIApp
from EcheancierDialog import EcheancierDialog
from LoginDialog import MyDialog
from MonPortefeuille import Portfolios
from DPricer.lib.User import User
from AddPortefeuilleDialog import PortefeuilleDialog


class MyClass(QMainWindow, Ui_MDIApp):
    def __init__(self):
        super(Ui_MDIApp, self).__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MDIApp()
        self.ui.setupUi(self)
        # log = MyDialog()
        # self.connect(log, QtCore.SIGNAL('accepted()'), self, QtCore.SLOT('stats()'))
        # log.exec_()
        self.user = User('uname', 'password')
        self.user.uid = 1
        # self.user = log.user
        nom = 'FAKIR'
        prenom = 'Marouane'
        self.ui.labelUser.setText(nom + ' ' + prenom)
        cur_day = QtCore.QDate().currentDate().toString()
        self.ui.labelDates.setText(cur_day)
        ##
        self.launched = QtCore.pyqtSignal(int)
        ##
        self.connect(self.ui.actionMonPortefeuille, QtCore.SIGNAL('triggered()'), self, QtCore.SLOT('affiche()'))
        self.connect(self.ui.actionAjoutPortefeuille, QtCore.SIGNAL('triggered()'), self.open_portefeuille_dialog)

    @QtCore.pyqtSlot()
    def open_portefeuille_dialog(self):
        pfdial = PortefeuilleDialog()
        self.ui.mdiArea.addSubWindow(pfdial)
        pfdial.show()

    @QtCore.pyqtSlot()
    def affiche(self):
        pf = Portfolios()
        self.ui.mdiArea.addSubWindow(pf)
        self.connect(pf.ui.tableWidgetPortefeuille, QtCore.SIGNAL('itemSelectionChanged()'), self.stats)
        # self.connect(pf.ui.pushButtonFermer, QtCore.SIGNAL('clicked()'), self.ui.mdiArea.closeActiveSubWindow)
        pf.ui.pushButtonFermer.clicked()
        pf.User = self.user
        pf.show()
        pf.affichePortefeuille()

    @QtCore.pyqtSlot()
    def filenew(self):
        wnd = QDialog()
        self.ui.mdiArea.addSubWindow(wnd)
        wnd.show()

    @QtCore.pyqtSlot()
    def title_all(self):
        i = 0
        for wndw in self.ui.mdiArea.subWindowList():
            i += 1
            wndw.setWindowTitle('Window {}'.format(i))


    # @QtCore.pyqtSlot(int,int)
    @QtCore.pyqtSlot()
    def stats(self):
        self.ui.statusbar.showMessage('Signal received row:{}, col:{} !!!!', 3500)
        # self.ui.statusbar.showMessage('Signal received !!!!', 3500)

    @QtCore.pyqtSlot()
    def action_stats(self):
        self.ui.statusbar.showMessage('Action Triggered !!!!', 2000)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.filenew()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MyClass()
    form.show()
    ap.exec_()
