# coding=utf-8
__author__ = 'F.Marouane'

"""
    Ce fichier ne contient que des 'first-class functions',
    des fonctions pouvant etre appellées de nulle-part concept typique de python.
    Le fichier Controller contient les fonctions qui vont assurer le contrôles de données
    et des actions depuis l'interface graphique.
"""

from DPricer.lib.Gestion import Gestion, GestionMd
from DPricer.lib.Portefeuille import Portefeuille, PortefeuilleMd
from DPricer.data.AppModel import *
import datetime as dt
from DPricer.data.AppModel import AppModel


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

def function():
    """
    testing my GitHub
    :return:
    """
    pass

if __name__ == '__main__':
    ajouter_obligation(8888888, 'MERO Oblig', 22222, .045, '22/7/1989',\
                           '22/7/1990', '10/10/2010', 55, 'AMC')