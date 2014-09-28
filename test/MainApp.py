# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/DPricer/test/DPricer.ui'
#
# Created: Wed Sep  3 16:48:59 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 464)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(145, 186))
        self.dockWidget.setMaximumSize(QtCore.QSize(165, 524287))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setMinimumSize(QtCore.QSize(115, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(160, 16777215))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.Box = QtGui.QWidget()
        self.Box.setGeometry(QtCore.QRect(0, 0, 125, 312))
        self.Box.setObjectName(_fromUtf8("Box"))
        self.toolBox.addItem(self.Box, _fromUtf8(""))
        self.Box2 = QtGui.QWidget()
        self.Box2.setGeometry(QtCore.QRect(0, 0, 125, 312))
        self.Box2.setObjectName(_fromUtf8("Box2"))
        self.toolBox.addItem(self.Box2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.toolBox)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DPricer", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Box), _translate("MainWindow", "Obligations", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Box2), _translate("MainWindow", "Courbe Taux", None))

