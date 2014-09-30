# coding=utf-8
from DPricer.presentation import AddAsset, GisementScreen

__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.MDI import Ui_MDIApp
from DPricer.presentation.LoginDialog import MyDialog
from DPricer.presentation.MonPortefeuille import Portfolios, PortefeuilleDialog
from DPricer.presentation.CourbeTauxScreen import CourbeTaux


class MyClass(QMainWindow, Ui_MDIApp):
    def __init__(self):
        super(Ui_MDIApp, self).__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MDIApp()
        self.ui.setupUi(self)
        log = MyDialog()
        log.accepted.connect(self.stats)
        log.exec_()
        # self.user = User('uname', 'password')
        # self.user.uid = 1
        self.user = log.user
        nom = 'FAKIR'
        prenom = 'Marouane'
        self.ui.labelUser.setText(nom + ' ' + prenom)
        cur_day = QtCore.QDate().currentDate().toString()
        self.ui.labelDates.setText(cur_day)
        self.connect_actions()

    def connect_actions(self):
        self.ui.actionMonPortefeuille.triggered.connect(self.open_portefeuille_screen)
        self.ui.actionAjoutPortefeuille.triggered.connect(self.open_portefeuille_dialog)
        self.ui.actionVisualiser.triggered.connect(self.open_courbe_screen)
        self.ui.actionGisement.triggered.connect(self.open_gisement_screen)
        self.ui.actionAjoutObligation.triggered.connect(self.open_add_asset_screen)

    @QtCore.pyqtSlot()
    def open_add_asset_screen(self):
        ct = AddAsset()
        ct.setWindowTitle('Ajouter Actif')
        self.ui.mdiArea.addSubWindow(ct)
        ct.show()

    @QtCore.pyqtSlot()
    def open_gisement_screen(self):
        ct = GisementScreen()
        self.ui.mdiArea.addSubWindow(ct)
        ct.show()

    @QtCore.pyqtSlot()
    def open_courbe_screen(self):
        ct = CourbeTaux()
        self.ui.mdiArea.addSubWindow(ct)
        ct.show()

    @QtCore.pyqtSlot()
    def open_portefeuille_dialog(self):
        pfdial = PortefeuilleDialog()
        # self.ui.mdiArea.addSubWindow(pfdial)
        pfdial.exec_()

    @QtCore.pyqtSlot()
    def open_portefeuille_screen(self):
        pf = Portfolios()
        self.ui.mdiArea.addSubWindow(pf)
        pf.ui.tableWidgetPortefeuille.itemSelectionChanged.connect(self.stats)
        pf.ui.pushButtonFermer.clicked.connect(self.ui.mdiArea.closeActiveSubWindow)
        pf.User = self.user
        pf.show()
        pf.affichePortefeuille()

    @QtCore.pyqtSlot()
    def filenew(self):
        wnd = QDialog()
        self.ui.mdiArea.addSubWindow(wnd)
        wnd.show()

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
        # Comment to commit


if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MyClass()
    form.show()
    ap.exec_()
