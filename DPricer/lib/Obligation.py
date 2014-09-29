# coding=utf-8
__author__ = 'F.Marouane'

import calendar as cal
import datetime as dt
from DPricer.lib.Courbe import Courbe


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

    def echeancier(self):
        echeancier = list()
        # Si prochain coupon est la date de jouissance
        if self.date_evaluation <= self.date_jouissance:
            temp = self.date_jouissance
            while temp <= self.date_echeance:
                new_year = temp.year + 1
                temp = temp.replace(year=new_year)
                if temp > self.date_echeance:
                    if echeancier[-1] != self.date_echeance:
                        echeancier.append(self.date_echeance)
                else:
                    echeancier.append(temp)
            return echeancier
        if self.date_evaluation >= self.date_jouissance:
            temp = self.date_jouissance.replace(year=self.date_evaluation.year)
            if temp > self.date_evaluation:
                echeancier.append(temp)
            while temp <= self.date_echeance:
                new_year = temp.year + 1
                temp = temp.replace(year=new_year)
                if temp > self.date_echeance:
                    if echeancier[-1] != self.date_echeance:
                        echeancier.append(self.date_echeance)
                else:
                    echeancier.append(temp)
            return echeancier

    def no_more_atypique(self):
        year_j = self.date_jouissance.year
        if self.is_atypique_gauche() and self.date_evaluation >= self.date_jouissance.replace(year=year_j+1):
            return True

    def coeff_echeancier(self):
        coeff_echeancier = list()
        p = self.echeancier()
        p.insert(0, self.date_evaluation)
        for i in range(len(p) - 1):
            delta = abs((p[i] - p[i + 1]).days)
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
                coeff = self.coeff_echeancier()
                tx_act = self.tx_actuariel + self.spread
                coupon = self.nominal * self.tx_facial
                # liste_actuariel = [pow(1+tx_act, -c) for c in coeff if c != 0]
                liste_actuariel = list()
                p = 0
                for i in range(len(coeff) - 1):
                    if coeff[i] != 0:
                        p += coeff[i]
                        actu = pow(1 / (1 + tx_act), p)
                        # actu = pow(1/(1+tx_act), coeff[0]+i)
                        liste_actuariel.append(round(actu, 8))
                liste_coupons = [coupon] * len(liste_actuariel)
                liste_coupons[0] = coupon * coeff[0]
                prix = 0
                if len(liste_coupons) == len(liste_actuariel):
                    dcf = list()
                    for i in range(len(liste_coupons)):
                        dcf.append(liste_actuariel[i] * liste_coupons[i])
                        # print 'prix ==>', liste_coupons[i]*act
                    else:
                        # print 'total avt principal ==>',prix
                        in_fine = self.nominal * liste_actuariel[-1]
                        #print 'principal ==>', in_fine
                        dcf.append(in_fine)
                    prix = sum(dcf)
                return round(prix, 2)

    def getParams(self):
        return self.__dict__

    def sensibilite(self):
        real_price = self.prix()
        if self.tx_actuariel is not None and self.tx_actuariel != 0:
            self.tx_actuariel += .01
            new_price = self.prix()
            self.tx_actuariel -= .01
            r = abs(new_price - real_price) / real_price
            return round(r * 100, 4)
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
    nom = 100000
    tx_fac = 0.04
    date_emission = '03/03/2010'
    date_jouissance = '03/03/2010'
    d_ech = '03/03/2020'
    date_eval = '3/6/2015'
    tx_act = 0.04
    obl = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval, tx_act=tx_act)
    print obl.echeancier()
    # obl2 = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval, tx_act)
    print round(obl.prix(),2)