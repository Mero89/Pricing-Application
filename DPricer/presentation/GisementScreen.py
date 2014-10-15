# coding=utf-8
__author__ = 'F.Marouane'

import sys
import datetime as dt
from PyQt4.QtGui import *
from PyQt4 import QtCore
import TableUtils as TU
from DPricer.presentation.PyuicFiles.AddAssetDialog import Ui_AddAsset
from DPricer.presentation.PyuicFiles.Gisement import Ui_Gisement
from DPricer.data.AppModel import ObligationMd, AppModel
from DPricer.lib.Obligation import Obligation
from ConfirmDialog import ConfirmDialog


class GisementScreen(QWidget, Ui_Gisement):
    def __init__(self, parent=None):
        super(Ui_Gisement, self).__init__(parent)
        QWidget.__init__(self)
        self.parent = parent
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
        # self.ui.tableWidgetActifs.resizeColumnsToContents()

    def connect_actions(self):
        self.ui.lineEditValeur.textChanged.connect(self.filter_by_value)
        self.ui.comboBoxCritere.currentIndexChanged.connect(self.set_completer_value)
        # self.ui.toolButtonEdit.clicked.connect(self.edit_asset)
        # parent's connect
        if self.parent is not None and type(self.parent) is not QFrame:
            self.ui.toolButtonDelete.clicked.connect(self.delete_asset)
            self.ui.toolButtonAdd.clicked.connect(self.parent.open_add_asset_screen)
            self.ui.toolButtonEdit.clicked.connect(self.edit_asset)
            self.connect(self, QtCore.SIGNAL('modified'), self.parent.update_asset_screen)

    # Modifie un actif
    def edit_asset(self):
        row = self.ui.tableWidgetActifs.currentRow()
        data = dict()
        data['isin'] = self.ui.tableWidgetActifs.item(row, 0).text()
        data['nom'] = self.ui.tableWidgetActifs.item(row, 1).text()
        data['nominal'] = self.ui.tableWidgetActifs.item(row, 2).text()
        data['taux_facial'] = str(self.ui.tableWidgetActifs.item(row, 3).text()).split('%')[0]
        data['spread'] = str(self.ui.tableWidgetActifs.item(row, 4).text()).split('%')[0]
        data['date_emission'] = self.ui.tableWidgetActifs.item(row, 5).text()
        data['date_jouissance'] = self.ui.tableWidgetActifs.item(row, 6).text()
        data['maturite'] = self.ui.tableWidgetActifs.item(row, 7).text()
        data['type'] = str(self.ui.tableWidgetActifs.item(row, 8).text())
        self.emit(QtCore.SIGNAL('modified'), data)

    # Supprime l'actif choisi
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
                trash = [session.query(ObligationMd).get(isin[1]) for isin in liste_isin]
                session.delete_all(trash)
                try:
                    session.commit()
                    self.tell_status(u"Actif(s) supprimé(s) avec succès.")
                    [self.ui.tableWidgetActifs.removeRow(el[0]) for el in liste_isin]
                except Exception as e:
                    session.rollback()
                    self.tell_status(u"Suppression échouée.")
                    self.tell_status(e.message)
                self.populate_completer()

    # Configure l'auto-completion en fonction du critère choisi
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

    # filtre la liste des actifs selon le critère choisi
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

    # Fournit la liste de l'auto-completion
    def populate_completer(self):
        self.isin_list = [el.isin for el in self.data]
        self.nom_list = [el.nom for el in self.data]

    # Remplit la table
    def populate_table(self):
        self.ui.tableWidgetActifs.clearContents()
        keys = ['isin', 'nom', 'nominal', 'taux_facial', 'spread', 'date_emission', 'date_jouissance', 'maturite',
                'type', 'echue', 'forcee']
        if self.data:
            self.ui.tableWidgetActifs.setRowCount(len(self.data))
            # populate table
            for el in self.data:
                row = self.data.index(el)
                obl = Obligation(el.nominal, el.taux_facial, el.date_emission, el.date_jouissance, el.maturite,
                                 d_eval='2/10/2014', spread=el.spread)
                calcul = [obl.prix(), obl.sensibilite(), obl.duration(), 'Not Implemented', obl.tx_actuariel +
                          obl.spread]
                # self.ui.tableWidgetActifs.insertRow(row)
                self.ui.tableWidgetActifs.setRowHeight(row, 27)
                TU.put_row(self.ui.tableWidgetActifs, row, keys, el)
                TU.insert_row(self.ui.tableWidgetActifs, calcul, row, offset=len(keys))

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()


