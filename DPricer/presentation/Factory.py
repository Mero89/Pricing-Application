# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4 import QtGui
from PyQt4 import QtCore
import datetime
import sys
import math
from DPricer.data.AppModel import *


class RateSpinBox(QtGui.QDoubleSpinBox):
    def __init__(self, parent=None):
        QtGui.QDoubleSpinBox.__init__(self, parent)
        self.setSuffix(" %")
        self.setMinimum(0)
        self.setDecimals(2)

    def set_value(self, p_float):
        self.setValue(p_float*100)

    def get_value(self):
        return self.value()/100


class TextEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)

    def set_value(self, text):
        self.setText(unicode(text))

    def get_value(self):
        return unicode(self.text())


class DateEdit(QtGui.QDateEdit):
    def __init__(self, parent=None):
        QtGui.QDateEdit.__init__(self, parent)
        self.setDisplayFormat("dd/MM/yyyy")
        self.setCalendarPopup(True)

    def set_value(self, _date):
        self.setDate(self.date_to_qdate(_date))

    def get_value(self):
        return self.convert_qdate(self.date().getDate())

    def convert_qdate(self, _qdate):
        return datetime.date(_qdate[0], _qdate[1], _qdate[2])

    def date_to_qdate(self, _date):
        if isinstance(_date, datetime.date):
            _qdate = QtCore.QDate(_date.year, _date.month, _date.day)
        elif isinstance(_date, str) or isinstance(_date, QtCore.QString):
            d = str(_date).split('-')
            _qdate = QtCore.QDate(int(d[0]), int(d[1]), int(d[2]))
        return _qdate


class InputBox(QtGui.QWidget):
    _model_view = {'date_echeance': u"Date d'échéance",
                   'transactions': u'Transactions',
                   'date_req': u"Date d'évaluation",
                   'date_transaction': u"Date de transaction",
                   'date_valeur': u"Date de valeur",
                   'taux_pondere': u"Taux Pondéré",
                   'maturite': u"Date d'échéance",
                   'isin': u"ISIN",
                   'date_jouissance': u"Date de jouissance",
                   'nominal': u"Nominal",
                   'p_isin': u"ISIN Portefeuille",
                   'spread': u"Spread",
                   'date_emission': u"Date d'émission",
                   'taux_facial': u"Taux facial",
                   'type': u"Type",
                   'nom': u"Nom",
                   'prenom': u"Prénom",
                   'mail': u"@Mail",
                   'password': u"Mot de passe",
                   'uname': u"Nom d'utilisateur",
                   'echue': u"Echue",
                   'forcee': u"Forcée"
                   }

    _model_dict = {datetime.date: DateEdit,
                   unicode: TextEdit,
                   str: TextEdit,
                   bool: QtGui.QCheckBox,
                   int: QtGui.QSpinBox,
                   float: QtGui.QDoubleSpinBox}

    def __init__(self, model=None, parent=None, update=False):
        QtGui.QWidget.__init__(self, parent)
        self.vlayout = QtGui.QVBoxLayout(self)
        self.setLayout(self.vlayout)
        self.form_layout = QtGui.QFormLayout()
        self.hlayout = QtGui.QHBoxLayout()
        self.ok_button = QtGui.QPushButton("OK")
        self.no_button = QtGui.QPushButton("Annuler")
        self.sz_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.setSizePolicy(self.sz_policy)
        self.model = model
        
        self.build_model_form(update=update)
        self.set_ui()

    def build_model_form(self, update=False):
        """
        Build the form.
        :return:
        """
        fields = dict(self.model.__dict__)
        del fields['_sa_instance_state']
        if not update:
            for el in fields.keys():
                lbl = QtGui.QLabel(self._model_view[el])
                lbl.setObjectName(el)
                # Si texte
                if isinstance(fields[el], unicode) or isinstance(fields[el], str):
                    item = TextEdit()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
                # Si nombre
                elif isinstance(fields[el], float):
                    item = QtGui.QDoubleSpinBox()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
                # Si Date, datetime.date
                elif isinstance(fields[el], datetime.date):
                    item = DateEdit()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
                # Si Booléen
                elif isinstance(fields[el], bool):
                    item = QtGui.QCheckBox()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
                # Si Entier
                elif isinstance(fields[el], int):
                    item = QtGui.QSpinBox()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
        elif update:
            for el in fields.keys():
                if el in self._model_view:
                    lbl = QtGui.QLabel(self._model_view[el])
                    lbl.setObjectName(el)
                    # Si texte
                    if isinstance(fields[el], unicode) or isinstance(fields[el], str):
                        item = TextEdit()
                        item.setObjectName(el)
                        item.set_value(fields[el])
                        self.form_layout.addRow(lbl, item)
                    # Si nombre
                    elif isinstance(fields[el], float):
                        # Vérifie l'ordre de grandeur
                        if math.log(fields[el]) < -1:
                            item = RateSpinBox()
                            item.setObjectName(el)
                            item.set_value(fields[el])
                            self.form_layout.addRow(lbl, item)
                        else:
                            item = QtGui.QDoubleSpinBox()
                            item.setObjectName(el)
                            item.setMaximum(9999999)
                            item.setValue(fields[el])
                            self.form_layout.addRow(lbl, item)
                    # Si Date, datetime.date
                    elif isinstance(fields[el], datetime.date):
                        item = DateEdit()
                        item.setObjectName(el)
                        item.set_value(fields[el])
                        self.form_layout.addRow(lbl, item)
                    # Si Booléen
                    elif isinstance(fields[el], bool):
                        item = QtGui.QCheckBox()
                        item.setObjectName(el)
                        item.setChecked(fields[el])
                        self.form_layout.addRow(lbl, item)
                    # Si Entier
                    elif isinstance(fields[el], int):
                        item = QtGui.QSpinBox()
                        item.setObjectName(el)
                        item.setValue(fields[el])
                        item.setMaximum(9999999)
                        self.form_layout.addRow(lbl, item)

    def set_ui(self):
        """
        Configure la mise en page.
        :return:
        """
        self.hlayout.addWidget(self.ok_button)
        self.hlayout.addWidget(self.no_button)
        self.vlayout.addLayout(self.form_layout)
        self.vlayout.addLayout(self.hlayout)

    def get_input(self):
        inputs = dict()
        md = dict(self.model.__dict__)
        del md['_sa_instance_state']
        for key in md:
            obj = self.findChild(self._model_dict[type(md[key])], name=QtCore.QString(unicode(key)))
            if isinstance(md[key], datetime.date):
                inputs[key] = obj.get_value()
            elif isinstance(md[key], unicode) or isinstance(md[key], str):
                inputs[key] = obj.get_value()
            elif isinstance(md[key], bool):
                inputs[key] = obj.checkState()
        else:
            return inputs


