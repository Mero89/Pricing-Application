# coding=utf-8
__author__ = 'F.Marouane'

"""
Ce fichier ne contient que des 'first-class functions',
des fonctions pouvant etre appellées de nulle-part concept typique de python.
Le fichier Controller contient les fonctions qui vont assurer le contrôle
de données et des actions depuis l'interface graphique.
"""

import datetime as dt

from PyQt4 import QtCore

from DPricer.lib.Gestion import Gestion
from DPricer.lib.Portefeuille import Portefeuille
from DPricer.data.AppModel import AppModel, ObligationMd, CourbeMd


class Unique(type):
    """
    Singleton pour Date Eval
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Unique, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DateEval(object):
    """
    Représente le Singleton Date d'évaluation.
    """
    __metaclass__ = Unique

    def __init__(self, _date=None):
        self.default = dt.date.today()
        if _date is None:
            self.date_eval = self.last_valid_date(dt.date.today())
        elif _date is not None:
            self.date_eval = self.last_valid_date(_date)

    def change_date(self, value):
        """
        Change la date d'évaluation de l'application.
        :param value: datetime.date
        :return: None
        """
        if self.check_courbe(value):
            self.date_eval = self.validate_date(value)
        else:
            self.date_eval = self.last_valid_date(value)

    def last_valid_date(self, _date):
        """
        :type _date: datetime.date
        :return: datetime.date
        """
        compare_to = self.validate_date(_date)
        session = AppModel().get_session()
        res = [el[0] for el in session.query(CourbeMd.date_req).distinct().all()]
        res.sort(reverse=True)
        if _date in res:
            return _date
        else:
            ld = [d for d in res if d <= compare_to]
            try:
                return ld[0]
            except IndexError:
                return dt.date.today()

    # noinspection PyArgumentList
    def get_qdate(self):
        """
        Retourne la date en Qdate.
        :return: PyQt4.QtCore.QDate
        """
        if self.date_eval:
            d = self.date_eval.day
            m = self.date_eval.month
            y = self.date_eval.year
            return QtCore.QDate(y, m, d)
        else:
            return QtCore.QDate.currentDate()

    def check_courbe(self, _date):
        """
        :type _date: object
        :return:
        """
        date = self.validate_date(_date)
        session = AppModel().get_session()
        res = session.query(CourbeMd).filter_by(date_req=date).first()
        if res:
            return True
        else:
            return False

    @staticmethod
    def validate_date(_date):
        """
        accepte une date ou CDC et retourne la date correspondante.
        :return: datetime.date
        """
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


def maroc_clear_to_isin(mc):
    if isinstance(mc, str):
        s = mc.split('MA')[1].strip()[3:9]
        return s


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
    """
    Ajoute une obligation à la base de données.
    :param isin: str
    :param nm: str
    :param nominal: float
    :param tx_f: float
    :param d_em: datetime.date
    :param d_j: datetime.date
    :param d_ech: datetime.date
    :param spread: float
    :param type_: str
    :return:
    """
    md = AppModel()
    session = md.get_session()
    ex = session.query(ObligationMd).filter_by(isin=str(isin)).first()
    if ex is None:
        obl = ObligationMd(isin=str(isin), nom=str(nm), nominal=nominal,\
                           taux_facial=tx_f, date_emission=validate_date(d_em),\
                           date_jouissance=validate_date(d_j),\
                           maturite=validate_date(d_ech),\
                           spread=spread, type=type_)
        session.add(obl)
        session.commit()
    elif ex is not None:
        pass
        # raise ObligationAlreadyExists
        # print " l'Oblig [{}] d'ISIN: {} existe déjà".format(ex.nom, ex.isin)
    md.close_session()


def validate_date(_date):
    """
    accepte une date ou CDC et retourne la date correspondante.
    :return: datetime.date
    """
    if type(_date) is str:
        return dt.datetime.strptime(_date, '%d/%m/%Y').date()
    else:
        return _date


def table_portefeuille(uid):
    """
    Retourne les portefeuilles gérés par le gestionnaire.
    :param uid: int
    :return: list of DPricer.lib.Portefeuille.Portefeuille
    """
    p_isins = Gestion().portefeuille_of_manager(uid)
    pf = [Portefeuille(el) for el in p_isins]
    return pf
