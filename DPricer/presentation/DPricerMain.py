# coding=utf-8
import os

__author__ = 'F.Marouane'

### App Library modules
from DPricer.lib.User import User
from DPricer.data import Excel
from DPricer.lib.YieldManager import YieldManager
from DPricer.lib.Controller import DateEval
### Library modules
import sys
import datetime as dt
from PyQt4.QtGui import *
from PyQt4 import QtCore
### Import App Screens and Dialogs ###
from DPricer.presentation.PyuicFiles.MDI import Ui_MDIApp
from GisementScreen import GisementScreen, AddAsset, UpdateAsset
from LoginDialog import LoginDialog
from MonPortefeuille import Portefeuilles, GererPortefeuille, StructurePortefeuilles
from CourbeTauxScreen import CourbeTaux
from ParametresScreen import Parametre
from outils import Calculette


class MyClass(QMainWindow, Ui_MDIApp):
    def __init__(self):
        super(Ui_MDIApp, self).__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MDIApp()
        self.ui.setupUi(self)
        # log = LoginDialog()
        # log.accepted.connect(self.stats)
        # log.exec_()
        self.user = User('Mero', 'mero')
        self.user.check()
        # self.user = log.user
        nom = 'FAKIR'
        prenom = 'Marouane'
        self.ui.labelUser.setText(nom + ' ' + prenom)
        self.date_eval = DateEval()
        qday = QtCore.QDate().currentDate()
        self.ui.dateEvalEdit.setDate(self.date_eval.last_valid_date(self.date_eval.default))
        self.ui.labelDates.setText(qday.toString())
        self.current_day = self.date_eval.default
        self.connect_actions()
        self.showMaximized()

    def connect_actions(self):
        self.ui.actionMonPortefeuille.triggered.connect(self.open_portefeuille_screen)
        self.ui.actionVisualiser.triggered.connect(self.open_courbe_screen)
        self.ui.actionGisement.triggered.connect(self.open_gisement_screen)
        self.ui.actionAjoutObligation.triggered.connect(self.open_add_asset_screen)
        self.ui.actionOnglets.triggered.connect(self.set_tabview_mode)
        self.ui.actionSousFenetres.triggered.connect(self.set_windowview_mode)
        self.ui.actionExcelCourbe.triggered.connect(self.import_courbe_taux)
        self.ui.actionImporterActifExcel.triggered.connect(self.import_obligations)
        self.ui.actionGeneral.triggered.connect(self.open_parametres)
        self.ui.actionCalculette.triggered.connect(self.open_tools)
        self.ui.actionGererPortefeuille.triggered.connect(self.open_gerer_portefeuille)
        self.ui.actionModifierMesPortefeuilles.triggered.connect(self.open_structure_portefeuille)
        self.ui.actionPlein_cran.triggered.connect(self.toggle_fullscreen)
        self.ui.dateEvalEdit.dateChanged.connect(self.change_date_eval)

    @QtCore.pyqtSlot()
    def change_date_eval(self):
        new_date = self.convert_qdate(self.ui.dateEvalEdit.date().getDate())
        self.date_eval.change_date(new_date)
        self.ui.dateEvalEdit.setDate(self.date_eval.get_qdate())

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
            self.ui.actionPlein_cran.setText(u'Plein écran')
        else:
            self.showFullScreen()
            self.ui.actionPlein_cran.setText(u'Quitter Plein écran')

    def load_screen(self, screen):
        ct = screen(parent=self)
        if ct.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(ct)
            ct.show()
        else:
            del ct

    # Ouvre la calculette
    def open_tools(self):
        self.load_screen(Calculette)

    # Ouvre l'écran de structuration de portefeuille
    def open_structure_portefeuille(self):
        self.load_screen(StructurePortefeuilles)

    # Met à jour la courbe de taux
    def update_courbe(self):
        YM = YieldManager()
        YM.import_auto()

    # Ouvre l'écran des paramètres
    def open_parametres(self):
        self.load_screen(Parametre)

    # Ouvre l'écran d'ajout d'un actif
    @QtCore.pyqtSlot()
    def open_add_asset_screen(self):
        self.load_screen(AddAsset)

    # Ouvre l'écran d'édition des actifs
    @QtCore.pyqtSlot(dict)
    def update_asset_screen(self, data):
        ct = UpdateAsset(data=data, parent=self)
        if ct.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(ct)
            ct.show()
        else:
            del ct

    # Ouvre l'écran des actifs
    @QtCore.pyqtSlot()
    def open_gisement_screen(self):
        self.load_screen(GisementScreen)

    # Ouvre l'écran de la courbe de taux
    @QtCore.pyqtSlot()
    def open_courbe_screen(self):
        self.load_screen(CourbeTaux)

    # Ouvre le dialogue du portefeuille
    @QtCore.pyqtSlot()
    def open_gerer_portefeuille(self):
        self.load_screen(GererPortefeuille)

    # Ouvre l'écran du portefeuille
    @QtCore.pyqtSlot()
    def open_portefeuille_screen(self):
        pf = Portefeuilles(parent=self)
        if pf.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(pf)
            pf.user = self.user
            pf.show()
            pf.affiche_portefeuille()
        else:
            del pf

    def title_list(self):
        """
        retourne la liste des titres des sous-fenêtres
        :return:
        """
        l = [unicode(el.windowTitle()) for el in self.ui.mdiArea.subWindowList()]
        return l

    def set_windowview_mode(self):
        self.ui.mdiArea.setViewMode(0)

    def set_tabview_mode(self):
        self.ui.mdiArea.setViewMode(1)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.close_current_window()
            # Comment to commit

    def import_courbe_taux(self):
        filename = self.open_excel()
        # importe Le fichier dans la BDD
        if str(filename):
            rep = Excel.commit_courbe_bam(filename)
            if rep == 1:
                message = u"La courbe a été importée avec succès."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == 0:
                message = u"La courbe existe déjà."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == -1:
                message = u"Le fichier ne contient pas les données au format attendu."
                self.ui.statusbar.showMessage(message, 4000)

    def import_obligations(self):
        filename = self.open_excel()
        if str(filename):
            Excel.import_obligation(filename)
            message = u"Le fichier a été importé avec succès."
            self.ui.statusbar.showMessage(message, 4000)
            # if rep == 1:
            # elif rep == 0:
            #     message = u"Certains champs sont manquants."
            #     self.ui.statusbar.showMessage(message, 4000)
            # elif rep == -1:
            #     message = u"Le fichier contient des données incompatibles ou des lignes déjà existantes."
            #     self.ui.statusbar.showMessage(message, 4000)

    def export_excel(self):
        rws = GisementScreen().ui.tableWidgetActifs.rowCount()
        cls = GisementScreen().ui.tableWidgetActifs.columnCount()
        headers = GisementScreen().ui.tableWidgetActifs.horizontalHeader()
        data = list()
        myrow = list()
        for row in range(rws):
            for col in range(cls):
                myrow.append(GisementScreen().ui.tableWidgetActifs.item(row, col).text())
            data.append(myrow)
        Excel.export_to_excel(headers, data, "/Users/mar/Desktop", "Export.xls")

    def open_excel(self):
        # lancer le FileDialog
        fDialog = QFileDialog(parent=self)
        fDialog.setFileMode(3)
        filename = fDialog.getOpenFileName(self, "Importer courbe Taux", filter="Fichiers (*.xls *.xlsx)")
        return filename

    def close_current_window(self):
        self.ui.mdiArea.closeActiveSubWindow()

    def convert_qdate(self, _qdate):
        return dt.date(_qdate[0], _qdate[1], _qdate[2])

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MyClass()
    form.show()
    ap.exec_()
