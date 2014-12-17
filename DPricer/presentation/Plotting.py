# coding=utf-8
__author__ = 'F.Marouane'
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
import datetime as dt
from DPricer.data.AppModel import CourbeMd, AppModel
from DPricer.lib.Courbe import Courbe
from DPricer.lib.Interpolation import Interpol
from DPricer.lib.YieldManager import YieldManager

def make_label(value, pos):
    if value < 365:
        return ''
    else:
        op = divmod(value, 365)
        if op[1] == 0:
            return str(op[0])+' ans'

if __name__ == '__main__':
    # YM = YieldManager()
    # YM.import_auto()
    # md = AppModel()
    # s = md.get_session()
    # res = s.query(CourbeMd).all()
    # for el in res:
    #     print el.date_req
    # res = md.session.query(CourbeMd).filter_by(date_req=ladate).all()
    ladate = dt.date(2014, 9, 15)
    cc = Courbe(ladate)
    # print cc.baseA
    print cc.liste_dico
    print 'taux 1 AN =>', cc.taux_lineaire(365)*100
    # print 'taux=> 3.1%; maturite => 298', cc.monetaire_actuel(.031, 298) * 100
    print 'taux 2 ANS =>', cc.taux_lineaire(730)*100
    # print cc.liste_dico
    # print cc.taux_lineaire(300)
    # courbe brute
    # liste_maturite_b = cc.liste_maturite
    # liste_taux_b = cc.liste_taux
    # liste_taux_b = [0]+liste_taux_b
    # liste_maturite_b = [0]+ liste_maturite_b
    # b_taux = np.array(liste_taux_b)
    # b_mat = np.array(liste_maturite_b)
    # courbe tenors
    # liste_tenors = [1, 91, 182, 273, 365, 455, 546, 637, 730, 1825, 3650, 5475, 7300]
    # mini = min(cc.liste_maturite)
    # liste_tenors = range(mini+1, 3650, 2)
    # liste_taux = [cc.taux_lineaire(m)*100 for m in liste_tenors]
    # liste_taux_spline = [cc.taux_spline(m)*100 for m in liste_tenors]
    # b_taux = np.array(liste_taux)
    # t_mat = np.array(liste_tenors)
    # t_taux = np.array(liste_taux)
    # t_spline = np.array(liste_taux_spline)

    # print 349 in cc.liste_maturite
    # print cc.zero_coupon()
    # print t_mat
    # print t_spline

    # Plotting
    # titre = 'Courbe BAM du {}'.format(ladate.strftime('%d/%m/%Y'))
    # plt.title(titre)
    # ax = plt.axes()
    # plt.xlabel('Maturites')
    # plt.ylabel('Taux Actuariel')
    # ax.xaxis.set_major_locator(mp.ticker.MultipleLocator(365))
    # ax.xaxis.set_major_formatter(mp.ticker.FuncFormatter(make_label))
    # labels = ax.get_xticklabels()
    # ax.xaxis.set_minor_locator(mp.ticker.MultipleLocator(45))
    # plt.plot(t_mat, t_taux, 'b', label='Courbe BAM')
    # plt.plot(t_mat, t_spline,'r', label='Courbe Spline')
    # plt.plot(b_mat,b_taux, 'k', label = 'Courbe Brute')
    # plt.setp(labels, rotation=30.)
    # plt.grid(True)
    # plt.legend(loc='best')
    # plt.show()
