# coding=utf-8
__author__ = 'F.Marouane'

import sys
import datetime as dt

from PyQt4.QtGui import *
from PyQt4 import QtCore

from DPricer.presentation.PyuicFiles.CourbeTaux import Ui_CourbeTaux
from DPricer.data.AppModel import CourbeMd, AppModel
import TableUtils as TU


class CourbeTaux(QDialog, Ui_CourbeTaux):
    def __init__(self, parent=None):
        super(Ui_CourbeTaux, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_CourbeTaux()
        self.ui.setupUi(self)
        self.parent = parent
        self.title = 'Courbes de Taux'
        self.setWindowTitle(self.title)
        self.session = AppModel().get_session()
        self.data = list()  # data est une liste contenant les Objets [CourbeMd]
        self.ui.dateEditFilter.setDate(QtCore.QDate(2014, 9, 22))
        self.ui.dateEditFilter.dateChanged.connect(self.filter_by_date)
        self.filter_by_date()
        headers = [u'transactions', u"date d'écheance", u"date valeur", u"taux pondéré", u"Maturités résiduelles"]
        TU.set_headers(self.ui.tableWidgetCourbe, headers)

    @QtCore.pyqtSlot()
    def filter_by_date(self):
        _date = self.convert_qdate(self.ui.dateEditFilter.date().getDate())
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

    def convert_qdate(self, _qdate):
        return dt.date(_qdate[0], _qdate[1], _qdate[2])

    def tell_status(self, status):
        self.parent.ui.statusbar.showMessage(status, 3200)

    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = CourbeTaux()
    form.show()
    ap.exec_()