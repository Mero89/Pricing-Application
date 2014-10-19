# coding=utf-8
__author__ = 'F.Marouane'

"""
    Ce fichier ne contient que des 'first-class functions',
    des fonctions pouvant etre appellées de nulle-part concept typique de python.
    Le fichier Controller contient les fonctions qui vont assurer le contrôles de données
    et des actions depuis l'interface graphique.
"""

from DPricer.lib.Gestion import Gestion
from DPricer.lib.Portefeuille import Portefeuille
from DPricer.data.AppModel import AppModel, ObligationMd, CourbeMd, GestionMd, PortefeuilleMd, EcheancierMd
import datetime as dt
from PyQt4 import QtCore


class Unique(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Unique, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DateEval(object):
    __metaclass__ = Unique

    def __init__(self, _date=None):
        self.default = dt.date.today()
        if _date is None:
            self.date_eval = self.last_valid_date(dt.date.today())
        elif _date is not None:
            self.date_eval = self.last_valid_date(_date)

    def change_date(self, value):
        if self.check_courbe(value):
            self.date_eval = self.validate_date(value)
        else:
            self.date_eval = self.last_valid_date(value)

    def last_valid_date(self, _date):
        compare_to = self.validate_date(_date)
        session = AppModel().get_session()
        res = [el[0] for el in session.query(CourbeMd.date_req).distinct().all()]
        res.sort(reverse=True)
        if _date in res:
            return _date
        else:
            ld = [d for d in res if d <= compare_to]
            return ld[0]

    def get_qdate(self):
        d = self.date_eval.day
        m = self.date_eval.month
        y = self.date_eval.year
        return QtCore.QDate(y, m, d)

    def check_courbe(self, _date):
        date = self.validate_date(_date)
        session = AppModel().get_session()
        res = session.query(CourbeMd).filter_by(date_req=date).first()
        if res:
            return True
        else:
            return False

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date

##############################
def afficher_gisement():
    md = AppModel()
    session = md.get_session()
    result = session.query(ObligationMd).all()
    md.close_session()
    return result


def supprimer_obligation(isin):
    md = AppModel()
    session = md.get_session()
    ex = session.query(ObligationMd).filter_by(isin=isin).first()
    if ex is not None:
        session.delete(ex)
    elif ex is None:
        # raise That the Asset is not found
        pass


def ajouter_obligation(isin, nm, nominal, tx_f, d_em, d_j, d_ech, spread=0, type_='N'):
    md = AppModel()
    session = md.get_session()
    ex = session.query(ObligationMd).filter_by(isin=str(isin)).first()
    if ex is None:
        obl = ObligationMd(isin=str(isin), nom=str(nm), nominal=nominal,\
                           taux_facial=tx_f, date_emission=validate_date(d_em),\
                           date_jouissance=validate_date(d_j), maturite=validate_date(d_ech),\
                           spread=spread, type=type_)
        session.add(obl)
        session.commit()
    elif ex is not None:
        pass
        # raise ObligationAlreadyExists
        # print " l'Oblig [{}] d'ISIN: {} existe déjà".format(ex.nom, ex.isin)
    md.close_session()


def validate_date(_date):
    if type(_date) is str:
        return dt.datetime.strptime(_date, '%d/%m/%Y').date()
    else:
        return _date


def table_portefeuille(uid):
    p_isins = Gestion().portefeuille_of_manager(uid)
    pf = [Portefeuille(el) for el in p_isins]
    return pf


if __name__ == '__main__':
    ajouter_obligation(8888888, 'MERO Oblig', 22222, .045, '22/7/1989',\
                           '22/7/1990', '10/10/2010', 55, 'AMC')