class TableBox(QtGui.QTableWidget):
    def __init__(self, model, parent=None):
        QtGui.QTableWidget.__init__(self, parent=parent)
        self.model = model
        self.data = list()
        self.header = self.set_headers()
        self.customize_view()
        self.setup_actions()
        self.show()

    # def define_headers(self):
    #     self.setHorizontalHeaderLabels(self.set_headers())
    #     pass
    def customize_view(self):
        self.setSelectionBehavior(1)
        self.setSortingEnabled(True)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSortIndicatorShown(True)

    def put_model(self, model, row):
        col_pos = 0
        db_dico = dict(model.__dict__)
        self.insertRow(row)
        for el in self.header:
            if el in db_dico:
                item = QtGui.QTableWidgetItem(unicode(db_dico[el]))
                self.setItem(row, col_pos, item)
                col_pos += 1

    def set_headers(self):
        h_list = self.model.__mapper__.columns.keys()
        self.setColumnCount(len(h_list))
        header_list = QtCore.QStringList(h_list)
        self.setHorizontalHeaderLabels(header_list)
        return h_list

    def show_data(self, data):
        e = enumerate(data)
        self.data = list(e)
        for el in self.data:
            self.put_model(el[1], el[0])

    @QtCore.pyqtSlot()
    def get_selected_object(self):
        idx = self.currentRow()
        obj = self.data[idx][1]
        print obj.isin, obj.nom
        # return obj

    def setup_actions(self):
        self.itemSelectionChanged.connect(self.get_selected_object)


####### Utils Functions #######
def convert_qdate(_qdate):
    return datetime.date(_qdate[0], _qdate[1], _qdate[2])


def date_to_qdate(_date):
    if isinstance(_date, datetime.date):
        _qdate = QtCore.QDate(_date.year, _date.month, _date.day)
    elif isinstance(_date, str) or isinstance(_date, QtCore.QString):
        d = str(_date).split('-')
        _qdate = QtCore.QDate(int(d[0]), int(d[1]), int(d[2]))
    return _qdate

if __name__ == '__main__':
    ap = QtGui.QApplication(sys.argv)
    s = AppModel().get_session()
    u = s.query(ObligationMd).first()
    # e = list(enumerate(u))
    # print e
    i = InputBox(u, update=True)
    print i.get_input()
    i.show()
    # t = TableBox(ObligationMd)
    # t.show_data(u)
    ap.exec_()