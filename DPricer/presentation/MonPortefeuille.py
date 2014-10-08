# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore

from DPricer.presentation.PyuicFiles.AddPFDialog import Ui_AddPFDialog
from DPricer.presentation.PyuicFiles.Portefeuilles import Ui_Portefeuilles
from DPricer.presentation.PyuicFiles.GererPortefeuilles import Ui_GererPortefeuilles
from DPricer.presentation.PyuicFiles.PortefeuilleInput import Ui_PortefeuilleInput

from DPricer.lib.Gestion import Gestion
from DPricer.lib.User import User

from DPricer.lib.Portefeuille import Portefeuille
from DPricer.data.AppModel import AppModel, PortefeuilleMd, GestionMd
from ConfirmDialog import ConfirmDialog


class Portefeuilles(QWidget, Ui_Portefeuilles):
    def __init__(self, parent=None):
        super(Ui_Portefeuilles, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Portefeuilles()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = 'Mes Portefeuilles'
        self.setWindowTitle(self.title)
        self.ui.tableWidgetPortefeuille.setAlternatingRowColors(True)
        self.user = None

    @QtCore.pyqtSlot()
    def affichePortefeuille(self):
        self.ui.tableWidgetPortefeuille.itemSelectionChanged.connect(self.update_assets)
        g = Gestion()
        pf = g.portefeuille_of_manager(uid=self.user.uid)
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
            # self.ui.tableWidgetPortefeuille.resizeColumnsToContents()
        self.ui.tableWidgetPortefeuille.setRowCount(len(liste_portefeuille))

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
            # self.ui.tableWidgetActifs.resizeColumnsToContents()
        self.ui.tableWidgetActifs.setRowCount(len(data))

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_Q:
            self.close()

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)


class PortefeuilleDialog(QDialog, Ui_AddPFDialog):
    def __init__(self, parent=None):
        super(Ui_AddPFDialog, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_AddPFDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.setWindowTitle('Ajout de Portefeuilles')
        self.accepted.connect(self.save_portefeuille)
        self.ui.pushButtonAjouter.clicked.connect(self.ajouter_clicked)
        self.ui.pushButtonSupprimer.clicked.connect(self.supprimer_clicked)

    @QtCore.pyqtSlot()
    def save_portefeuille(self):
        num = self.ui.tableWidget.rowCount()
        pf_liste = list()
        g_liste = list()
        if num >= 1:
            for i in range(num):
                isin = self.ui.tableWidget.item(i, 0).text()
                nom = self.ui.tableWidget.item(i, 1).text()
                if isin != str and nom != str:
                    pf_liste.append(PortefeuilleMd(p_isin=str(isin), nom=str(nom)))
                    if self.parent is not None:
                        g_liste.append(GestionMd(uid=self.parent.user.uid, p_isin=str(isin)))
        session = AppModel().get_session()
        session.add_all(pf_liste)
        if self.parent is not None:
            session.add_all(g_liste)
        try:
            session.commit()
            self.tell_status("Portefeuille ajouté avec succès.")
        except Exception as e:
            print e.message
            session.rollback()

    @QtCore.pyqtSlot()
    def ajouter_clicked(self):
        num = self.ui.tableWidget.rowCount()
        dd = QTableWidgetItem()
        ff = QTableWidgetItem()
        self.ui.tableWidget.insertRow(num)
        self.ui.tableWidget.setItem(num, 0, dd)
        self.ui.tableWidget.setItem(num, 1, ff)
        self.ui.tableWidget.setFocus()

    @QtCore.pyqtSlot()
    def supprimer_clicked(self):
        itm = self.ui.tableWidget.currentItem()
        idx = self.ui.tableWidget.indexFromItem(itm)
        self.ui.tableWidget.removeRow(idx.row())

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)


