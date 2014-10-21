# coding=utf-8
__author__ = 'F.Marouane'

import copy

from Interpolation import Interpol
from Obligation import Obligation


class ObligationAMC(Obligation):
    """
    Représente une Obligatin Amortissable.
    Le pricing d'une oblig Amortissable se base sur la courbe Zero-Coupon.
    """
    def __init__(self, nominal, tx_f, d_em, d_j, d_ech, d_eval=None, spread=0, forcee=False):
        """
        :type nominal: float
        :type tx_f: float
        :type d_em: datetime.date
        :type d_j: datetime.date
        :type d_ech: datetime.date
        :type d_eval: datetime.date
        :type spread: float
        :type forcee: bool
        :return:
        """
        Obligation.__init__(self, nominal, tx_f, d_em, d_j, d_ech, d_eval, spread)
        self.forcee = forcee
        self.amortissement = self.montant_amortissement()
        self.principal = len(self.coeff_actuariels()) * self.amortissement
        self.zc_dico = self.courbe.zc_dico()

    def montant_amortissement(self):
        """
        Calcule le montant d'amortissement de l'obligation à partir de la date de jouissance
        et la date d'echeance
        :return:
        """
        diff = self.date_echeance - self.date_emission
        nb_annees = divmod(diff.days, 365)[0]
        return float(self.nominal)/nb_annees

    def prix(self, sensi=0):
        """ pour afficher l'ensemble des étapes parcourues par la ligne
        Creer une fonction Tableau qui retourne un vecteur[4xN] tq:
            vect[0]: VAN des coupons
            vect[1]: montant restant dans le principal
            vect[2]: date de tombee des coupons
            vect[3]: taux zero_coupon avec lequel est calculée la VAN
        Dans ce cas la Fonction prix() serait simplement
        'return' sum(Tableau[0])
        NB => Modifier aussi la Sensibilité
        :type sensi: float
        """
        montant_restant = copy.deepcopy(self.principal)
        ech = self.coeff_echeancier()
        ordre = 0
        px = 0
        index = 0
        for i in ech:
            ordre += i
            tx_zc = self.interp_zc(ordre)
            next_coupon = self.amortissement + montant_restant * self.tx_facial
            # print 'Montant Coupon: {} au: {} actualisé au taux: {}'.format(next_coupon, index, tx_zc)
            van = next_coupon * pow(1 + tx_zc+sensi + self.spread, -ordre)
            montant_restant -= self.amortissement
            index += 1
            px += van
        return px

    def interp_zc(self, coeff):
        """
        Retourne la valeur interpolée.
        :type coeff: float
        :return: float
        """
        liste_coeff = [el[1] for el in self.zc_dico]
        liste_tx = [el[0] for el in self.zc_dico]
        i = Interpol(liste_tx, liste_coeff)
        return i.i_lineaire(coeff)

    def sensibilite(self, sensi=.001):
        """
        Calcule la sensibilité de l'actif.
        :type sensi: float
        :return: float
        """
        real_price = self.prix()
        new_price = self.prix(sensi)
        r = abs(new_price - real_price) / real_price
        return round(r * 100, 4)

    def duration(self):
        """
        Calcule la duration de l'actif.
        :return: float
        """
        # Duration se calcule depuis la sensibilité => Duration =Sensi*(1+Tr)
        dur = self.sensibilite() * (1 + self.tx_actuariel + self.spread)
        return round(dur, 4)

if __name__ == '__main__':
    nom = 100000
    tx_fac = 0.037
    date_emission = '20/12/2006'
    date_jouissance = '20/12/2006'
    d_ech = '20/12/2021'
    date_eval = '22/9/2014'
    spread = 0.002
    # prix: 54306.09
    # obl = Obligation(nom, tx_fac, date_emission, date_jouissance, d_ech)
    # obl = ObligationAMC(nom, tx_fac, date_emission, date_jouissance, d_ech, date_eval, spread)
