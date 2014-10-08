# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/DPricer/presentation/Designer-Files/PortefeuilleInput.ui'
#
# Created: Wed Oct  8 21:14:22 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PortefeuilleInput(object):
    def setupUi(self, PortefeuilleInput):
        PortefeuilleInput.setObjectName(_fromUtf8("PortefeuilleInput"))
        PortefeuilleInput.setWindowModality(QtCore.Qt.WindowModal)
        PortefeuilleInput.resize(310, 170)
        PortefeuilleInput.setSizeGripEnabled(False)
        PortefeuilleInput.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(PortefeuilleInput)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setContentsMargins(-1, 30, -1, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.isinLabel = QtGui.QLabel(PortefeuilleInput)
        self.isinLabel.setObjectName(_fromUtf8("isinLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.isinLabel)
        self.isinLineEdit = QtGui.QLineEdit(PortefeuilleInput)
        self.isinLineEdit.setObjectName(_fromUtf8("isinLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.isinLineEdit)
        self.nomDuPortefeuilleLabel = QtGui.QLabel(PortefeuilleInput)
        self.nomDuPortefeuilleLabel.setObjectName(_fromUtf8("nomDuPortefeuilleLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.nomDuPortefeuilleLabel)
        self.nomDuPortefeuilleLineEdit = QtGui.QLineEdit(PortefeuilleInput)
        self.nomDuPortefeuilleLineEdit.setObjectName(_fromUtf8("nomDuPortefeuilleLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.nomDuPortefeuilleLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(PortefeuilleInput)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.isinLabel.setBuddy(self.isinLineEdit)
        self.nomDuPortefeuilleLabel.setBuddy(self.nomDuPortefeuilleLineEdit)

        self.retranslateUi(PortefeuilleInput)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PortefeuilleInput.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PortefeuilleInput.reject)
        QtCore.QMetaObject.connectSlotsByName(PortefeuilleInput)

    def retranslateUi(self, PortefeuilleInput):
        PortefeuilleInput.setWindowTitle(_translate("PortefeuilleInput", "Modifier infos portefeuille", None))
        self.isinLabel.setText(_translate("PortefeuilleInput", "&Isin portefeuille", None))
        self.nomDuPortefeuilleLabel.setText(_translate("PortefeuilleInput", "&Nom du portefeuille", None))

