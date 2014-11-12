# coding=utf-8

__author__ = 'F.Marouane'

import calendar as cal
import datetime as dt

from DPricer.lib.Courbe import Courbe
from DPricer.data.AppModel import AppModel, EcheancierMd


class Coupon(object):
    """
    Représente une classe Coupon.
    """

    def __init__(self, date_coupon, tx_facial=None, nominal=None, amortissement=None, coupon=None):
        if date_coupon is not None:
            self.date_coupon = validate_date(date_coupon)
        self.taux_facial = float(tx_facial)
        self.nominal = float(nominal)
        if amortissement is not None:
            self.coupon = amortissement
        elif coupon is not None:
            self.coupon = coupon
        else:
            self.coupon = self.nominal * self.taux_facial
        if cal.isleap(self.date_coupon.year):
            self.base = 366
        else:
            self.base = 365

    def __str__(self):
        """
        Affiche les infos nécessaires.
        """
        return 'date coupon: {d}, coupon: {c}'.format(d=self.date_coupon, c=self.coupon)

    def __repr__(self):
        """
        Affichage spécial
        """
        return '{d}::{c}'.format(d=self.date_coupon, c=self.coupon)

    def __sub__(self, other):
        """
        la Différence de deux coupons renvoie la différence des dates.
        """
        if type(other) is Coupon:
            return self.date_coupon - other.date_coupon

    def get_coupon(self, d_coupon):
        """
        Retourne le coupon associé à la date.
        """
        if d_coupon == self.date_coupon:
            return self.coupon


class Echeancier(object):
    """
    Classe représentant un échéancier.
    l'échéancier génère un echeancier à partir des dates de début
    et de fin suivant une périodicité désirée.
    echelle => a : An, m: Mois, d: jours
    """

    def __init__(self, debut, fin, periode, echelle='a'):
        self.debut = validate_date(debut)
        self.fin = validate_date(fin)
        self.periode = periode
        self.echelle = echelle

    def echeancier(self, flag=1):
        return self.digest(self.debut, self.fin, self.periode, flag)

    def coupons(self, tx_facial=0, nominal=0):
        ech = self.echeancier()
        coupons = list()
        for i in range(len(ech)):
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
                echeancier.reverse()
            return echeancier

    @staticmethod
    def incremente(_date, periode, echelle='a'):
        """
        :param _date: datetime.date
        :param periode: int
        :param echelle: str
        """
        if type(periode) is int:
            if echelle == 'a':
                return _date.replace(year=_date.year + periode)
            elif echelle == 'm':
                s = divmod(_date.month + periode, 12)
                if s[1] >= 1:
                    return _date.replace(year=_date.year + s[0], month=s[1])
                elif s[1] == 0 and s[0] > 1:
                    return _date.replace(year=_date.year + s[0])
                elif s[1] == 0 and s[0] == 1:
                    return _date.replace(month=12)
            elif echelle == 'd':
                delta = dt.timedelta(days=periode)
                return _date + delta


class EcheancierDB(object):
    """
    Classe qui gère les échéanciers forcés par l'utilisateur et qui sont stockés dans la BDD.
    """
    def __init__(self, isin=None):
        """
        Instancie un objet Echeancier depuis la base de données.
        :param isin: str
        :return:
        """
        self.session = AppModel().get_session()
        self.echeancier_to_add = None
        self.isin = isin
        self.coupons = None
        if isin is not None:
            self.coupons = self.load_echeancier(self.isin)

    def load_echeancier(self, isin):
        """
        Charge l'echeancier de l'actif désigné par [isin]
        :param isin: str
        :return: list
        """
        session = AppModel().get_session()
        self.coupons = session.query(EcheancierMd).filter_by(isin=str(isin)).all()
        echeancier = [el.date_coupon for el in self.coupons]
        return echeancier

    def add_coupon(self, isin, date_coupon, coupon=None, amortissement=None):
        """
        Ajoute un coupon à l'echeancier de l'actif designé par isin.
        :param isin: str
        :param date_coupon: datetime.date
        :param coupon: float
        :param amortissement: float
        :return:
        """
        cpon = EcheancierMd(isin=str(isin), date_coupon=date_coupon, coupon=coupon, amortissement=amortissement)
        try:
            self.echeancier_to_add.append(cpon)
        except AttributeError:
            self.echeancier_to_add = list()
            self.echeancier_to_add.append(cpon)

    def add_echeancier(self):
        """
        Insère l'échéancier après avoir ajouté les coupons.
        :return:
        """
        session = AppModel().get_session()
        session.add_all(self.echeancier_to_add)
        session.commit()

    @staticmethod
    def update_coupon(isin, date_coupon, cpon):
        """
        Where cpon is a dictionary.
        cpon = {isin:
                date_coupon:
                coupon:
                amortissement:}
        :param isin: str
        :param date_coupon: datetime.date
        :param cpon: dict
        """
        session = AppModel().get_session()
        session.query(EcheancierMd).filter_by(isin=str(isin), date_coupon=date_coupon).update(cpon)
        session.commit()

    def delete_echeancier(self, isin):
        """
        Supprime l'échéancier de l'actif [isin]
        :param isin: str
        """
        self.session.query(EcheancierMd).filter_by(isin=str(isin)).delete()
        try:
            self.session.commit()
        except (TypeError, ValueError):
            self.session.rollback()


