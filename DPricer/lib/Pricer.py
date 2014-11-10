# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.data.AppModel import AppModel, EcheancierMd, ObligationMd
from DPricer.lib.Courbe import Courbe
from Interpolation import Interpol
import datetime as dt
import calendar as cal


class Pricer(object):
    pass


class Credilog(object):
    def __init__(self, date_eval, isin='5032'):
        self.isin = isin
        self.baseA = 365
        if date_eval:
            self.date_eval = self.validate_date(date_eval)
        self.zerocoupon_list = Courbe(date_eval).zc_list()
        self.echeancier = self.extract_echeancier()
        self.montant_restant = 89687.5
        self.db = self.load_model()
        print self.db.__dict__
        pass

    def load_model(self):
        s = AppModel().get_session()
        return s.query(ObligationMd).filter_by(isin=self.isin).first()

    def extract_echeancier(self):
        s = AppModel().get_session()
        result_set = s.query(EcheancierMd).filter_by(isin=self.isin).order_by(EcheancierMd.date_coupon).all()
        result = [ech for ech in result_set if ech.date_coupon > self.date_eval]
        return result

    def coeff_echeancier(self):
        ech = self.echeancier
        coeff_echeancier = list()
        p = [el.date_coupon for el in ech if el.date_coupon > self.date_eval]
        p.insert(0, self.date_eval)
        for i in range(len(p) - 1):
            delta = abs((p[i + 1] - p[i]).days)
            mod = divmod(delta, 365)
            if mod[1] == 0 or mod[1] == 1:
                delta = mod[0]
            if mod[1] > 1:
                delta = float(delta) / self.baseA
            coeff_echeancier.append(delta)
        return coeff_echeancier

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
        montant_restant = float(self.montant_restant)
        ech = self.coeff_echeancier()
        ordre = 0
        px = 0
        index = 0
        for i in ech:
            ordre += i
            tx_zc = self.interp_zc(ordre)
            next_coupon = self.amortissement + montant_restant * self.tx_facial
            # print 'Montant Coupon: {} au: {} actualisé au taux: {}'.format(next_coupon, index, tx_zc)
            van = next_coupon * pow(1 + tx_zc + sensi + self.spread, -ordre)
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
        liste_coeff = [el[1] for el in self.zerocoupon_list]
        liste_tx = [el[0] for el in self.zerocoupon_list]
        i = Interpol(liste_tx, liste_coeff)
        return round(i.i_lineaire(coeff), 5)

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date

if __name__ == '__main__':
    log = Credilog('7/11/2014')
    log.extract_echeancier()