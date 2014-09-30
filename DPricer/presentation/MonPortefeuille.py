# coding=utf-8
__author__ = 'F.Marouane'

import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore

from .PyuicFiles.AddPFDialog import Ui_AddPFDialog
from .PyuicFiles.Portefeuilles import Ui_Portefeuilles
from DPricer.lib.Gestion import Gestion
from DPricer.lib.Portefeuille import Portefeuille
from DPricer.data.AppModel import AppModel, PortefeuilleMd


class Portfolios(QWidget, Ui_Portefeuilles):
    def __init__(self):
        super(Ui_Portefeuilles, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Portefeuilles()
        self.ui.setupUi(self)
        self.User = None
        self.ui.tableWidgetPortefeuille.setAlternatingRowColors(True)

    @QtCore.pyqtSlot()
    def affichePortefeuille(self):
        self.ui.tableWidgetPortefeuille.itemSelectionChanged.connect(self.update_assets)
        g = Gestion()
        pf = g.portefeuille_of_manager(uid=self.User.uid)
        liste_portefeuille = [Portefeuille(el.p_isin, '22/9/2014') for el in pf]
        self.ui.tableWidgetPortefeuille.clearContents()
        cur_rows = self.ui.tableWidgetPortefeuille.rowCount()
        for el in liste_portefeuille:
            idx = liste_portefeuille.index(el)
            isin = QTableWidgetItem(str(el.p_isin))
            nom = QTableWidgetItem(str(el.nom))
            prix = QTableWidgetItem(str(round(el.prix(),2)))
            sensi = QTableWidgetItem(str(round(el.sensibilite(),4)))
            dur = QTableWidgetItem(str(round(el.duration(),4)))
            if idx +1 >= cur_rows:
                self.ui.tableWidgetPortefeuille.insertRow(idx)
            self.ui.tableWidgetPortefeuille.setItem(idx, 0, isin)
            self.ui.tableWidgetPortefeuille.setItem(idx, 1, nom)
            self.ui.tableWidgetPortefeuille.setItem(idx, 2, prix)
            self.ui.tableWidgetPortefeuille.setItem(idx, 3, sensi)
            self.ui.tableWidgetPortefeuille.setItem(idx, 4, dur)
            self.ui.tableWidgetPortefeuille.resizeRowsToContents()
            self.ui.tableWidgetPortefeuille.resizeColumnsToContents()

    def asset_of_portefeuille(self, p_isin, date_eval='22/9/2014'):
        # (Obligation, Qt) <- Portefeuille.obligations
        # ponderation <- Portefeuille.ponderation(isin)
        pf = Portefeuille(str(p_isin), date_eval)
        assets = pf.obligations
        # ==> [..., [Obligation ,Qt, Poids], ....]
        pour_afficher = [[el[0], el[1], pf.ponderation(el[0].isin)] for el in assets]
        return pour_afficher


    @QtCore.pyqtSlot()
    def update_assets(self):
        self.ui.tableWidgetActifs.clearContents()
        cur_item = self.ui.tableWidgetPortefeuille.currentItem()
        p_isin = self.ui.tableWidgetPortefeuille.item(cur_item.row(), 0).text()
        data = self.asset_of_portefeuille(p_isin)
        cur_rows = self.ui.tableWidgetActifs.rowCount()
        for el in data:
            idx = data.index(el)
            isin = QTableWidgetItem(str(el[0].isin))
            # Qstring because of french letters, Nom, Description, etc...
            nom = QTableWidgetItem(QtCore.QString(el[0].nom))
            prix = QTableWidgetItem(str(round(el[0].prix(), 2)))
            sensi = QTableWidgetItem(str(round(el[0].sensibilite(), 4)))
            dur = QTableWidgetItem(str(round(el[0].duration(), 4)))
            quant = QTableWidgetItem(str(el[1]))
            poids = QTableWidgetItem(str(round(el[2], 4)))
            if idx + 1 >= cur_rows:
                self.ui.tableWidgetActifs.insertRow(idx)
            self.ui.tableWidgetActifs.setItem(idx, 0, isin)
            self.ui.tableWidgetActifs.setItem(idx, 1, nom)
            self.ui.tableWidgetActifs.setItem(idx, 2, quant)
            self.ui.tableWidgetActifs.setItem(idx, 3, poids)
            self.ui.tableWidgetActifs.setItem(idx, 4, prix)
            self.ui.tableWidgetActifs.setItem(idx, 5, sensi)
            self.ui.tableWidgetActifs.setItem(idx, 6, dur)
            self.ui.tableWidgetActifs.resizeRowsToContents()
            self.ui.tableWidgetActifs.resizeColumnsToContents()

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_Q:
            self.close()


class PortefeuilleDialog(QDialog, Ui_AddPFDialog):
    def __init__(self):
        super(Ui_AddPFDialog, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_AddPFDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Ajout de Portefeuilles')
        self.accepted.connect(self.save_portefeuille)
        self.ui.pushButtonAjouter.clicked.connect(self.Ajouter_clicked)
        self.ui.pushButtonSupprimer.clicked.connect(self.Supprimer_clicked)

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
    ap = QApplication(sys.argv)
    form = Portfolios()
    form.show()
    ap.exec_()