# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/DPricer/presentation/Designer-Files/Login.ui'
#
# Created: Tue Sep 30 12:31:42 2014
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(394, 278)
        Login.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Login)
        self.verticalLayout.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Login)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 65))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setMargin(8)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, 5, -1, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.userNameLabel = QtGui.QLabel(Login)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setObjectName(_fromUtf8("userNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.userNameLabel)
        self.userNameLineEdit = QtGui.QLineEdit(Login)
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.userNameLineEdit)
        self.motDePasseLabel = QtGui.QLabel(Login)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.motDePasseLabel.setFont(font)
        self.motDePasseLabel.setObjectName(_fromUtf8("motDePasseLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.motDePasseLabel)
        self.motDePasseLineEdit = QtGui.QLineEdit(Login)
        self.motDePasseLineEdit.setInputMask(_fromUtf8(""))
        self.motDePasseLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.motDePasseLineEdit.setObjectName(_fromUtf8("motDePasseLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.motDePasseLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Login)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.userNameLabel.setBuddy(self.userNameLineEdit)
        self.motDePasseLabel.setBuddy(self.motDePasseLineEdit)

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Login.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Dialog", None))
        self.label.setText(_translate("Login", "Veuillez fournir vos coordonnées pour accéder à votre workspace", None))
        self.userNameLabel.setText(_translate("Login", "&User Name", None))
        self.motDePasseLabel.setText(_translate("Login", "&Mot de Passe", None))

