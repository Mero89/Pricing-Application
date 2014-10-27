# coding=utf-8
__author__ = 'F.Marouane'

import os
from collections import deque
import shelve
import datetime as dt
import os.path as path
from DPricer.lib.Obligation import Echeancier
from DPricer.data.AppModel import AppModel, ObligationMd


class AlertManager(object):
    def __init__(self):
        self.working_directory = os.getcwdu()
        self.filename = 'dbAlerts.db'
        self.dst_path = path.join(self.working_directory, 'serial', self.filename)
        self.coupon_alerts = deque()
        self.infine_alerts = deque()

    def shelve_alerts(self):
        dbalerts = shelve.open(self.dst_path, writeback=True)
        dbalerts['coupons'] = self.coupon_alerts
        dbalerts['remboursement'] = self.infine_alerts
        pass

    def unshelve_alerts(self):
        dbalerts = shelve.open(self.dst_path, writeback=True)
        self.coupon_alerts = dbalerts['coupons']
        self.infine_alerts = dbalerts['remboursement']
        print len(dbalerts['coupons'])

    def load_alerts(self):
        s = AppModel().get_session()
        res = s.query(ObligationMd).all()
        ech = [Echeancier(el.date_jouissance.replace(year=el.date_jouissance.year+1), el.maturite, 1).echeancier()
               for el in res]
        next_coupons = [[ec for ec in el if ec > dt.date.today()] for el in ech]
        print 'test  =====> ', len(next_coupons)
        alerts = list()
        for el in next_coupons:
            if len(el) >= 1:
                alerts.append(el[0])
        self.coupon_alerts = deque(alerts)

    def check_alerts(self):

        pass

if __name__ == '__main__':
    am = AlertManager()
    am.unshelve_alerts()
    am.load_alerts()