class Obligation(object):
    """
    Classe représentant une Obligation.
    """

    def __init__(self, nominal, tx_f, d_em, d_j, d_ech, d_eval=None, spread=0, tx_act=None, nom='', le_type='',
                 isin=''):
        # threading.Thread.__init__(self)
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
            self.date_evaluation = validate_date(d_eval)
        self.date_emission = validate_date(d_em)
        self.date_jouissance = validate_date(d_j)
        self.date_echeance = validate_date(d_ech)
        # END VALIDATION
        if cal.isleap(self.date_evaluation.year):
            self.baseA = 366
        self.nominal = validate_float(nominal)
        self.tx_facial = validate_float(tx_f)
        self.spread = validate_float(spread)
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
        self.e = Echeancier(self.date_jouissance.replace(year=self.date_jouissance.year+1), self.date_echeance, 1)

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
        return self.e.echeancier()
        pass

    def coeff_echeancier(self):
        ech = self.e.echeancier()
        coeff_echeancier = list()
        p = [el for el in ech if el > self.date_evaluation]
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

    def coeff_actuariels(self, taux=0, spread=0):
        coeff_echeancier = self.coeff_echeancier()
        p = 0
        coeff_act = list()
        for i in range(len(coeff_echeancier)):
            p += coeff_echeancier[i]
            coeff = pow(1 / (1 + taux + spread), p)
            coeff_act.append(coeff)
        return coeff_act

    def coupons(self):
        cps = self.e.coupons(self.tx_facial, self.nominal)
        cps.insert(0, Coupon(self.date_emission, 0, 0))
        cps_restants = [el for el in cps if el.date_coupon > self.date_evaluation]
        before = cps[cps.index(cps_restants[0])-1]
        cps_restants.insert(0, before)
        for i in range(1, len(cps_restants)):
            coeff = (cps_restants[i] - cps_restants[i-1]).days/float(cps_restants[i].base)
            cps_restants[i].coupon *= coeff
        return cps_restants[1:]

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
                coeff_act = self.coeff_actuariels(self.tx_actuariel, self.spread)
                coupons = self.coupons()
                tableau = zip(coeff_act, coupons)
                px = 0
                for el in tableau:
                    px += el[0]*el[1].coupon
                else:
                    px += self.nominal * coeff_act[-1]
                return px

    def get_params(self):
        """
        Retourne les attributs de la classe.
        :return: dict
        """
        return self.__dict__

    def sensibilite(self):
        """
        Calcule la sensibilité de l'actif.
        :return: float
        """
        real_price = self.prix()
        var = .0001
        if self.tx_actuariel is not None and self.tx_actuariel != 0:
            self.tx_actuariel += var
            new_price = self.prix()
            self.tx_actuariel -= var
            try:
                r = abs(new_price - real_price) / real_price
                return round(r/var, 5)
            except ZeroDivisionError:
                return 0
        else:
            return 0

    def duration(self):
        # Duration se calcule depuis la sensibilité => Duration =Sensi*(1+Tr)
        dur = self.sensibilite() * (1 + self.tx_actuariel + self.spread)
        return round(dur, 4)


##### ext functions #####
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


# --><-- .....A Completer..... --><--
def load_model(md):
    dico = {'nominal': md.nominal,
            'tx_f': md.taux_facial, 'd_em': md.date_emission,
            'd_j': md.date_jouissance, 'd_ech': md.maturite,
            'd_eval': dt.date.today(), 'spread': md.spread}
    return Obligation(**dico)

if __name__ == '__main__':
    # prix = 101752 MAD, ISIN = 100581
    # import swampy.Lumpy as Lumpy
    # lumpy = Lumpy.Lumpy()
    # lumpy.make_reference()
    nom = 100000
    tx_fac = .0416
    date_emission = '30/04/2014'
    date_jouissance = '30/04/2014'
    d_ech = '10/04/2022'
    ech = Echeancier(date_emission, d_ech, 3, 'm')
    e = ech.echeancier()

    # date_eval = '2/10/2014'
    # tx_act = 0.04
    # spread = .0060
    # obl = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval, spread=spread)
    # print obl.coeff_actuariels()
    # for el in obl.coupons():
    #     print el
    # print obl.prix()
    # test_echeancier()
    # lumpy.object_diagram()
    # lumpy.class_diagram()