#### UPDATE ASSET ####
class UpdateAsset(QWidget, Ui_AddAsset):
    def __init__(self, data, parent=None):
        super(Ui_AddAsset, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_AddAsset()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = 'Modifier Actif'
        self.setWindowTitle(self.title)
        self.choix = {'3': 'AMCREV', '0': 'N', '1': 'AMC', '2': 'REV'}
        self.ui.buttonBox.accepted.connect(self.get_data)
        self.ui.isinLineEdit.setReadOnly(1)
        if data:
            self.data = data
            self.put_data(data)

    def put_data(self, data):
        """
        affiche les données voulues à l'écran.
        :param data: dict
        :return:
        """
        indices_choix = {'AMCREV': '3', 'N': '0', 'AMC': '1', 'REV': '2'}
        self.ui.isinLineEdit.setText(data['isin'])
        self.ui.nomLineEdit.setText(data['nom'])
        self.ui.nominalLineEdit.setText(data['nominal'])
        self.ui.doubleSpinBoxTauxFacial.setValue(float(data['taux_facial']))
        self.ui.doubleSpinBoxSpread.setValue(float(data['spread']))
        self.ui.dateEditDateEmission.setDate(self.date_to_qdate(data['date_emission']))
        self.ui.dateEditDateJouissance.setDate(self.date_to_qdate(data['date_jouissance']))
        self.ui.dateEditDateEcheance.setDate(self.date_to_qdate(data['maturite']))
        self.ui.typeComboBox.setCurrentIndex(int(indices_choix[data['type']]))

    def get_data(self):
        # extrait les données saisies
        self.data['isin'] = str(self.ui.isinLineEdit.text())
        self.data['nom'] = unicode(self.ui.nomLineEdit.text())
        self.data['nominal'] = self.validate_float(self.ui.nominalLineEdit.text())
        self.data['taux_facial'] = self.ui.doubleSpinBoxTauxFacial.value() / 100.
        self.data['spread'] = self.ui.doubleSpinBoxSpread.value() / 100.
        self.data['date_emission'] = self.convert_qdate(self.ui.dateEditDateEmission.date().getDate())
        self.data['date_jouissance'] = self.convert_qdate(self.ui.dateEditDateJouissance.date().getDate())
        self.data['maturite'] = self.convert_qdate(self.ui.dateEditDateEcheance.date().getDate())
        self.data['type'] = self.choix[str(self.ui.typeComboBox.currentIndex())]
        # self.data['forcee'] = self.ui.forcerCheckBox.isChecked()
        if self.data['maturite'] < dt.date.today():
            self.data['echue'] = False
        else:
            self.data['echue'] = True
        missing = list()
        for key, value in self.data.items():
            if not value and type(value) is not bool:
                missing.append(key)
        if len(missing) >= 1:
            confirm = ConfirmDialog()
            confirm.set_message('les champs suivants sont manquants:\n {}'.format(missing))
            confirm.exec_()
        else:
            self.update_asset()

    def update_asset(self):
        d = self.data
        session = AppModel().get_session()
        session.query(ObligationMd).filter_by(isin=d['isin']).update(d)
        try:
            session.commit()
            self.tell_status(u'Modifications enregistrées.')
        except Exception as e:
            session.rollback()
            self.tell_status(u'Une erreur est survenue lors de la modification.')
            self.tell_status(e.message)

    def validate_float(self, _num):
        if _num == '':
            return 0
        else:
            return float(_num)

    def date_to_qdate(self, _sdate):
        _date = dt.datetime.strptime(str(_sdate), '%Y-%m-%d')
        _qdate = QtCore.QDate(_date.year, _date.month, _date.day)
        return _qdate

    def convert_qdate(self, _qdate):
        return dt.date(_qdate[0], _qdate[1], _qdate[2])

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)


