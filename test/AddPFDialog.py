# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/test/AddPFDialog.ui'
#
# Created: Fri Sep 26 16:44:08 2014
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

class Ui_AddPFDialog(object):
    def setupUi(self, AddPFDialog):
        AddPFDialog.setObjectName(_fromUtf8("AddPFDialog"))
        AddPFDialog.resize(455, 287)
        self.verticalLayout_3 = QtGui.QVBoxLayout(AddPFDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(AddPFDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButtonAjouter_2 = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAjouter_2.sizePolicy().hasHeightForWidth())
        self.pushButtonAjouter_2.setSizePolicy(sizePolicy)
        self.pushButtonAjouter_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pushButtonAjouter_2.setObjectName(_fromUtf8("pushButtonAjouter_2"))
        self.verticalLayout_2.addWidget(self.pushButtonAjouter_2)
        self.pushButtonSupprimer_2 = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSupprimer_2.sizePolicy().hasHeightForWidth())
        self.pushButtonSupprimer_2.setSizePolicy(sizePolicy)
        self.pushButtonSupprimer_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pushButtonSupprimer_2.setObjectName(_fromUtf8("pushButtonSupprimer_2"))
        self.verticalLayout_2.addWidget(self.pushButtonSupprimer_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddPFDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(AddPFDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddPFDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddPFDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPFDialog)

    def retranslateUi(self, AddPFDialog):
        AddPFDialog.setWindowTitle(_translate("AddPFDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("AddPFDialog", "Fournir les Informations nécessaires", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddPFDialog", "ISIN Portefeuille", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddPFDialog", "Nom Portefeuille", None))
        self.pushButtonAjouter_2.setText(_translate("AddPFDialog", "Ajouter", None))
        self.pushButtonSupprimer_2.setText(_translate("AddPFDialog", "Supprimer", None))

