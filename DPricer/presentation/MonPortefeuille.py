# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore

from DPricer.presentation.PyuicFiles.AddPFDialog import Ui_AddPFDialog
from DPricer.presentation.PyuicFiles.Portefeuilles import Ui_Portefeuilles
from DPricer.presentation.PyuicFiles.GererPortefeuilles import Ui_GererPortefeuilles
from DPricer.presentation.PyuicFiles.PortefeuilleInput import Ui_PortefeuilleInput
from DPricer.presentation.PyuicFiles.StructurePortefeuille import Ui_StructurePortefeuille

from DPricer.lib.Gestion import Gestion
from DPricer.lib.Panier import Panier
from DPricer.lib.User import User
from DPricer.lib.Controller import DateEval
import DPricer.presentation.TableUtils as TU
from DPricer.lib.Portefeuille import Portefeuille
from DPricer.data.AppModel import AppModel, PortefeuilleMd, GestionMd, ObligationMd
from ConfirmDialog import ConfirmDialog
from GisementScreen import GisementScreen


class Portefeuilles(QWidget, Ui_Portefeuilles):
    def __init__(self, parent=None):
        super(Ui_Portefeuilles, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Portefeuilles()
        self.ui.setupUi(self)
        self.parent = parent
        self.date_eval = DateEval().date_eval
        self.title = 'Mes Portefeuilles'
        self.setWindowTitle(self.title)
        self.ui.tableWidgetPortefeuille.setAlternatingRowColors(True)
        self.user = User()

    @QtCore.pyqtSlot()
    def affichePortefeuille(self):
        self.ui.tableWidgetPortefeuille.itemSelectionChanged.connect(self.update_assets)
        g = Gestion()
        pf = g.portefeuille_of_manager(uid=self.user.uid)
        liste_portefeuille = [Portefeuille(el.p_isin, self.date_eval) for el in pf]
        self.ui.tableWidgetPortefeuille.clearContents()
        self.ui.tableWidgetPortefeuille.setRowCount(len(liste_portefeuille))
        for el in liste_portefeuille:
            idx = liste_portefeuille.index(el)
            row = (str(el.p_isin), str(el.nom), round(el.prix(), 2), round(el.sensibilite(), 4),
                   round(el.duration, 4))
            self.ui.tableWidgetPortefeuille.insertRow(idx)
            TU.insert_row(self.ui.tableWidgetPortefeuille, row, idx)

        self.ui.tableWidgetPortefeuille.resizeRowsToContents()


    def asset_of_portefeuille(self, p_isin, date_eval=None):
        # (Obligation, Qt) <- Portefeuille.obligations
        # ponderation <- Portefeuille.ponderation(isin)
        if date_eval is None:
            date_eval = self.date_eval
        else:
            date_eval = date_eval
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
        self.ui.tableWidgetActifs.setRowCount(len(data))
        for el in data:
            idx = data.index(el)
            # Qstring because of french letters, Nom, Description, etc...
            row = (str(el[0].isin), unicode(el[0].nom), round(el[0].prix(), 2), round(el[0].sensibilite(), 4),
                   round(el[0].duration, 4), str(el[1]), round(el[2], 4))
            self.ui.tableWidgetActifs.insertRow(idx)
            TU.insert_row(self.ui.tableWidgetActifs, row, idx)
        self.ui.tableWidgetActifs.resizeRowsToContents()
            # self.ui.tableWidgetActifs.resizeColumnsToContents()


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
        session.commit()
        if self.parent is not None:
            session.add_all(g_liste)
        try:
            session.commit()
            self.tell_status(u"Portefeuille ajouté avec succès.")
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
                self.session.delete_all(trash)
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


class StructurePortefeuilles(QWidget, Ui_StructurePortefeuille):
    def __init__(self, parent=None):
        super(Ui_StructurePortefeuille, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_StructurePortefeuille()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = u"Gérer structure portefeuille"
        self.setWindowTitle(self.title)
        self.session = AppModel().get_session()
        self.user = User('mero', 'mero')
        self.user.uid = 1
        self.user_pf = None
        self.current_pf = None
        self.oldvalue = None
        # setUp and show gisement screen
        self.gisement_screen = self.load_gisement_screen()
        self.gisement_screen.show()
        self.set_data()
        self.connect_actions()
        self.update_panier_screen()
        self.ui.comboBoxSelect.setFocus()
        self.showMaximized()

    def connect_actions(self):
        self.ui.toolButtonAddToMyPortfolio.clicked.connect(self.add_to_my_portefeuille)
        self.ui.toolButtonRemoveFromMyPortfolio.clicked.connect(self.delete_from_my_portefeuille)
        self.ui.comboBoxSelect.currentIndexChanged.connect(self.update_panier_screen)
        self.ui.tableWidgetStructure.itemPressed.connect(self.edit_quantite)
        self.ui.tableWidgetStructure.itemChanged.connect(self.update_quantite)
        # self.ui.toolButtonRefresh.clicked.connect(self.update_panier_screen)

    def update_quantite(self):
        curr_row = self.ui.tableWidgetStructure.currentRow()
        if curr_row != -1:
            quant = self.ui.tableWidgetStructure.item(curr_row, 2)
            isinitem = self.ui.tableWidgetStructure.item(curr_row, 0)
            isin = str(isinitem.text())
            old_value = self.oldvalue
            new_value = int(quant.text())
            p = Panier()
            rep = p.update_quantite(self.current_pf, isin, new_value)
            if rep == 0:
                self.ui.tableWidgetStructure.clearFocus()
                quant.setText(str(old_value))
            else:
                self.ui.tableWidgetStructure.clearFocus()

    def edit_quantite(self):
        curr_row = self.ui.tableWidgetStructure.currentRow()
        if curr_row != -1:
            quant = self.ui.tableWidgetStructure.item(curr_row, 2)
            value = int(quant.text())
            self.ui.tableWidgetStructure.editItem(quant)
            self.oldvalue = value

    def set_data(self):
        self.populate_combo_box()
        self.user_pf = self.mes_portefeuilles()
        pass

    def actifs_du_portefeuille(self):
        """
        Retourne la liste des Actifs avec leurs quantités respectives.
        :return list((ObligationMd, Quantité)):
        """
        p = Panier()
        nom = unicode(self.ui.comboBoxSelect.currentText())
        p_isin = [el.p_isin for el in self.user_pf if el.nom == nom]
        if len(p_isin) == 1:
            liste_actifs = p.oblig_of_portefeuille(p_isin[0])
            self.current_pf = p_isin[0]
        liste_actifs = [(self.session.query(ObligationMd).get(el[0]), el[1]) for el in liste_actifs]
        return liste_actifs

    def update_panier_screen(self):
        data = self.actifs_du_portefeuille()
        self.ui.tableWidgetStructure.setRowCount(len(data))
        for el in data:
            idx = data.index(el)
            isin = QTableWidgetItem(str(el[0].isin))
            nom = QTableWidgetItem(unicode(el[0].nom))
            quant = QTableWidgetItem(str(el[1]))
            quant.setTextAlignment(QtCore.Qt.AlignHCenter)

            self.ui.tableWidgetStructure.insertRow(idx)
            self.ui.tableWidgetStructure.setItem(idx, 0, isin)
            self.ui.tableWidgetStructure.setItem(idx, 1, nom)
            self.ui.tableWidgetStructure.setItem(idx, 2, quant)
        else:
            self.ui.tableWidgetStructure.resizeColumnToContents(0)
            self.ui.tableWidgetStructure.resizeColumnToContents(1)

    def add_to_my_portefeuille(self):
        """
        Ajoute un actif depuis le gisement au portefeuille géré du gestionnaire.
        :return:
        """
        p = Panier()
        selection = self.gisement_screen.ui.tableWidgetActifs.selectedIndexes()
        if len(selection) >= 1:
            liste_actifs = [str(self.gisement_screen.ui.tableWidgetActifs.itemFromIndex(el).text())
                                  for el in selection if el.column() == 0]
            if self.current_pf:
                [p.add_oblig_to_portefeuille(self.current_pf, isin) for isin in liste_actifs]
        self.gisement_screen.ui.tableWidgetActifs.clearSelection()
        self.update_panier_screen()

    def delete_from_my_portefeuille(self):
        """
        Supprime un portefeuille de ceux initialement gérés.
        :return:
        """
        p = Panier()
        selection = self.ui.tableWidgetStructure.selectedIndexes()
        if len(selection) >= 1:
            liste_actifs = [(el.row(), str(self.ui.tableWidgetStructure.itemFromIndex(el).text()))
                                  for el in selection if el.column() == 0]
            [p.delete_oblig_from_portefeuille(self.current_pf, isin[1]) for isin in liste_actifs]
            [self.ui.tableWidgetStructure.removeRow(isin[0]) for isin in liste_actifs]
            self.ui.tableWidgetStructure.clearSelection()

    def load_gisement_screen(self):
        frame_layout = QVBoxLayout()
        gp = GisementScreen(self.ui.frame)
        # remove unwanted elements
        gp.ui.verticalLayout_3.removeItem(gp.ui.horizontalLayout_2)
        gp.ui.toolButtonDelete.hide()
        gp.ui.toolButtonAdd.hide()
        gp.ui.toolButtonEdit.hide()
        # remove unwanted columns
        for i in range(16, 9, -1):
            gp.ui.tableWidgetActifs.removeColumn(i)
        frame_layout.addWidget(gp)
        self.ui.frame.setLayout(frame_layout)
        return gp

    def mes_portefeuilles(self):
        g = Gestion()
        mes_pf = g.portefeuille_of_manager(self.user.uid)
        return mes_pf

    def populate_combo_box(self):
        mes_pf = self.mes_portefeuilles()
        combo_list = QtCore.QStringList()
        if mes_pf:
            [combo_list.append(unicode(p.nom)) for p in mes_pf]
            comp = QCompleter(combo_list)
            comp.setCaseSensitivity(0)
            self.ui.comboBoxSelect.setCompleter(comp)
            self.ui.comboBoxSelect.addItems(combo_list)


if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = StructurePortefeuilles()
    form.show()
    ap.exec_()