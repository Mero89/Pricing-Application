# coding=utf-8
__author__ = 'F.Marouane'

import calendar as cal
import datetime as dt
from DPricer.lib.Courbe import Courbe


class Coupon(object):
    """
    Représente une classe Coupon.
    """

    def __init__(self, date_coupon, tx_facial, nominal):
        if date_coupon is not None:
            self.date_coupon = self.validate_date(date_coupon)
        self.taux_facial = float(tx_facial)
        self.nominal = float(nominal)
        self.coupon = self.nominal * self.taux_facial
        if cal.isleap(self.date_coupon.year):
            self.base = 366
        else:
            self.base = 365

    def __str__(self):
        return 'date coupon: {d}, coupon: {c}'.format(d=self.date_coupon, c=self.coupon)

    def __repr__(self):
        return '{d}::{c}'.format(d=self.date_coupon, c=self.coupon)

    def __sub__(self, other):
        if type(other) is Coupon:
            return self.date_coupon - other.date_coupon

    def get_coupon(self, d_coupon):
        if d_coupon == self.date_coupon:
            return self.coupon

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date


class Echeancier(object):
    """
    Classe représentant un échéancier.
    l'échéancier génère un echeancier à partir des dates de début
    et de fin suivant une périodicité désirée.
    echelle => a : An, m: Mois, d: jours
    """

    def __init__(self, debut, fin, periode, echelle='a'):
        self.debut = self.validate_date(debut)
        self.fin = self.validate_date(fin)
        self.periode = periode
        self.echelle = echelle

    def echeancier(self, flag=1):
        return self.digest(self.debut, self.fin, self.periode, flag)

    def coupons(self, tx_facial=0, nominal=0):
        ech = self.echeancier()
        coupons = list()
        for i in range(1, len(ech)):
            coupons.append(Coupon(ech[i], tx_facial, nominal))
        return coupons

    def digest(self, start, end, periode, flag=1):
        echeancier = list()
        st = start
        e = end
        if flag == 1:
            p = periode
            while st < e:
                echeancier.append(st)
                st = self.incremente(st, p, self.echelle)
            else:
                echeancier.append(e)
            return echeancier
        elif flag == -1:
            p = -periode
            while st < e:
                echeancier.append(e)
                e = self.incremente(e, p, self.echelle)
            else:
                echeancier.append(st)
            return echeancier

    def incremente(self, _date, periode, echelle='a'):
        """
        incrémente une date par la périodicité choisie.
        """
        if type(periode) is int:
            if echelle == 'a':
                return _date.replace(year=_date.year + periode)
            elif echelle == 'm':
                s = divmod(_date.month + periode, 12)
                if s[1] >= 1:
                    return _date.replace(month=s[1], year=_date.year +s[0])
                elif s[1] == 0 and s[0] > 1:
                    return _date.replace(year=_date.year + s[0])
                elif s[1] == 0 and s[0] == 1:
                    return _date.replace(month=12)
            elif echelle == 'd':
                delta = dt.timedelta(days= periode)
                return _date + delta

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date


