# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/ImporterCourbeTaux.ui'
#
# Created: Thu Aug 28 10:09:47 2014
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

class Ui_ImportForm(object):
    def setupUi(self, ImportForm):
        ImportForm.setObjectName(_fromUtf8("ImportForm"))
        ImportForm.resize(389, 213)
        self.verticalLayout = QtGui.QVBoxLayout(ImportForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ImportForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_courbe = QtGui.QWidget()
        self.tab_courbe.setObjectName(_fromUtf8("tab_courbe"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_courbe)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.DateLabelTaux = QtGui.QLabel(self.tab_courbe)
        self.DateLabelTaux.setObjectName(_fromUtf8("DateLabelTaux"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.DateLabelTaux)
        self.DateEditTaux = QtGui.QDateEdit(self.tab_courbe)
        self.DateEditTaux.setObjectName(_fromUtf8("DateEditTaux"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.DateEditTaux)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCourbe = QtGui.QPushButton(self.tab_courbe)
        self.pushButtonCourbe.setObjectName(_fromUtf8("pushButtonCourbe"))
        self.horizontalLayout.addWidget(self.pushButtonCourbe)
        self.pushButtonQuitter = QtGui.QPushButton(self.tab_courbe)
        self.pushButtonQuitter.setObjectName(_fromUtf8("pushButtonQuitter"))
        self.horizontalLayout.addWidget(self.pushButtonQuitter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_courbe, _fromUtf8(""))
        self.tab_courbe_multi = QtGui.QWidget()
        self.tab_courbe_multi.setObjectName(_fromUtf8("tab_courbe_multi"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_courbe_multi)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.LabelDateFin = QtGui.QLabel(self.tab_courbe_multi)
        self.LabelDateFin.setObjectName(_fromUtf8("LabelDateFin"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.LabelDateFin)
        self.DateEditDateFin = QtGui.QDateEdit(self.tab_courbe_multi)
        self.DateEditDateFin.setObjectName(_fromUtf8("DateEditDateFin"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.DateEditDateFin)
        self.DateEditDateDebut = QtGui.QDateEdit(self.tab_courbe_multi)
        self.DateEditDateDebut.setObjectName(_fromUtf8("DateEditDateDebut"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.DateEditDateDebut)
        self.LabelDateDebut = QtGui.QLabel(self.tab_courbe_multi)
        self.LabelDateDebut.setObjectName(_fromUtf8("LabelDateDebut"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.LabelDateDebut)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButtonCourbeMulti = QtGui.QPushButton(self.tab_courbe_multi)
        self.pushButtonCourbeMulti.setObjectName(_fromUtf8("pushButtonCourbeMulti"))
        self.horizontalLayout_2.addWidget(self.pushButtonCourbeMulti)
        self.pushButton_4 = QtGui.QPushButton(self.tab_courbe_multi)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_courbe_multi, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(ImportForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), ImportForm.close)
        QtCore.QObject.connect(self.pushButtonQuitter, QtCore.SIGNAL(_fromUtf8("clicked()")), ImportForm.close)
        QtCore.QMetaObject.connectSlotsByName(ImportForm)
        ImportForm.setTabOrder(self.DateEditTaux, self.pushButtonCourbe)
        ImportForm.setTabOrder(self.pushButtonCourbe, self.pushButtonQuitter)
        ImportForm.setTabOrder(self.pushButtonQuitter, self.DateEditDateDebut)
        ImportForm.setTabOrder(self.DateEditDateDebut, self.DateEditDateFin)
        ImportForm.setTabOrder(self.DateEditDateFin, self.pushButtonCourbeMulti)
        ImportForm.setTabOrder(self.pushButtonCourbeMulti, self.pushButton_4)
        ImportForm.setTabOrder(self.pushButton_4, self.tabWidget)

    def retranslateUi(self, ImportForm):
        ImportForm.setWindowTitle(_translate("ImportForm", "Importer coube taux (BAM)", None))
        self.DateLabelTaux.setText(_translate("ImportForm", "Selectionner date", None))
        self.pushButtonCourbe.setText(_translate("ImportForm", "Charger La courbe", None))
        self.pushButtonQuitter.setText(_translate("ImportForm", "Quitter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_courbe), _translate("ImportForm", "Importer une courbe", None))
        self.LabelDateFin.setText(_translate("ImportForm", "A", None))
        self.LabelDateDebut.setText(_translate("ImportForm", "Date Debut", None))
        self.pushButtonCourbeMulti.setText(_translate("ImportForm", "Charger Les courbes", None))
        self.pushButton_4.setText(_translate("ImportForm", "Quitter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_courbe_multi), _translate("ImportForm", "Importer plusieurs courbes", None))

