# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.data.AppModel import AppModel, EcheancierMd, ObligationMd
from DPricer.lib.Courbe import Courbe
import datetime as dt


class Pricer(object):
    def __init__(self, actif, date_eval, mode='BAM'):
        if mode.upper() in ('BAM', 'ZC'):
            self.mode = mode
        self.actif = actif
        self.date_eval = validate_date(date_eval)
        self.courbe = Courbe(self.date_eval)
        pass

    def prix(self):
        pass


def validate_date(_date):
    if isinstance(_date, str):
        return dt.datetime.strptime(_date, '%d/%m/%Y').date()
    else:
        return _date


def validate_float(number):
    if number is None or number == '':
        return 0
    if isinstance(number, float):
        return number
    else:
        return float(number)
