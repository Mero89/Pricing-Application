# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/DPricer/presentation/Designer-Files/AddAssetDialog.ui'
#
# Created: Thu Oct  2 13:24:42 2014
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

class Ui_AddAsset(object):
    def setupUi(self, AddAsset):
        AddAsset.setObjectName(_fromUtf8("AddAsset"))
        AddAsset.resize(674, 506)
        self.verticalLayout = QtGui.QVBoxLayout(AddAsset)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 10, 5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBoxInfo = QtGui.QGroupBox(AddAsset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxInfo.sizePolicy().hasHeightForWidth())
        self.groupBoxInfo.setSizePolicy(sizePolicy)
        self.groupBoxInfo.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBoxInfo.setMaximumSize(QtCore.QSize(330, 16777215))
        self.groupBoxInfo.setObjectName(_fromUtf8("groupBoxInfo"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxInfo)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 281, 400))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.iSINLabel = QtGui.QLabel(self.layoutWidget)
        self.iSINLabel.setObjectName(_fromUtf8("iSINLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.iSINLabel)
        self.iSINLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.iSINLineEdit.setMaximumSize(QtCore.QSize(102, 16777215))
        self.iSINLineEdit.setObjectName(_fromUtf8("iSINLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.iSINLineEdit)
        self.nomLabel = QtGui.QLabel(self.layoutWidget)
        self.nomLabel.setObjectName(_fromUtf8("nomLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nomLineEdit.setMaximumSize(QtCore.QSize(102, 16777215))
        self.nomLineEdit.setObjectName(_fromUtf8("nomLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.nomLineEdit)
        self.nominalLabel = QtGui.QLabel(self.layoutWidget)
        self.nominalLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.nominalLabel.setObjectName(_fromUtf8("nominalLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.nominalLabel)
        self.nominalLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nominalLineEdit.setMinimumSize(QtCore.QSize(102, 0))
        self.nominalLineEdit.setMaximumSize(QtCore.QSize(102, 16777215))
        self.nominalLineEdit.setObjectName(_fromUtf8("nominalLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.nominalLineEdit)
        self.tauxFacialLabel = QtGui.QLabel(self.layoutWidget)
        self.tauxFacialLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.tauxFacialLabel.setObjectName(_fromUtf8("tauxFacialLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.tauxFacialLabel)
        self.doubleSpinBoxTauxFacial = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxTauxFacial.setMinimumSize(QtCore.QSize(102, 0))
        self.doubleSpinBoxTauxFacial.setObjectName(_fromUtf8("doubleSpinBoxTauxFacial"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTauxFacial)
        self.labelSpread = QtGui.QLabel(self.layoutWidget)
        self.labelSpread.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSpread.setObjectName(_fromUtf8("labelSpread"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelSpread)
        self.doubleSpinBoxSpread = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxSpread.setMinimumSize(QtCore.QSize(102, 0))
        self.doubleSpinBoxSpread.setSingleStep(0.1)
        self.doubleSpinBoxSpread.setObjectName(_fromUtf8("doubleSpinBoxSpread"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxSpread)
        self.dateEmissionLabel = QtGui.QLabel(self.layoutWidget)
        self.dateEmissionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateEmissionLabel.setObjectName(_fromUtf8("dateEmissionLabel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.dateEmissionLabel)
        self.dateEditDateEmission = QtGui.QDateEdit(self.layoutWidget)
        self.dateEditDateEmission.setObjectName(_fromUtf8("dateEditDateEmission"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.dateEditDateEmission)
        self.dateDeJouissanceLabel = QtGui.QLabel(self.layoutWidget)
        self.dateDeJouissanceLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateDeJouissanceLabel.setObjectName(_fromUtf8("dateDeJouissanceLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.dateDeJouissanceLabel)
        self.dateEditDateJouissance = QtGui.QDateEdit(self.layoutWidget)
        self.dateEditDateJouissance.setObjectName(_fromUtf8("dateEditDateJouissance"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.dateEditDateJouissance)
        self.dateDChAnceLabel = QtGui.QLabel(self.layoutWidget)
        self.dateDChAnceLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dateDChAnceLabel.setObjectName(_fromUtf8("dateDChAnceLabel"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.dateDChAnceLabel)
        self.dateEditDateEcheance = QtGui.QDateEdit(self.layoutWidget)
        self.dateEditDateEcheance.setObjectName(_fromUtf8("dateEditDateEcheance"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.dateEditDateEcheance)
        self.typeLabel = QtGui.QLabel(self.layoutWidget)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.typeLabel)
        self.typeComboBox = QtGui.QComboBox(self.layoutWidget)
        self.typeComboBox.setMaximumSize(QtCore.QSize(130, 110))
        self.typeComboBox.setObjectName(_fromUtf8("typeComboBox"))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.typeComboBox)
        self.forcerLabel = QtGui.QLabel(self.layoutWidget)
        self.forcerLabel.setObjectName(_fromUtf8("forcerLabel"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.forcerLabel)
        self.forcerCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.forcerCheckBox.setTristate(False)
        self.forcerCheckBox.setObjectName(_fromUtf8("forcerCheckBox"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.forcerCheckBox)
        self.horizontalLayout.addWidget(self.groupBoxInfo)
        self.line = QtGui.QFrame(AddAsset)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.groupBoxAvance = QtGui.QGroupBox(AddAsset)
        self.groupBoxAvance.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAvance.sizePolicy().hasHeightForWidth())
        self.groupBoxAvance.setSizePolicy(sizePolicy)
        self.groupBoxAvance.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBoxAvance.setMaximumSize(QtCore.QSize(350, 16777215))
        self.groupBoxAvance.setCheckable(False)
        self.groupBoxAvance.setChecked(False)
        self.groupBoxAvance.setObjectName(_fromUtf8("groupBoxAvance"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBoxAvance)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBoxAvance)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.toolButtonAdd = QtGui.QToolButton(self.groupBoxAvance)
        self.toolButtonAdd.setObjectName(_fromUtf8("toolButtonAdd"))
        self.horizontalLayout_2.addWidget(self.toolButtonAdd)
        self.toolButtonRemove = QtGui.QToolButton(self.groupBoxAvance)
        self.toolButtonRemove.setObjectName(_fromUtf8("toolButtonRemove"))
        self.horizontalLayout_2.addWidget(self.toolButtonRemove)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(self.groupBoxAvance)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBoxAvance)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddAsset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(730, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.labelSpread.setBuddy(self.doubleSpinBoxSpread)

        self.retranslateUi(AddAsset)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddAsset.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddAsset.reject)
        QtCore.QObject.connect(self.forcerCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBoxAvance.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AddAsset)

    def retranslateUi(self, AddAsset):
        AddAsset.setWindowTitle(_translate("AddAsset", "Dialog", None))
        self.groupBoxInfo.setTitle(_translate("AddAsset", "Fournir les informations nécessaires", None))
        self.iSINLabel.setText(_translate("AddAsset", "ISIN", None))
        self.nomLabel.setText(_translate("AddAsset", "Nom", None))
        self.nominalLabel.setText(_translate("AddAsset", "Nominal", None))
        self.tauxFacialLabel.setText(_translate("AddAsset", "Taux Facial", None))
        self.doubleSpinBoxTauxFacial.setSuffix(_translate("AddAsset", " %", None))
        self.labelSpread.setText(_translate("AddAsset", "Spread", None))
        self.doubleSpinBoxSpread.setSuffix(_translate("AddAsset", " %", None))
        self.dateEmissionLabel.setText(_translate("AddAsset", "Date Emission", None))
        self.dateEditDateEmission.setDisplayFormat(_translate("AddAsset", "dd/MM/yyyy", None))
        self.dateDeJouissanceLabel.setText(_translate("AddAsset", "Date de Jouissance", None))
        self.dateEditDateJouissance.setDisplayFormat(_translate("AddAsset", "dd/MM/yyyy", None))
        self.dateDChAnceLabel.setText(_translate("AddAsset", "Date d\'echeance", None))
        self.dateEditDateEcheance.setDisplayFormat(_translate("AddAsset", "dd/MM/yyyy", None))
        self.typeLabel.setText(_translate("AddAsset", "Type", None))
        self.typeComboBox.setItemText(0, _translate("AddAsset", "Normale ou Atypique (N)", None))
        self.typeComboBox.setItemText(1, _translate("AddAsset", "Amortissable (AMC)", None))
        self.typeComboBox.setItemText(2, _translate("AddAsset", "Révisable (REV)", None))
        self.typeComboBox.setItemText(3, _translate("AddAsset", "Amortissable Révisable (AMCREV)", None))
        self.forcerLabel.setText(_translate("AddAsset", "forcer", None))
        self.groupBoxAvance.setTitle(_translate("AddAsset", "Avancé", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddAsset", "Date Coupon", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddAsset", "Flux Coupon (MAD)", None))
        self.toolButtonAdd.setText(_translate("AddAsset", "+", None))
        self.toolButtonRemove.setText(_translate("AddAsset", "-", None))

