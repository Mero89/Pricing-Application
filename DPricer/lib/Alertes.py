# coding=utf-8
__author__ = 'F.Marouane'

import os
import pickle
import shelve
import datetime as dt
import os.path as path


class AlertManager(object):
    """
    Classe qui gère les alertes de l'application.
    """
    _alerts = {}
    _dbname = 'Alerts.db'

    def __init__(self):
        self.filename = 'serial alerts.pkl'
        self.pathfile = path.join(os.getcwdu(), 'serial', self.filename)

    def launch_alerts(self):
        pass

    def create_alert(self, alert):
        if alert in self._alerts:
            return self._alerts[alert]
        self._alerts[alert] = alert

    def load_alerts(self):

        f = file(self.pathfile, 'rb')
        self._alerts = pickle.load(f)
        f.close()

    def save_alerts(self):
        filename = 'serial alerts.pkl'
        pathfile = path.join(self.serial_path, filename)
        f = file(pathfile, 'wb')
        # pickle.dump(self._alerts, f)
        pkl = shelve
        f.close()


class AssetAlert(object):
    """
    Classe qui représente les alertes liées aux futures échéances des actifs.
    """
    def __init__(self, alert_date):
        self.alert_date = alert_date
        pass

    def check_assets(self):
        pass

if __name__ == '__main__':
    am = AlertManager()
    # am.create_alert('an Alert')
    # aa = AssetAlert(dt.date.today())
    # am.create_alert(aa)
    # am.save_alerts()
    am.load_alerts()
    print am._alerts