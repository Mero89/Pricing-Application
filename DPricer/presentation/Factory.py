# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4 import QtGui
from PyQt4 import QtCore
import datetime
import sys
import math
from DPricer.data.AppModel import *
from sqlalchemy import *
import sqlalchemy


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


class NumericEdit(QtGui.QDoubleSpinBox):
    def __init__(self, parent=None):
        QtGui.QDoubleSpinBox.__init__(self, parent)
        self.setMinimum(-9999999999)
        self.setMaximum(9999999999)
        self.setDecimals(2)
        self.setButtonSymbols(2)

    def get_value(self):
        return self.value()

    def set_value(self, value):
        self.setValue(value)


class TextEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)

    def set_value(self, text):
        self.setText(unicode(text))

    def get_value(self):
        return unicode(self.text())


class DateEdit(QtGui.QDateEdit):
    def __init__(self, parent=None, popup=True):
        QtGui.QDateEdit.__init__(self, parent)
        self.setDisplayFormat("dd/MM/yyyy")
        self.setCalendarPopup(popup)

    def set_value(self, _date):
        self.setDate(self.date_to_qdate(_date))

    def get_value(self):
        return self.convert_qdate(self.date().getDate())

    @staticmethod
    def convert_qdate(_qdate):
        return datetime.date(_qdate[0], _qdate[1], _qdate[2])

    @staticmethod
    def date_to_qdate(_date):
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
                   'forcee': u"Forcée",
                   'date_coupon': u"Date du coupon",
                   'amortissement': u"Amortissement",
                   'coupon': u"Coupon",
                   'date_observation': u"Date d'observation",
                   'valeur': u"Valeur"
                   }

    _model_dict = {datetime.date: DateEdit,
                   unicode: TextEdit,
                   str: TextEdit,
                   bool: QtGui.QCheckBox,
                   int: QtGui.QSpinBox,
                   float: NumericEdit}

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
        if isinstance(model, dict):
            self.md = self.model
        else:
            self.md = dict(self.model.__dict__)
            del self.md['_sa_instance_state']
        self.build_model_form(update=update)
        self.set_ui()
        self.set_actions()

    def build_model_form(self, update=False):
        """
        Build the form.
        :return:
        """
        if not update:
            self.input_table()
        elif update:
            self.update_form()

    def input_table(self):
        table = self.model.__table__
        for col in table.columns:
            if col.name in self._model_view:
                lbl = QtGui.QLabel(self._model_view[col.name])
                lbl.setObjectName(col.name)
                # Si texte
                if isinstance(col.type, sqlalchemy.sql.sqltypes.String):
                    item = TextEdit()
                    item.setObjectName(col.name)
                    self.form_layout.addRow(lbl, item)
                # Si nombre
                elif isinstance(col.type, sqlalchemy.sql.sqltypes.Float):
                    item = NumericEdit()
                    item.setObjectName(col.name)
                    self.form_layout.addRow(lbl, item)
                # Si Date, datetime.date
                elif isinstance(col.type, sqlalchemy.sql.sqltypes.Date):
                    item = DateEdit()
                    item.setObjectName(col.name)
                    self.form_layout.addRow(lbl, item)
                # Si Booléen
                elif isinstance(col.type, sqlalchemy.sql.sqltypes.Boolean):
                    item = QtGui.QCheckBox()
                    item.setObjectName(col.name)
                    self.form_layout.addRow(lbl, item)
                # Si Entier
                elif isinstance(col.type, sqlalchemy.sql.sqltypes.Integer):
                    item = QtGui.QSpinBox()
                    item.setObjectName(col.name)
                    item.setButtonSymbols(2)
                    self.form_layout.addRow(lbl, item)

    def input_form(self):
        """
        Create an empty form for new entities.
        :return:
        """
        fields = self.md
        for el in fields.keys():
            if el in self._model_view:
                lbl = QtGui.QLabel(self._model_view[el])
                lbl.setObjectName(el)
                # Si texte
                if isinstance(fields[el], unicode) or isinstance(fields[el], str):
                    item = TextEdit()
                    item.setObjectName(el)
                    self.form_layout.addRow(lbl, item)
                # Si nombre
                elif isinstance(fields[el], float):
                    item = NumericEdit()
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
                    item.setButtonSymbols(2)
                    self.form_layout.addRow(lbl, item)

    def update_form(self):
        """
        Create a form for updating the provided model values.
        :return:
        """
        fields = self.md
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
                    item = NumericEdit()
                    item.setObjectName(el)
                    item.set_value(fields[el])
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
                    item.setMaximum(9999999999)
                    item.setButtonSymbols(2)
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

    def set_actions(self):
        self.ok_button.clicked.connect(self.get_input)
        self.no_button.clicked.connect(self.close)

    def get_input(self):
        # todo: return inputs of all instances type
        inputs = dict()
        md = self.md
        for key in md:
            if md[key] is not None:
                obj = self.findChild(self._model_dict[type(md[key])], name=QtCore.QString(unicode(key)))
                if isinstance(md[key], datetime.date):
                    inputs[key] = obj.get_value()
                elif isinstance(md[key], unicode) or isinstance(md[key], str):
                    inputs[key] = obj.get_value()
                elif isinstance(md[key], float):
                    inputs[key] = obj.get_value()
                elif isinstance(md[key], bool):
                    inputs[key] = obj.checkState()
        else:
            # print inputs
            print inputs
            self.insert_model(inputs)
            self.close()

    def insert_model(self, dico):
        """
        Insert a new row of the given model with the provided dict()
        :param dico: dict
        :return:
        """
        s = AppModel().get_session()
        if u'id' in dico.keys():
            del dico['id']
        new = self.model.__class__.__call__(**dico)
        print new
        print new.__dict__
        try:
            s.add(new)
            s.commit()
        except Exception as e:
            print e.message

    def update_model(self, dico):
        """
        Update the model with the provided dict()
        :param dico: dict
        :return:
        """
        s = AppModel().get_session()
        md = self.md
        try:
            s.query(self.model.__class__).filter_by(**md).update(dico)
            s.commit()
        except Exception as e:
            print e.message


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
    # s = AppModel().get_session()
    # u = s.query(EcheancierMd).first()
    # e = list(enumerate(u))
    # print e
    # a = dict(coupon=55,isin='azerty')
    i = InputBox(ObligationMd(), update=False)
    i.show()
    # t = TableBox(ObligationMd)
    # t.show_data(u)
    ap.exec_()