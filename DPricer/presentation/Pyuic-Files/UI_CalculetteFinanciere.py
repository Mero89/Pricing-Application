# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/CalculetteFinanciere.ui'
#
# Created: Wed Aug 27 14:11:30 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 450)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_functions = QtGui.QWidget()
        self.tab_functions.setObjectName(_fromUtf8("tab_functions"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_functions)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_functions)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.LabelAnnuite = QtGui.QLabel(self.groupBox)
        self.LabelAnnuite.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelAnnuite.setObjectName(_fromUtf8("LabelAnnuite"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.LabelAnnuite)
        self.LineEditAnnuite = QtGui.QLineEdit(self.groupBox)
        self.LineEditAnnuite.setMaximumSize(QtCore.QSize(85, 16777215))
        self.LineEditAnnuite.setObjectName(_fromUtf8("LineEditAnnuite"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.LineEditAnnuite)
        self.LabelTauxActualisation = QtGui.QLabel(self.groupBox)
        self.LabelTauxActualisation.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelTauxActualisation.setObjectName(_fromUtf8("LabelTauxActualisation"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.LabelTauxActualisation)
        self.LineEditTauxActualisation = QtGui.QLineEdit(self.groupBox)
        self.LineEditTauxActualisation.setMaximumSize(QtCore.QSize(85, 16777215))
        self.LineEditTauxActualisation.setToolTip(_fromUtf8(""))
        self.LineEditTauxActualisation.setWhatsThis(_fromUtf8(""))
        self.LineEditTauxActualisation.setObjectName(_fromUtf8("LineEditTauxActualisation"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.LineEditTauxActualisation)
        self.LabelDateActualisation = QtGui.QLabel(self.groupBox)
        self.LabelDateActualisation.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelDateActualisation.setObjectName(_fromUtf8("LabelDateActualisation"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.LabelDateActualisation)
        self.DateEditDateActualisation = QtGui.QDateEdit(self.groupBox)
        self.DateEditDateActualisation.setDate(QtCore.QDate(2014, 1, 1))
        self.DateEditDateActualisation.setObjectName(_fromUtf8("DateEditDateActualisation"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.DateEditDateActualisation)
        self.LabelDateAnnuite = QtGui.QLabel(self.groupBox)
        self.LabelDateAnnuite.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelDateAnnuite.setObjectName(_fromUtf8("LabelDateAnnuite"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.LabelDateAnnuite)
        self.DateEditDateAnnuite = QtGui.QDateEdit(self.groupBox)
        self.DateEditDateAnnuite.setDate(QtCore.QDate(2014, 1, 1))
        self.DateEditDateAnnuite.setObjectName(_fromUtf8("DateEditDateAnnuite"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.DateEditDateAnnuite)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonVanEval = QtGui.QPushButton(self.groupBox)
        self.pushButtonVanEval.setObjectName(_fromUtf8("pushButtonVanEval"))
        self.horizontalLayout_2.addWidget(self.pushButtonVanEval)
        self.lineEditVanEval = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditVanEval.setFont(font)
        self.lineEditVanEval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditVanEval.setReadOnly(True)
        self.lineEditVanEval.setObjectName(_fromUtf8("lineEditVanEval"))
        self.horizontalLayout_2.addWidget(self.lineEditVanEval)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_functions, _fromUtf8(""))
        self.tab_obligation = QtGui.QWidget()
        self.tab_obligation.setObjectName(_fromUtf8("tab_obligation"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_obligation)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.nominalLabel = QtGui.QLabel(self.tab_obligation)
        self.nominalLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.nominalLabel.setObjectName(_fromUtf8("nominalLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.nominalLabel)
        self.nominalLineEdit = QtGui.QLineEdit(self.tab_obligation)
        self.nominalLineEdit.setMinimumSize(QtCore.QSize(102, 0))
        self.nominalLineEdit.setMaximumSize(QtCore.QSize(102, 16777215))
        self.nominalLineEdit.setObjectName(_fromUtf8("nominalLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.nominalLineEdit)
        self.tauxFacialLabel = QtGui.QLabel(self.tab_obligation)
        self.tauxFacialLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.tauxFacialLabel.setObjectName(_fromUtf8("tauxFacialLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.tauxFacialLabel)
        self.doubleSpinBoxTauxFacial = QtGui.QDoubleSpinBox(self.tab_obligation)
        self.doubleSpinBoxTauxFacial.setMinimumSize(QtCore.QSize(102, 0))
        self.doubleSpinBoxTauxFacial.setObjectName(_fromUtf8("doubleSpinBoxTauxFacial"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTauxFacial)
        self.LabelTauxActuariel = QtGui.QLabel(self.tab_obligation)
        self.LabelTauxActuariel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelTauxActuariel.setObjectName(_fromUtf8("LabelTauxActuariel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.LabelTauxActuariel)
        self.doubleSpinBoxTauxActuariel = QtGui.QDoubleSpinBox(self.tab_obligation)
        self.doubleSpinBoxTauxActuariel.setMinimumSize(QtCore.QSize(102, 0))
        self.doubleSpinBoxTauxActuariel.setObjectName(_fromUtf8("doubleSpinBoxTauxActuariel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTauxActuariel)
        self.dateEmissionLabel = QtGui.QLabel(self.tab_obligation)
        self.dateEmissionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateEmissionLabel.setObjectName(_fromUtf8("dateEmissionLabel"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.dateEmissionLabel)
        self.dateEditDateEmission = QtGui.QDateEdit(self.tab_obligation)
        self.dateEditDateEmission.setObjectName(_fromUtf8("dateEditDateEmission"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEditDateEmission)
        self.dateDeJouissanceLabel = QtGui.QLabel(self.tab_obligation)
        self.dateDeJouissanceLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateDeJouissanceLabel.setObjectName(_fromUtf8("dateDeJouissanceLabel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.dateDeJouissanceLabel)
        self.dateEditDateJouissance = QtGui.QDateEdit(self.tab_obligation)
        self.dateEditDateJouissance.setObjectName(_fromUtf8("dateEditDateJouissance"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.dateEditDateJouissance)
        self.dateDChAnceLabel = QtGui.QLabel(self.tab_obligation)
        self.dateDChAnceLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateDChAnceLabel.setObjectName(_fromUtf8("dateDChAnceLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.dateDChAnceLabel)
        self.dateEditDateEcheance = QtGui.QDateEdit(self.tab_obligation)
        self.dateEditDateEcheance.setObjectName(_fromUtf8("dateEditDateEcheance"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.dateEditDateEcheance)
        self.LabelDateEvaluation = QtGui.QLabel(self.tab_obligation)
        self.LabelDateEvaluation.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.LabelDateEvaluation.setObjectName(_fromUtf8("LabelDateEvaluation"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.LabelDateEvaluation)
        self.dateEditDateEvaluation = QtGui.QDateEdit(self.tab_obligation)
        self.dateEditDateEvaluation.setEnabled(True)
        self.dateEditDateEvaluation.setMinimumDate(QtCore.QDate(1799, 9, 14))
        self.dateEditDateEvaluation.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEditDateEvaluation.setCalendarPopup(False)
        self.dateEditDateEvaluation.setObjectName(_fromUtf8("dateEditDateEvaluation"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.dateEditDateEvaluation)
        self.comboBoxFrequenceCoupon = QtGui.QComboBox(self.tab_obligation)
        self.comboBoxFrequenceCoupon.setMinimumSize(QtCore.QSize(102, 0))
        self.comboBoxFrequenceCoupon.setMaximumSize(QtCore.QSize(102, 16777215))
        self.comboBoxFrequenceCoupon.setMaxVisibleItems(6)
        self.comboBoxFrequenceCoupon.setModelColumn(0)
        self.comboBoxFrequenceCoupon.setObjectName(_fromUtf8("comboBoxFrequenceCoupon"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.comboBoxFrequenceCoupon)
        self.pushButtonObligEval = QtGui.QPushButton(self.tab_obligation)
        self.pushButtonObligEval.setObjectName(_fromUtf8("pushButtonObligEval"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.pushButtonObligEval)
        self.evaluerLineEdit = QtGui.QLineEdit(self.tab_obligation)
        self.evaluerLineEdit.setMinimumSize(QtCore.QSize(102, 0))
        self.evaluerLineEdit.setMaximumSize(QtCore.QSize(102, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.evaluerLineEdit.setFont(font)
        self.evaluerLineEdit.setAutoFillBackground(False)
        self.evaluerLineEdit.setReadOnly(True)
        self.evaluerLineEdit.setObjectName(_fromUtf8("evaluerLineEdit"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.evaluerLineEdit)
        self.labelSpread = QtGui.QLabel(self.tab_obligation)
        self.labelSpread.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSpread.setObjectName(_fromUtf8("labelSpread"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelSpread)
        self.doubleSpinBoxSpread = QtGui.QDoubleSpinBox(self.tab_obligation)
        self.doubleSpinBoxSpread.setMinimumSize(QtCore.QSize(102, 0))
        self.doubleSpinBoxSpread.setSingleStep(0.1)
        self.doubleSpinBoxSpread.setObjectName(_fromUtf8("doubleSpinBoxSpread"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxSpread)
        self.labelFrequenceCoupon = QtGui.QLabel(self.tab_obligation)
        self.labelFrequenceCoupon.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelFrequenceCoupon.setObjectName(_fromUtf8("labelFrequenceCoupon"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.labelFrequenceCoupon)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.tab_obligation, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.LabelAnnuite.setBuddy(self.LineEditAnnuite)
        self.LabelTauxActualisation.setBuddy(self.DateEditDateActualisation)
        self.LabelDateActualisation.setBuddy(self.LineEditTauxActualisation)
        self.LabelDateAnnuite.setBuddy(self.DateEditDateAnnuite)
        self.LabelTauxActuariel.setBuddy(self.doubleSpinBoxTauxActuariel)
        self.labelSpread.setBuddy(self.doubleSpinBoxSpread)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Calculette Financière", None))
        self.groupBox.setTitle(_translate("Form", "VAN - Valeur Actuelle Nette d\'un montant", None))
        self.LabelAnnuite.setText(_translate("Form", "&Montant", None))
        self.LabelTauxActualisation.setText(_translate("Form", "&Taux d\'actualisation", None))
        self.LabelDateActualisation.setText(_translate("Form", "&Date d\'actualisation", None))
        self.DateEditDateActualisation.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.LabelDateAnnuite.setText(_translate("Form", "Date du montant", None))
        self.DateEditDateAnnuite.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.pushButtonVanEval.setText(_translate("Form", "&Calculer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_functions), _translate("Form", "Fonctions", None))
        self.nominalLabel.setText(_translate("Form", "Nominal", None))
        self.tauxFacialLabel.setText(_translate("Form", "Taux Facial", None))
        self.doubleSpinBoxTauxFacial.setSuffix(_translate("Form", " %", None))
        self.LabelTauxActuariel.setText(_translate("Form", "&Taux Actuariel", None))
        self.doubleSpinBoxTauxActuariel.setSuffix(_translate("Form", " %", None))
        self.dateEmissionLabel.setText(_translate("Form", "Date Emission", None))
        self.dateEditDateEmission.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.dateDeJouissanceLabel.setText(_translate("Form", "Date de Jouissance", None))
        self.dateEditDateJouissance.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.dateDChAnceLabel.setText(_translate("Form", "Date d\'echeance", None))
        self.dateEditDateEcheance.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.LabelDateEvaluation.setText(_translate("Form", "Date d\'évaluation", None))
        self.dateEditDateEvaluation.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.pushButtonObligEval.setText(_translate("Form", "&Calculer", None))
        self.labelSpread.setText(_translate("Form", "&Spread", None))
        self.doubleSpinBoxSpread.setSuffix(_translate("Form", " %", None))
        self.labelFrequenceCoupon.setText(_translate("Form", "Fréquence de coupons", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_obligation), _translate("Form", "Obligation", None))
        self.pushButton.setText(_translate("Form", "Quitter", None))