#### ADD ASSET CLASS ####
class AddAsset(QWidget, Ui_AddAsset):
    def __init__(self, parent=None):
        super(Ui_AddAsset, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_AddAsset()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = 'Ajouter Actif'
        self.setWindowTitle(self.title)
        self.data = dict()
        self.choix = {'3':'AMCREV','0':'N', '1':'AMC','2':'REV'}
        # self.ui.toolButtonAdd.clicked.connect(self.toolButtonAjouter)
        # self.ui.toolButtonRemove.clicked.connect(self.toolButtonSupprimer)
        self.ui.buttonBox.accepted.connect(self.get_data)
        # self.ui.buttonBox.rejected.connnect(self.parent.remove)

    def get_data(self):
        # extrait les données saisies
        self.data['isin'] = str(self.ui.isinLineEdit.text())
        self.data['nom'] = unicode(self.ui.nomLineEdit.text())
        self.data['nominal'] = self.validate_float(self.ui.nominalLineEdit.text())
        self.data['taux_facial'] = self.ui.doubleSpinBoxTauxFacial.value()/100.
        self.data['spread'] = self.ui.doubleSpinBoxSpread.value()/100.
        self.data['date_emission'] = self.convert_qdate(self.ui.dateEditDateEmission.date().getDate())
        self.data['date_jouissance'] = self.convert_qdate(self.ui.dateEditDateJouissance.date().getDate())
        self.data['maturite'] = self.convert_qdate(self.ui.dateEditDateEcheance.date().getDate())
        self.data['type'] = self.choix[str(self.ui.typeComboBox.currentIndex())]
        # self.data['forcee'] = self.ui.forcerCheckBox.isChecked()
        if self.data['maturite'] < dt.date.today():
            self.data['echue'] = False
        else:
            self.data['echue'] = True
        missing = list()
        for key, value in self.data.items():
            if not value and type(value) is not bool:
                missing.append(key)
        if len(missing) >= 1:
            confirm = ConfirmDialog()
            confirm.set_message('les champs suivants sont manquants:\n {}'.format(missing))
            confirm.exec_()
        else:
            self.save_asset()

    def save_asset(self):
        d = self.data
        session = AppModel().get_session()
        # Enregistre les données saisies
        obl = ObligationMd(isin=d['isin'], nom=d['nom'], nominal=d['nominal'],
                           taux_facial=d['taux_facial'], spread=d['spread'], date_emission=d['date_emission'],
                           date_jouissance=d['date_jouissance'], forcee=False,
                           maturite=d['maturite'], type=d['type'], echue=d['echue'])
        if session.query(ObligationMd).get(obl.isin):
            confirm = ConfirmDialog(self)
            confirm.set_message(u"l'actif fourni existe déjà dans la base de données.")
            confirm.exec_()
        elif not session.query(ObligationMd).get(obl.isin):
            session.add(obl)
            try:
                session.commit()
                self.tell_status(u'Actif ajouté avec succès.')
            except Exception as e:
                self.tell_status(u'Actif non ajouté.')
                session.rollback()
                self.tell_status(e.message)

    def validate_float(self, _num):
        if _num == '':
            return 0
        else:
            return float(_num)

    def date_to_qdate(self, _date):
        _qdate = QtCore.QDate(_date.year, _date.month, _date.day)
        return _qdate

    def convert_qdate(self, _qdate):
        return dt.date(_qdate[0], _qdate[1], _qdate[2])

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)

    # @QtCore.pyqtSlot()
    # def toolButtonAjouter(self):
    # num = self.ui.tableWidget.rowCount()
    #     dd = QTableWidgetItem()
    #     ff = QTableWidgetItem()
    #     self.ui.tableWidget.insertRow(num)
    #     self.ui.tableWidget.setItem(num, 0, dd)
    #     self.ui.tableWidget.setItem(num, 1, ff)
    #
    # @QtCore.pyqtSlot()
    # def toolButtonSupprimer(self):
    #     itm = self.ui.tableWidget.currentItem()
    #     idx = self.ui.tableWidget.indexFromItem(itm)
    #     self.ui.tableWidget.removeRow(idx.row())

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = GisementScreen()
    # form = AddAsset()
    form.show()
    ap.exec_()