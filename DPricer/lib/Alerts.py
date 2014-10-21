# coding=utf-8
__author__ = 'F.Marouane'

from PyQt4.QtCore import QTimer
import datetime as dt
from DPricer.data.AppModel import AppModel, CourbeMd, ObligationMd
import threading


class AlertManager(object):
    """
    Classe qui gère les alertes de l'application.
    """
    _alerts = {}

    def __init__(self):
        pass

    def launch_alerts(self):
        pass

    def create_alert(self):
        pass

    def load_alerts(self):
        pass

    def save_alerts(self):
        pass


class AssetAlert(object):
    """
    Classe qui représente les alertes liées aux futures échéances des actifs.
    """
    def __init__(self, obligation):
        pass

    def check_assets(self):
        pass