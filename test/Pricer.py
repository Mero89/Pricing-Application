# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.lib.Obligation import *
from DPricer.lib.Courbe import *
import datetime as dt
from DPricer.data.AppModel import *
import pandas as pd


def prix_titre(actif, date_eval, courbe=None):
    """
    Retourne le prix du titre.
    :param actif:
    :type DPricer.data.ObligationMd:
    :param date_eval:
    :type dt.datetime:
    :param courbe:
    :type DPricer.lib.Courbe:
    :return: float
    """
    titre = load_model(actif, date_eval, courbe)
    return titre.prix()


def simulate():
    s = AppModel().get_session()
    actifs = s.query(ObligationMd).all()
    date_eval = dt.date(2014, 12, 5)
    date_limite = date_eval.replace(year=date_eval.year - 2)
    _courbes = s.query(CourbeMd).filter(CourbeMd.date_req >= date_limite).distinct(CourbeMd.date_req).all()
    _dates = (el.date_req for el in _courbes)
    courbes = [Courbe(el) for el in _dates]
    res_dict = dict()
    for a in actifs:
        res_dict[a.isin] = [{c.date_du_jour: prix_titre(a, date_eval, courbe=c)} for c in courbes]
    else:
        return res_dict


def get_serie(result):
    id_result = pd.DatetimeIndex([x.keys()[0] for x in result])
    val_result = [x.values()[0] for x in result]
    s_result = pd.Series(val_result, index=id_result)
    return s_result

if __name__ == '__main__':
    res_dic = simulate()
    print res_dic['9088.0']
    pass
    # todo: Completer le truc des courbes et preparer les données pour l'analyse régressive et y penser à Siegel
    # d1 = dt.date(2013, 12, 5)
    # d2 = dt.date(2012, 6, 5)
    # courbe = Courbe(d1)
    # cc = Courbe(d2)
    # px=dict()
    # px[d1] = prix_titre(actif, dt.date(2014, 12, 5), courbe)
    # px[d2] = prix_titre(actif, dt.date(2014, 12, 5), cc)
    # print px