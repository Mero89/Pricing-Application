# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


def alert(message):
    """
    :param due: in seconds
    :return:
    """
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=48><b>" + message + "</b></font>")
    label.setWindowFlags(Qt.SplashScreen)
    label.move(1100,40)
    label.show()
    QTimer.singleShot(7000, app.quit)  # 1 minute
    app.exec_()

if __name__ == '__main__':
    ct = QTime.currentTime()
    alert(ct.toString())