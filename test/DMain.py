# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MainApp import Ui_MainWindow
import sys


class MainBox(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage('Window Loaded', 2000)

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MainBox()
    form.show()
    ap.exec_()