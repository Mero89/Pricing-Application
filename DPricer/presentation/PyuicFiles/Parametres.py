# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/DPricer/presentation/Designer-Files/Parametres.ui'
#
# Created: Tue Oct  7 10:13:44 2014
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

class Ui_Parametres(object):
    def setupUi(self, Parametres):
        Parametres.setObjectName(_fromUtf8("Parametres"))
        Parametres.resize(640, 380)
        Parametres.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Parametres)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.groupBox_2 = QtGui.QGroupBox(Parametres)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 315))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nomLabel = QtGui.QLabel(self.groupBox_2)
        self.nomLabel.setObjectName(_fromUtf8("nomLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.nomLineEdit.setObjectName(_fromUtf8("nomLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nomLineEdit)
        self.prenomLabel = QtGui.QLabel(self.groupBox_2)
        self.prenomLabel.setObjectName(_fromUtf8("prenomLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.prenomLabel)
        self.prenomLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.prenomLineEdit.setObjectName(_fromUtf8("prenomLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prenomLineEdit)
        self.unameLabel = QtGui.QLabel(self.groupBox_2)
        self.unameLabel.setObjectName(_fromUtf8("unameLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.unameLabel)
        self.unameLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.unameLineEdit.setObjectName(_fromUtf8("unameLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.unameLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.line = QtGui.QFrame(Parametres)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.groupBox = QtGui.QGroupBox(Parametres)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 315))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.nouveauMotDePasseLabel = QtGui.QLabel(self.groupBox)
        self.nouveauMotDePasseLabel.setObjectName(_fromUtf8("nouveauMotDePasseLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.nouveauMotDePasseLabel)
        self.nouveauMotDePasseLineEdit = QtGui.QLineEdit(self.groupBox)
        self.nouveauMotDePasseLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.nouveauMotDePasseLineEdit.setObjectName(_fromUtf8("nouveauMotDePasseLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.nouveauMotDePasseLineEdit)
        self.vRifierMotDePasseLabel = QtGui.QLabel(self.groupBox)
        self.vRifierMotDePasseLabel.setObjectName(_fromUtf8("vRifierMotDePasseLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.vRifierMotDePasseLabel)
        self.vRifierMotDePasseLineEdit = QtGui.QLineEdit(self.groupBox)
        self.vRifierMotDePasseLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.vRifierMotDePasseLineEdit.setObjectName(_fromUtf8("vRifierMotDePasseLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.vRifierMotDePasseLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(175, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.nomLabel.setBuddy(self.nomLineEdit)
        self.prenomLabel.setBuddy(self.prenomLineEdit)
        self.unameLabel.setBuddy(self.unameLineEdit)

        self.retranslateUi(Parametres)
        QtCore.QMetaObject.connectSlotsByName(Parametres)

    def retranslateUi(self, Parametres):
        Parametres.setWindowTitle(_translate("Parametres", "Parametres", None))
        self.groupBox_2.setTitle(_translate("Parametres", "Infos utilisateur", None))
        self.nomLabel.setText(_translate("Parametres", "&Nom", None))
        self.prenomLabel.setText(_translate("Parametres", "&Prenom", None))
        self.unameLabel.setText(_translate("Parametres", "Nom d\'&utilisateur", None))
        self.pushButton.setText(_translate("Parametres", "Enregistrer", None))
        self.groupBox.setTitle(_translate("Parametres", "Changer Mot de passe", None))
        self.nouveauMotDePasseLabel.setText(_translate("Parametres", "Nouveau Mot de passe", None))
        self.vRifierMotDePasseLabel.setText(_translate("Parametres", "Vérifier mot de passe", None))
        self.pushButton_2.setText(_translate("Parametres", "Changer mot de passe", None))

