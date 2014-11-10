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
                lbl = QtGui.QLabel(el)
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
                lbl = QtGui.QLabel(el)
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
        # obj = self.findChild(RateSpinBox, name=QtCore.QString(unicode("taux_facial")))
        # inputs["taux_facial"] = obj.get_value()
        # return inputs


####### Utils Functions #####
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
    u = s.query(ObligationMd).filter_by(isin="100503").first()
    i = InputBox(u, update=True)
    print i.get_input()
    i.show()
    ap.exec_()