class GererPortefeuille(QWidget, Ui_GererPortefeuilles):
    def __init__(self, parent=None):
        super(Ui_GererPortefeuilles, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_GererPortefeuilles()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = u'Gérer les Portefeuilles'
        self.setWindowTitle(self.title)
        self.session = AppModel().get_session()
        self.user = User('mero','mero')
        self.user.uid = 1
        self.connect_actions()
        self.affiche_gisement_portefeuille()
        self.affiche_mes_portefeuille()
        self.before = None

    def get_row(self, table):
        """
        Extrait les données séléctionnées depuis une table.
        :return:
        """
        data = dict()
        row = table.currentRow()
        data['p_isin'] = str(table.item(row, 0).text())
        data['nom'] = unicode(table.item(row, 1).text())
        return data

    def connect_actions(self):
        self.ui.toolButtonAdd.clicked.connect(self.new_portefeuille)
        self.ui.toolButtonRemove.clicked.connect(self.delete_portefeuille)
        self.ui.toolButtonAddToMyPortfolio.clicked.connect(self.add_to_my_portefeuille)
        self.ui.toolButtonRemoveFromMyPortfolio.clicked.connect(self.remove_from_my_portefeuille)
        self.ui.toolButtonEdit.clicked.connect(self.update_portfeuille)

    def new_portefeuille(self):
        """
        Ajoute un nouveau portefeuille.
        :return:
        """
        P = PortefeuilleDialog(parent=self.parent)
        rep = P.exec_()
        if rep:
            self.affiche_gisement_portefeuille()

    def add_to_my_portefeuille(self):
        """
        Ajoute un portefeuille depuis le gisement au portefeuille du gestionnaire.
        :return:
        """
        g = Gestion()
        selection = self.ui.tableWidgetGisementPortefeuille.selectedIndexes()
        if len(selection) >= 1:
            liste_portefeuille = [str(self.ui.tableWidgetGisementPortefeuille.itemFromIndex(el).text())
                                  for el in selection if el.column() == 0]
            [g.add_portofolio(self.user.uid, isin) for isin in liste_portefeuille]
            self.affiche_mes_portefeuille()

    def remove_from_my_portefeuille(self):
        """
        Supprime un portefeuille de ceux initialement gérés.
        :return:
        """
        g = Gestion()
        selection = self.ui.tableWidgetPortefeuilles.selectedIndexes()
        if len(selection) >= 1:
            liste_portefeuille = [(el.row(), str(self.ui.tableWidgetPortefeuilles.itemFromIndex(el).text()))
                                  for el in selection if el.column() == 0]
            [g.remove_portofolio(self.user.uid, isin[1]) for isin in liste_portefeuille]
            [self.ui.tableWidgetPortefeuilles.removeRow(isin[0]) for isin in liste_portefeuille]

    def update_portfeuille(self):
        matable = self.ui.tableWidgetGisementPortefeuille
        old_row = self.get_row(matable)
        self.before = old_row
        edit = EditPortefeuille(old_row, self)
        edit.exec_()

    @QtCore.pyqtSlot(dict)
    def save_edit(self, data):
        old = self.before
        d = data
        self.session.query(PortefeuilleMd).filter_by(p_isin=old['p_isin']).update(d)
        try:
            self.session.commit()
            self.tell_status(u'Modification éffectuée avec succès.')
        except Exception as e:
            self.session.rollback()
            self.tell_status(u'Une erreur est survenue lors de la modification.')
            self.tell_status(e.message)
        self.affiche_mes_portefeuille()
        self.affiche_gisement_portefeuille()

    def delete_portefeuille(self):
        """
        Supprime un portefeuille de la base de données.
        :return:
        """
        selection = self.ui.tableWidgetGisementPortefeuille.selectedIndexes()
        if len(selection) >= 1:
            liste_portefeuille = [(el.row(), str(self.ui.tableWidgetGisementPortefeuille.itemFromIndex(el).text()))
                                   for el in selection if el.column() == 0]
            confirm = ConfirmDialog(self)
            if len(liste_portefeuille) == 1:
                confirm.set_message(u"Vous êtes sur le point de supprimer le portefeuille sélectionné")
            else:
                confirm.set_message(u'Vous êtes sur le point de supprimer les portefeuilles sélectionnés')
            rep = confirm.exec_()
            if rep:
                trash = [self.session.query(PortefeuilleMd).get(isin[1]) for isin in liste_portefeuille]
                for garbage in trash:
                    self.session.delete(garbage)
                else:
                    try:
                        self.session.commit()
                        self.tell_status(u"Portefeuilles(s) supprimé(s) avec succès.")
                        [self.ui.tableWidgetGisementPortefeuille.removeRow(el[0]) for el in liste_portefeuille]
                    except:
                        self.session.rollback()
                        self.tell_status(u"Suppression échouée.")

    def affiche_mes_portefeuille(self):
        """
        Affiche les portefeuilles du gestionnaire.
        :return:
        """
        g = Gestion()
        liste_portefeuille = g.portefeuille_of_manager(uid=self.user.uid)
        if liste_portefeuille:
            self.populate_table_portefeuille(self.ui.tableWidgetPortefeuilles, liste_portefeuille)

    def affiche_gisement_portefeuille(self):
        """
        Affiche les potefeuilles du gisement.
        :return:
        """
        gisement = self.session.query(PortefeuilleMd).all()
        if gisement:
            self.populate_table_portefeuille(self.ui.tableWidgetGisementPortefeuille, gisement)

    def populate_table_portefeuille(self, table, pf_list):
        """
        Remplit une tableWidget [table] par les informations fournies dans [pf_list]
        :param table:
        :param pf_list:
        :return:
        """
        table.clearContents()
        num_rows = table.rowCount()
        for el in pf_list:
            idx = pf_list.index(el)
            isin = QTableWidgetItem(str(el.p_isin))
            nom = QTableWidgetItem(str(el.nom))
            if idx + 1 >= num_rows:
                table.insertRow(idx)
            table.setItem(idx, 0, isin)
            table.setItem(idx, 1, nom)
        table.resizeRowsToContents()
        # table.resizeColumnsToContents()
        table.setRowCount(len(pf_list))

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)


class EditPortefeuille(QDialog, Ui_PortefeuilleInput):
    def __init__(self, data, parent=None):
        super(Ui_PortefeuilleInput, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_PortefeuilleInput()
        self.ui.setupUi(self)
        self.old_data = data
        self.new_data = dict()
        self.parent = parent
        self.set_data()
        self.ui.buttonBox.accepted.connect(self.get_data)
        self.ui.buttonBox.rejected.connect(self.close)
        if self.parent:
            self.connect(self, QtCore.SIGNAL('edited'), self.parent.save_edit)

    def set_data(self):
        self.ui.isinLineEdit.setText(self.old_data['p_isin'])
        self.ui.nomDuPortefeuilleLineEdit.setText(self.old_data['nom'])

    def get_data(self):
        self.new_data['p_isin'] = str(self.ui.isinLineEdit.text())
        self.new_data['nom'] = unicode(self.ui.nomDuPortefeuilleLineEdit.text())
        self.emit(QtCore.SIGNAL('edited'), self.new_data)

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = GererPortefeuille()
    form.show()
    ap.exec_()