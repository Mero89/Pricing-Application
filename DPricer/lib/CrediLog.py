# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.data.AppModel import AppModel, EcheancierMd, ObligationMd
from DPricer.lib.Courbe import Courbe
from Interpolation import Interpol
import datetime as dt
# import calendar as cal


class Credilog(object):
    """
    *  Vérifier zc_list() de la classe Courbe.
    ** Vérifier la liste d'itération des dates.
    """
    def __init__(self, date_eval, isin='5032'):
        self.isin = isin
        self.baseA = 365.
        if date_eval:
            self.date_eval = self.validate_date(date_eval)
        self.zerocoupon_list = Courbe(date_eval).zc_list()
        self.echeancier = self.extract_echeancier()
        self.montant_restant = 89687.5
        self.db = self.load_model()
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
        # vect_coupon = [0.252054795]+ech[1:]
        vect_coupon = [0.25]*len(ech)
        # vect_coupon = [0.252054795, 0.246575342, 0.249315068, 0.252054795,
        #                0.25136612, 0.24863388, 0.24863388, 0.25136612,
        #                0.252054795, 0.246575342, 0.249315068, 0.252054795,
        #                0.252054795, 0.246575342, 0.249315068, 0.252054795,
        #                0.252054795, 0.246575342, 0.249315068, 0.252054795,
        #                0.25136612, 0.24863388, 0.24863388, 0.25136612,
        #                0.252054795, 0.246575342, 0.249315068, 0.252054795,
        #                0.252054795, 0.246575342]
        # print 'avg ==> ', sum(vect_coupon)/len(vect_coupon)
        ordre = 0
        px = 0
        index = 0
        for i in ech:
            ordre += i
            tx_zc = self.interp_zc(ordre)
            val_coupon = montant_restant * self.db.taux_facial * vect_coupon[index]
            # print val_coupon
            next_coupon = self.echeancier[index].amortissement + val_coupon
            # print 'Montant Coupon: {} au: {} actualisé au taux: {}'.format(next_coupon, index, tx_zc)
            van = next_coupon * pow(1 + tx_zc + sensi + self.db.spread, -ordre)
            # print van
            montant_restant -= self.echeancier[index].amortissement
            index += 1
            px += van
        return px

    def sensibilite(self, sensi=.0001):
        """
        Calcule la sensibilité de l'actif.
        :type sensi: float
        :return: float
        """
        real_price = self.prix()
        new_price = self.prix(sensi)
        r = abs(new_price - real_price) / real_price
        return round(r / sensi, 6)

    def duration(self):
        """
        Calcule la duration de l'actif.
        :return: float
        """
        # Duration se calcule depuis la sensibilité => Duration =Sensi*(1+Tr)
        # dur = self.sensibilite() * (1 + self.db.taux_actuariel + self.db.spread)
        # return round(dur, 6)
        pass

    def interp_zc(self, coeff):
        """
        Retourne la valeur interpolée.
        :type coeff: float
        :return: float
        """
        liste_coeff = [el[1] for el in self.zerocoupon_list]
        liste_tx = [el[0] for el in self.zerocoupon_list]
        i = Interpol(liste_tx, liste_coeff)
        # return round(i.i_lineaire(coeff), 5)
        return i.i_lineaire(coeff)

    def validate_date(self, _date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date

if __name__ == '__main__':
    log = Credilog('7/11/2014')
    # print len(log.coeff_echeancier())
    # print log.zerocoupon_list
    print 'Prix ==', log.prix()
    # print 'Prix ==', log.duration()
    print 'Sensi ==', log.sensibilite()
    # print log.interp_zc(0.1739130435)+log.db.spread