# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/test/Portefeuilles.ui'
#
# Created: Sun Sep 28 18:13:15 2014
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

class Ui_Portefeuilles(object):
    def setupUi(self, Portefeuilles):
        Portefeuilles.setObjectName(_fromUtf8("Portefeuilles"))
        Portefeuilles.resize(722, 595)
        self.verticalLayout = QtGui.QVBoxLayout(Portefeuilles)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Portefeuilles)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(230, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(530, 16777215))
        self.groupBox.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetPortefeuille = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetPortefeuille.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetPortefeuille.sizePolicy().hasHeightForWidth())
        self.tableWidgetPortefeuille.setSizePolicy(sizePolicy)
        self.tableWidgetPortefeuille.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidgetPortefeuille.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidgetPortefeuille.setFont(font)
        self.tableWidgetPortefeuille.setMidLineWidth(0)
        self.tableWidgetPortefeuille.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.tableWidgetPortefeuille.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tableWidgetPortefeuille.setShowGrid(False)
        self.tableWidgetPortefeuille.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetPortefeuille.setRowCount(0)
        self.tableWidgetPortefeuille.setObjectName(_fromUtf8("tableWidgetPortefeuille"))
        self.tableWidgetPortefeuille.setColumnCount(5)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetPortefeuille.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetPortefeuille.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetPortefeuille.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetPortefeuille.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetPortefeuille.setHorizontalHeaderItem(4, item)
        self.tableWidgetPortefeuille.horizontalHeader().setVisible(True)
        self.tableWidgetPortefeuille.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetPortefeuille.verticalHeader().setVisible(False)
        self.tableWidgetPortefeuille.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetPortefeuille.verticalHeader().setSortIndicatorShown(True)
        self.tableWidgetPortefeuille.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidgetPortefeuille)
        self.horizontalLayout.addWidget(self.groupBox)
        self.line = QtGui.QFrame(Portefeuilles)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.groupBox_2 = QtGui.QGroupBox(Portefeuilles)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(230, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox_2.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidgetActifs = QtGui.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidgetActifs.setFont(font)
        self.tableWidgetActifs.setMidLineWidth(0)
        self.tableWidgetActifs.setDragDropOverwriteMode(False)
        self.tableWidgetActifs.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidgetActifs.setAlternatingRowColors(True)
        self.tableWidgetActifs.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetActifs.setShowGrid(False)
        self.tableWidgetActifs.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetActifs.setRowCount(0)
        self.tableWidgetActifs.setObjectName(_fromUtf8("tableWidgetActifs"))
        self.tableWidgetActifs.setColumnCount(7)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetActifs.setHorizontalHeaderItem(6, item)
        self.tableWidgetActifs.horizontalHeader().setVisible(True)
        self.tableWidgetActifs.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetActifs.verticalHeader().setVisible(False)
        self.tableWidgetActifs.verticalHeader().setSortIndicatorShown(True)
        self.tableWidgetActifs.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidgetActifs)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(Portefeuilles)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButtonFermer = QtGui.QPushButton(Portefeuilles)
        self.pushButtonFermer.setObjectName(_fromUtf8("pushButtonFermer"))
        self.horizontalLayout_2.addWidget(self.pushButtonFermer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Portefeuilles)
        QtCore.QMetaObject.connectSlotsByName(Portefeuilles)

    def retranslateUi(self, Portefeuilles):
        Portefeuilles.setWindowTitle(_translate("Portefeuilles", "Mes Portefeuiles", None))
        self.groupBox.setTitle(_translate("Portefeuilles", "Mes portefeuilles", None))
        item = self.tableWidgetPortefeuille.horizontalHeaderItem(0)
        item.setText(_translate("Portefeuilles", "ISIN", None))
        item = self.tableWidgetPortefeuille.horizontalHeaderItem(1)
        item.setText(_translate("Portefeuilles", "Nom", None))
        item = self.tableWidgetPortefeuille.horizontalHeaderItem(2)
        item.setText(_translate("Portefeuilles", "Prix", None))
        item = self.tableWidgetPortefeuille.horizontalHeaderItem(3)
        item.setText(_translate("Portefeuilles", "Sensibilité", None))
        item = self.tableWidgetPortefeuille.horizontalHeaderItem(4)
        item.setText(_translate("Portefeuilles", "Duration", None))
        self.groupBox_2.setTitle(_translate("Portefeuilles", "Structure Portefeuille", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(0)
        item.setText(_translate("Portefeuilles", "ISIN", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(1)
        item.setText(_translate("Portefeuilles", "Nom", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(2)
        item.setText(_translate("Portefeuilles", "Quantite", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(3)
        item.setText(_translate("Portefeuilles", "Poids", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(4)
        item.setText(_translate("Portefeuilles", "Prix", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(5)
        item.setText(_translate("Portefeuilles", "Sensibilité", None))
        item = self.tableWidgetActifs.horizontalHeaderItem(6)
        item.setText(_translate("Portefeuilles", "Duration", None))
        self.pushButton.setText(_translate("Portefeuilles", "PushButton", None))
        self.pushButtonFermer.setText(_translate("Portefeuilles", "Fermer", None))

