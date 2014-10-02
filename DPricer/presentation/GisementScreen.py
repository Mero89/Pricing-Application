# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.AddAssetDialog import Ui_AddAsset
from DPricer.presentation.PyuicFiles.Gisement import Ui_Gisement
from DPricer.data.AppModel import ObligationMd, AppModel
from DPricer.lib.Obligation import Obligation
from ConfirmDialog import ConfirmDialog


class GisementScreen(QWidget, Ui_Gisement):
    def __init__(self):
        super(Ui_Gisement, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Gisement()
        self.ui.setupUi(self)
        self.title = 'Gisement Obligataire'
        self.setWindowTitle(self.title)
        self.session = AppModel().get_session()
        self.isin_list = list()
        self.nom_list = list()
        self.data = list()
        self.connect_actions()
        self.filter_by_value()
        self.populate_completer()
        self.set_completer_value()
        self.ui.tableWidgetActifs.resizeColumnsToContents()


    def connect_actions(self):
        self.ui.lineEditValeur.textChanged.connect(self.filter_by_value)
        self.ui.comboBoxCritere.currentIndexChanged.connect(self.set_completer_value)
        self.ui.toolButtonAdd.clicked.connect(self.open_add_dialog)
        self.ui.toolButtonEdit.clicked.connect(self.edit_asset)
        self.ui.toolButtonDelete.clicked.connect(self.delete_asset)

    #### TableWidget editing related Method ####

    def open_add_dialog(self):
        # ouvre l'ecran d'ajout d'un actif
        dialog = AddAsset()
        dialog.exec_()
        pass

    def edit_asset(self):
        # édite l'actif choisi
        pass

    def delete_asset(self):
        # supprime l'actif désigné
        selection = self.ui.tableWidgetActifs.selectedIndexes()
        liste_isin = list()
        if len(selection) >= 1:
            for el in selection:
                if el.column() == 0:
                    liste_isin.append((el.row(), str(self.ui.tableWidgetActifs.itemFromIndex(el).text())))
            # confirmation de la suppression
            confirm = ConfirmDialog()
            if len(liste_isin) == 1:
                confirm.set_message(u"Vous êtes sur le point de supprimer l'actif sélectionné")
            else:
                confirm.set_message(u'Vous êtes sur le point de supprimer les actifs sélectionnés')
            rep = confirm.exec_()
            if rep:
                # Suppression de la BDD
                session = AppModel().get_session()
                liste_assets = [session.query(ObligationMd).get(isin[1]) for isin in liste_isin]
                for asset in liste_assets:
                    session.delete(asset)
                else:
                    try:
                        session.commit()
                    except:
                        session.rollback()
                self.filter_by_value()
                self.populate_completer()
                self.set_completer_value()


    ##### TableWidget related Methods #####
    @QtCore.pyqtSlot()
    def set_completer_value(self):
        """
        Complete la saisie de l'utilisateur en fonction des données disponibles dans la base de données
        :return:
        """
        if self.ui.comboBoxCritere.currentText() == 'ISIN':
            value_list = self.isin_list
        elif self.ui.comboBoxCritere.currentText() == 'NOM':
            value_list = self.nom_list
        completer = QCompleter(value_list, self)
        completer.setCaseSensitivity(2)
        completer.setCompletionMode(0)
        self.ui.lineEditValeur.setCompleter(completer)

    @QtCore.pyqtSlot()
    def filter_by_value(self):
        # All data
        if self.ui.lineEditValeur.text() == '':
            self.data = self.session.query(ObligationMd).all()
        else:
            # criterion = ISIN or NOM
            if self.ui.comboBoxCritere.currentText() == 'ISIN':
                self.data = self.session.query(ObligationMd).filter_by(isin=str(self.ui.lineEditValeur.text())).all()
            elif self.ui.comboBoxCritere.currentText() == 'NOM':
                self.data = self.session.query(ObligationMd).filter_by(nom=unicode(self.ui.lineEditValeur.text())).all()
        if self.data:
            if self.ui.tableWidgetActifs.isSortingEnabled():
                self.ui.tableWidgetActifs.setSortingEnabled(False)
            self.populate_table()
            self.ui.tableWidgetActifs.setSortingEnabled(True)

    def populate_completer(self):
        self.isin_list = [el.isin for el in self.data]
        self.nom_list = [el.nom for el in self.data]

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
                ttype = QTableWidgetItem(str(el.type))
                echue = QTableWidgetItem(str(el.echue))
                forcee = QTableWidgetItem(str(el.forcee))
                obl = Obligation(el.nominal, el.taux_facial, el.date_emission, el.date_jouissance, el.maturite,
                                 d_eval='22/9/2014', spread=el.spread)
                prix = QTableWidgetItem(str(obl.prix()) + ' MAD')
                sensi = QTableWidgetItem(str(obl.sensibilite()))
                dur = QTableWidgetItem(str(obl.duration()))
                conv = QTableWidgetItem(str('Not Implemented'))
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
                self.ui.tableWidgetActifs.setItem(idx, 8, ttype)
                self.ui.tableWidgetActifs.setItem(idx, 9, echue)
                self.ui.tableWidgetActifs.setItem(idx, 10, forcee)
                self.ui.tableWidgetActifs.setItem(idx, 11, prix)
                self.ui.tableWidgetActifs.setItem(idx, 12, sensi)
                self.ui.tableWidgetActifs.setItem(idx, 13, dur)
                self.ui.tableWidgetActifs.setItem(idx, 14, conv)
                self.ui.tableWidgetActifs.setItem(idx, 15, tx_act)

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()


class AddAsset(QDialog, Ui_AddAsset):
    def __init__(self):
        super(Ui_AddAsset, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_AddAsset()
        self.ui.setupUi(self)
        self.title = 'Ajouter Actif'
        self.setWindowTitle(self.title)

    @QtCore.pyqtSlot()
    def toolButtonAjouter(self):
        num = self.ui.tableWidget.rowCount()
        dd = QTableWidgetItem()
        ff = QTableWidgetItem()
        self.ui.tableWidget.insertRow(num)
        self.ui.tableWidget.setItem(num, 0, dd)
        self.ui.tableWidget.setItem(num, 1, ff)


if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = GisementScreen()
    form.show()
    ap.exec_()