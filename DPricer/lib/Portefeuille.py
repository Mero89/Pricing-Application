# coding=utf-8
__author__ = 'F.Marouane'

import datetime as dt

from DPricer.data.AppModel import AppModel, PortefeuilleMd, ObligationMd
from Panier import Panier
from Obligation import Obligation


class Portefeuille(object):
    """
    La classe Portefeuille permet de pricer un Portefeuille ainsi
    que tous les actifs contenus dans ce dernier.
    """
    def __init__(self, p_isin, d_eval=None):
        md = AppModel()
        if d_eval is not None:
            self.date_eval = self.validate_date(d_eval)
        self.p_isin = p_isin
        self.session = md.get_session()
        self.nom = str(self.session.query(PortefeuilleMd.nom).filter_by(p_isin=self.p_isin).first()[0])
        # renvoie aussi la quantité. => [(ISIN, Qt)]
        self.actifs = self.load_actifs()
        # ==> [..., [Obligation ,Qt], ....]
        self.obligations = [[self.oblig_from_isin(a[0]), a[1]] for a in self.actifs]
        self.total = self.prix()

    def load_actifs(self):
        """
        Charge les actifs du portefeuille
        :return:
        """
        a = Panier().oblig_of_portefeuille(self.p_isin)
        return a

    def oblig_from_isin(self, isin):
        """
        Retourne un objet Obligation depuis son code [ISIN]
        :param isin:
        :return:
        """
        o = self.session.query(ObligationMd).get(str(isin))
        oblig = Obligation(o.nominal, o.taux_facial, o.date_emission, o.date_jouissance, o.maturite,
                           d_eval=self.date_eval, spread=o.spread, nom=o.nom, le_type=o.type, isin=o.isin)
        del o
        return oblig

    def update(self):
        """
        Met à jour les informations relatives au portefeuille.
        :return:
        """
        self.actifs = self.load_actifs()
        self.obligations = [[self.oblig_from_isin(o[0]), o[1]] for o in self.actifs]
        self.total = self.prix()

    def prix(self):
        """
        Calcule la somme des prix des obligations contenues dans le portefeuille
        :return prix_global:
        """
        prix_global = sum([obl[0].prix() * obl[1] for obl in self.obligations])
        return prix_global

    def sensibilite(self):
        """
        Calcule la sensibité du portefeuille
        :return sensi_globale:
        """
        sensi = 0
        for el in self.actifs:
            obl = self.oblig_from_isin(el[0])
            pd = self.ponderation(el[0])
            sensi += pd * obl.sensibilite()
        else:
            return sensi

    def duration(self):
        """
        Calcule la duration du portefeuille
        :return duration_globale:
        """
        dur = 0
        for el in self.actifs:
            obl = self.oblig_from_isin(el[0])
            pd = self.ponderation(el[0])
            dur += pd * obl.duration()
        else:
            return dur

    @staticmethod
    def validate_date(_date):
        if type(_date) is str:
            return dt.datetime.strptime(_date, '%d/%m/%Y').date()
        else:
            return _date

    def ponderation(self, isin):
        """
        calcule la pondération de la valeur d'un actif dans le potefeuille.
        :param isin:
        :return:
        """
        qt = Panier().quantite(self.p_isin, isin)
        obl = self.oblig_from_isin(isin)
        val = obl.prix() * qt
        return float(val/self.total)


if __name__ == '__main__':
    p = Portefeuille(100200, '1/9/2014')
    l = p.duration()
    s = p.sensibilite()
    print l
    print s
    # print p.prix()
    # res = p.session.query(PortefeuilleMd).all()
    # o = p.oblig_from_isin(100503)
    # Panier().add_oblig_to_portefeuille(100200,9074,5)
    # Panier().add_oblig_to_portefeuille(100200,9073,15)
