# coding=utf-8
__author__ = 'F.Marouane'

import calendar as cal
from DPricer.data.AppModel import AppModel, CourbeMd
from Interpolation import Interpol
import datetime
import copy


class Courbe(CourbeMd):

    def __init__(self, date_du_jour):
        """
        initialise la courbe selon le jour recherché
        :param: date_du_jour: si CDC entrer la date au format 'jj/mm/aaaa'
        """
        md = AppModel()
        self.baseA = 365
        self.intervalle = range(56, 92)
        self.req = md.session.query(CourbeMd)
        if type(date_du_jour) is str:
            self.date_du_jour = datetime.datetime.strptime(date_du_jour, '%d/%m/%Y').date()
        else:
            self.date_du_jour = date_du_jour
        if cal.isleap(self.date_du_jour.year):
            self.baseA = 366
        res = self.req.filter_by(date_req=self.date_du_jour).all()
        self.date_de_transaction = res[0].date_transaction
        self.liste_taux = [c.taux_pondere for c in res]
        self.liste_maturite = [abs((c.date_echeance - c.date_valeur).days) for c in res]
        # retourne une liste de doublets : [taux, maturite_res]
        self.liste_dico = zip(self.liste_taux, self.liste_maturite)
        self.point_minimal = [el for el in self.liste_dico if el[1] in self.intervalle][0]
        md.close_session()

    def taux_lineaire(self, maturite):
        # retourne une liste de doublets < à la maturite cible.
        # Doublets => (taux, maturités)
        if maturite < self.point_minimal[1]:
            return self.point_minimal[0]
        else:
            copie_dico = copy.deepcopy(self.liste_dico)
            copie_dico = [list(tple) for tple in copie_dico]
            dico_inf = [i for i in copie_dico if i[1] < maturite]
            dico_sup = [i for i in copie_dico if i[1] > maturite]
            # selectionne la borne inférieure de la maturité désirée
            try:
                borne_inf = dico_inf[-1][1]
                borne_sup = dico_sup[0][1]
            except IndexError:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                return ii.i_lineaire(maturite)
            # selectionne la borne supérieure de la maturité désirée
            if maturite in self.liste_maturite:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                return ii.i_lineaire(maturite)
            elif maturite < 365 <= borne_sup:
                """
                Cas où la borne sup (taux) est actuarielle
                On la ramène au taux monétaire.
                """
                le_taux = self.actuel_monetaire(dico_sup[0][0], dico_sup[0][1])
                dico_sup[0][0] = le_taux
                """
                On rassemble notre liste avec le nouveau taux
                avant Interpolation.
                """
                # [..., [TAUX, MATURITE], ...]
                nv_liste_taux = [i[0] for i in dico_inf] + [i[0] for i in dico_sup]
                nv_liste_maturite = [i[1] for i in dico_inf] + [i[1] for i in dico_sup]
                ii = Interpol(nv_liste_taux, nv_liste_maturite)
                del copie_dico
                return ii.i_lineaire(maturite)
            elif maturite >= 365 > borne_inf:
                """
                Cas où la borne inf (taux) est monétaire
                On la ramène au taux actuariel
                """
                le_taux = self.monetaire_actuel(dico_inf[-1][0], dico_inf[-1][1])
                dico_inf[-1][0] = le_taux
                nv_liste_taux = [i[0] for i in dico_inf] + [i[0] for i in dico_sup]
                nv_liste_maturite = [i[1] for i in dico_inf] + [i[1] for i in dico_sup]
                ii = Interpol(nv_liste_taux, nv_liste_maturite)
                del copie_dico
                return ii.i_lineaire(maturite)
            else:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                return ii.i_lineaire(maturite)

    def taux_spline(self, maturite):
        """
        :param maturite:
        :return: le taux demandé par interpolation b-spline cubique
        """
        if maturite < self.point_minimal[1]:
            return self.point_minimal[0]
        else:
            copie_dico = copy.deepcopy(self.liste_dico)
            copie_dico = [list(tple) for tple in copie_dico]
            dico_inf = [i for i in copie_dico if i[1] < maturite]
            dico_sup = [i for i in copie_dico if i[1] > maturite]
            try:
                borne_inf = dico_inf[-1][1]
                borne_sup = dico_sup[0][1]
            except IndexError:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                del copie_dico
                return ii.i_spline(maturite)
            if maturite in self.liste_maturite:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                del copie_dico
                return ii.i_spline(maturite)
            elif maturite < 365 <= borne_sup:
                le_taux = self.actuel_monetaire(dico_sup[0][0], dico_sup[0][1])
                dico_sup[0][0] = le_taux
                nv_liste_taux = [i[0] for i in dico_inf] + [i[0] for i in dico_sup]
                nv_liste_maturite = [i[1] for i in dico_inf] + [i[1] for i in dico_sup]
                ii = Interpol(nv_liste_taux, nv_liste_maturite)
                del copie_dico
                return ii.i_spline(maturite)

            elif maturite >= 365 > borne_inf:
                le_taux = self.monetaire_actuel(dico_inf[-1][0], dico_inf[-1][1])
                dico_inf[-1][0] = le_taux
                nv_liste_taux = [i[0] for i in dico_inf] + [i[0] for i in dico_sup]
                nv_liste_maturite = [i[1] for i in dico_inf] + [i[1] for i in dico_sup]
                ii = Interpol(nv_liste_taux, nv_liste_maturite)
                del copie_dico
                return ii.i_spline(maturite)
            else:
                ii = Interpol(self.liste_taux, self.liste_maturite)
                del copie_dico
                return ii.i_spline(maturite)

    def monetaire_actuel(self, tx_mon, maturite_a_convertir):
        """
        :param tx_mon:
        :param maturite_a_convertir:
        :return: le taux monetaire depuis un taux actuariel
        """
        n = maturite_a_convertir
        b = 1 + (tx_mon * n / 360.0)
        puiss = float(self.baseA) / n
        tx_actuel = pow(b, puiss) - 1
        del n, b
        return tx_actuel

    def actuel_monetaire(self, tx_act, maturite_a_convertir):
        """
        n: représente la maturité que nous cherchons
        ex: n=300 avec borne inf = 250 et borne sup = 400
        """
        n = maturite_a_convertir
        b = pow((1 + tx_act), (float(n) / self.baseA)) - 1
        tx_monetaire = 360.0 / n * b
        del n, b
        return tx_monetaire

    def get_liste_taux(self):
        return self.liste_taux

    def get_liste_maturite(self):
        return self.liste_maturite

    def zc_dico(self):
        head = [(self.monetaire_actuel(el[0], el[1]), el[1] / 365.) for el in self.liste_dico if el[1] < 365]
        zc_dico = self.zero_coupon()
        tx1jour = self.monetaire_actuel(self.point_minimal[0], 1)
        pr = [(tx1jour, 1 / 365.)]
        dico = pr + head + zc_dico
        return dico

    def zero_coupon(self):
        # liste initialisée par le taux zero-coupon 1 an
        zc1 = self.taux_lineaire(365)
        liste_zc = [zc1]
        annee = self.date_de_transaction.year
        for ordre in range(2, 22):
            mat = (self.date_de_transaction.replace(year=annee + ordre) - self.date_de_transaction).days
            ta = self.taux_lineaire(mat)
            px = self.price(ta, ta, ordre)
            px_zc = self.price_zc(ta, liste_zc)
            diff = float(px - px_zc)
            zci = pow((1 + ta) / diff, 1. / ordre) - 1
            liste_zc.append(zci)
        else:
            return zip(liste_zc, range(1, 22))

    def price(self, tf, ta, p):
        px = []
        for i in range(1, p):
            px.append(tf / pow((1 + ta), i))
        else:
            px.append((1 + tf) / pow(1 + ta, p))
        return sum(px)

    def price_zc(self, tf, zc_list):
        px = []
        en_list = list(enumerate(zc_list, 1))
        for zc in en_list:
            px.append(tf / pow((1 + zc[1]), zc[0]))
        return sum(px)

    def tenors(self):
        # genere les tenors fixes
        pass


def test_monetaire_actuel():
    dd = datetime.date.today()
    cc = Courbe(date_du_jour=dd)
    tx = .03072
    mat = 222
    res = cc.monetaire_actuel(tx, mat)
    print 'Monétaire => Actuariel', res


def test_actuel_monetaire():
    dd = datetime.date.today()
    cc = Courbe(date_du_jour=dd)
    tx = .03142385
    mat = 103
    res = cc.actuel_monetaire(tx, mat)
    print 'Actuariel => Monétaire', res


if __name__ == '__main__':
    d = datetime.date(2014, 8, 22)
    c = Courbe(d)
    tx = c.taux_lineaire(400)
    print tx
    print c.get_liste_taux()
    print c.get_liste_maturite()