class Obligation(object):
    """
    Classe représentant une Obligation.
    """

    def __init__(self, nominal, tx_f, d_em, d_j, d_ech, d_eval=None, spread=0, tx_act=None, nom='', le_type='',
                 isin=''):
        # si Date evaluation n'est pas definie, elle prend la valeur d'aujourd'hui
        self.base = 360
        self.baseA = 365
        self.nom = nom
        self.type = le_type
        self.isin = isin
        # BEGIN VALIDATION DES DATES
        if d_eval is None:
            self.date_evaluation = dt.date.today()
        elif d_eval is not None:
            self.date_evaluation = self.validate_date(d_eval)
        self.date_emission = self.validate_date(d_em)
        self.date_jouissance = self.validate_date(d_j)
        self.date_echeance = self.validate_date(d_ech)
        # END VALIDATION
        if cal.isleap(self.date_evaluation.year):
            self.baseA = 366
        self.nominal = self.validate_float(nominal)
        self.tx_facial = self.validate_float(tx_f)
        self.spread = self.validate_float(spread)
        # Maturité initiale
        self.maturite_initiale = (self.date_echeance - self.date_emission).days
        # Maturite residuelle
        self.mat_residuelle = (self.date_echeance - self.date_evaluation).days
        self.tx_actuariel = 0
        if tx_act is None and self.mat_residuelle > 0:
            self.courbe = Courbe(self.date_evaluation)
            self.tx_actuariel = self.courbe.taux_lineaire(self.mat_residuelle)
        elif tx_act is not None:
            self.tx_actuariel = tx_act
        self.coupons = list()
        self.e = Echeancier(self.date_jouissance.replace(year=self.date_jouissance+1), self.date_echeance, 1)

    def is_atypique_droite(self):
        de = self.date_echeance
        dj = self.date_jouissance
        duo = (de.month, de.day)
        duo2 = (dj.month, dj.day)
        if duo == duo2:
            return True

    def is_atypique_gauche(self):
        if self.date_emission != self.date_jouissance:
            return True

    def no_more_atypique(self):
        year_j = self.date_jouissance.year
        if self.is_atypique_gauche() and self.date_evaluation >= self.date_jouissance.replace(year=year_j + 1):
            return True

    def echeancier(self):
        return e.echeancier()
        pass

    def coeff_echeancier(self):
        coeff_echeancier = list()
        p = self.echeancier()
        # p = self.vie()
        p.insert(0, self.date_evaluation)
        for i in range(len(p) - 1):
            delta = abs((p[i + 1] - p[i]).days)
            mod = divmod(delta, 365)
            if mod[1] == 0 or mod[1] == 1:
                delta = mod[0]
            if mod[1] > 1:
                delta = float(delta) / self.baseA
            coeff_echeancier.append(delta)
        return coeff_echeancier

    def prix(self):
        if self.date_echeance <= dt.date.today():
            return 0
        else:
            if self.maturite_initiale < 365 and self.mat_residuelle < 365:
                tx_act = (self.tx_actuariel + self.spread) * self.mat_residuelle / self.base
                tx_facial = self.tx_facial * self.maturite_initiale / self.base
                prix = self.nominal * (1 + tx_facial) / (1 + tx_act)
                return round(prix, 2)
            elif self.mat_residuelle < 365 < self.maturite_initiale:
                if not self.is_atypique_gauche() or self.no_more_atypique():
                    # Si ligne Normale
                    tx_facial = self.tx_facial
                    tx_act = (self.tx_actuariel + self.spread) * self.mat_residuelle / self.base
                    prix = self.nominal * (1 + tx_facial) / (1 + tx_act)
                    return round(prix, 2)
                elif self.is_atypique_gauche():
                    # SI ligne Atypique
                    tx_facial = self.tx_facial * self.maturite_initiale / self.baseA
                    tx_act = (self.tx_actuariel + self.spread) * self.mat_residuelle / self.base
                    prix = self.nominal * (1 + tx_facial) / (1 + tx_act)
                    return round(prix, 2)
            elif self.mat_residuelle > 365 and self.maturite_initiale > 365:
                # Integre tous les cas pour calculer le prix de l'obligation
                # en utilisant la méthode de l'echeancier et des coefficients de l'écheancier
               pass

    def prix_long(self):
        """
        calcule le prx de l'oblig suivant ma nouvelle méthode.
        :return:
        """
        ob_vie = self.vie()
        nv_coupons = list()
        tx_act = self.tx_actuariel
        d_eval = self.date_evaluation
        liste_actuarielle = list()
        if self.coupons:
            ob_coupons = list(self.coupons)
        for i in range(len(ob_coupons) - 1):
            temp_coupon = ob_coupons[i+1] * (ob_coupons[i+1].date_coupon - ob_coupons[i].date_coupon).days / float(
                ob_coupons[i].base)
            ob_coupons[i].coupon = temp_coupon
        for i in range(len(ob_coupons)):
            puiss = (ob_coupons[1].date_coupon - d_eval).days / float(self.baseA)
            coeff_actu = pow(1/(1+tx_act), puiss)
            liste_actuarielle.append(coeff_actu)
            # Produit Scalaire entre vecteur d'actualisation et vecteur de coupons

    def getParams(self):
        return self.__dict__

    def sensibilite(self):
        real_price = self.prix()
        if self.tx_actuariel is not None and self.tx_actuariel != 0:
            self.tx_actuariel += .01
            new_price = self.prix()
            self.tx_actuariel -= .01
            try:
                r = abs(new_price - real_price) / real_price
                return round(r * 100, 4)
            except ZeroDivisionError:
                return 0
        else:
            return 0

    def duration(self):
        # Duration se calcule depuis la sensibilité => Duration =Sensi*(1+Tr)
        dur = self.sensibilite() * (1 + self.tx_actuariel + self.spread)
        return round(dur, 4)

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date

    def validate_float(self, number):
        if number is None or number == '':
            return 0
        if isinstance(number, float):
            return number
        else:
            return float(number)


def print_list(mylist):
    for el in mylist:
        print el

if __name__ == '__main__':
    # prix = 101752 MAD, ISIN = 100581
    nom = 100000
    tx_fac = .0416
    date_emission = '18/06/2014'
    date_jouissance = '20/06/2014'
    d_ech = '20/06/2016'
    date_eval = '2/10/2014'
    # tx_act = 0.04
    spread = .0060
    obl = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval)
    # obl.vie()
    # obl2 = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval, tx_act)
    # print obl.prix()
    # print obl.vie()
    # print obl.coupons
    e = Echeancier(date_emission, d_ech, 24, echelle='m')
    print e.echeancier()
