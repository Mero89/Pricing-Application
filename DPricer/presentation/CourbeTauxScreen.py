# coding=utf-8
__author__ = 'F.Marouane'

import sys
import datetime as dt

from PyQt4.QtGui import *
from PyQt4 import QtCore

from DPricer.presentation.PyuicFiles.CourbeTaux import Ui_CourbeTaux
from DPricer.data.AppModel import CourbeMd, AppModel
from DPricer.lib.Courbe import Courbe
from DPricer.lib.Controller import DateEval
import TableUtils as TU


class CourbeTaux(QWidget, Ui_CourbeTaux):
    def __init__(self, parent=None):
        super(Ui_CourbeTaux, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_CourbeTaux()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = 'Courbes de Taux'
        self.setWindowTitle(self.title)
        self.session = AppModel().get_session()
        self.data = list()  # data est une liste contenant les Objets [CourbeMd]
        self.date_eval = DateEval()
        self.ui.dateEditFilter.setDate(self.date_eval.get_qdate())
        self.ui.dateEditFilter.dateChanged.connect(self.filter_by_date)
        self.ui.maturiteLineEdit.editingFinished.connect(self.calcul_maturite)
        self.filter_by_date()
        headers = [u'transactions', u"date d'échéance", u"date valeur", u"taux pondéré", u"Maturité résiduelle"]
        TU.set_headers(self.ui.tableWidgetCourbe, headers)

    @QtCore.pyqtSlot()
    def filter_by_date(self):
        _date = convert_qdate(self.ui.dateEditFilter.date().getDate())
        self.data = self.session.query(CourbeMd).filter_by(date_req=_date).all()
        if self.data:
            self.ui.lineEditTransaction.setText(str(self.data[0].date_transaction.strftime('%d/%m/%Y')))
            self.populate_table()
        else:
            self.ui.tableWidgetCourbe.clearContents()
            self.ui.lineEditTransaction.clear()
            self.tell_status(u'Courbe non disponible')

    def populate_table(self):
        self.ui.tableWidgetCourbe.clearContents()
        keys = ['transactions', 'date_echeance', 'date_valeur', 'taux_pondere']
        if self.data:
            self.ui.tableWidgetCourbe.setRowCount(len(self.data))
            # populate table
            for el in self.data:
                row = self.data.index(el)
                mat_residuelle = QTableWidgetItem(str((el.date_echeance - el.date_valeur).days))
                self.ui.tableWidgetCourbe.setRowHeight(row, 30)
                TU.put_row(self.ui.tableWidgetCourbe, row, keys, el)
                self.ui.tableWidgetCourbe.setItem(row, len(keys), mat_residuelle)

    def tell_status(self, status):
        if self.parent:
            self.parent.ui.statusbar.showMessage(status, 3200)

    def calcul_maturite(self):
        cc = Courbe(convert_qdate(self.ui.dateEditFilter.date().getDate()))
        value = self.ui.maturiteLineEdit.text()
        if value:
            maturite = int(value)
            if self.ui.splineCheckBox.checkState():
                taux = cc.taux_spline(maturite)
            else:
                taux = cc.taux_lineaire(maturite)
            self.ui.tauxLineEdit.setText(str(round(taux * 100, 4))+ ' %')

    def add_ligne(self):

        pass

    def remove_ligne(self):
        pass

    def update_ligne(self):
        pass

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()


def convert_qdate(_qdate):
    return dt.date(_qdate[0], _qdate[1], _qdate[2])

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = CourbeTaux()
    form.show()
    ap.exec_()