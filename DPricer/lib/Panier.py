# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.data.AppModel import PanierMd, AppModel


class Panier(object):
    """
    La classe Panier prend en charge l'ensemble des opérations qui concernent
    l'interaction entre les actifs et le portefeuille.
    Opérations:
            • Ajout/Modif/Suppression des actifs du portefeuile
            • Modif des Quantités de chaque actif dans un portefeuille.
            • Liste les actifs appartenant à un portefeuille donné.
            • Liste les Portefeuilles contenant un actif donné.
    """
    def __init__(self):
        md = AppModel()
        self.session = md.get_session()

    def quantite(self, p_isin, isin):
        """
        Retourne la quantité de l'actif de code [ISIN] dans le portefeuille
        de code [P_ISIN].
        :param p_isin:
        :param isin:
        :return:
        """
        res = self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).first()
        return res.quantite
        del res

    def oblig_of_portefeuille(self, p_isin):
        """
        Retourne une liste de code d'obligations [ISIN]
        appartenant au portefeuille de code [p_isin]
        avec leur quantité dans le PF.
        :param p_isin:
        :return [obligations.isin,Qt]:
        """
        liste_actifs = self.session.query(PanierMd).filter_by(p_isin=str(p_isin)).all()
        liste_finale = [[el.isin, el.quantite] for el in liste_actifs]
        del liste_actifs
        return liste_finale

    def portefeuille_from_obligation(self, isin):
        """
        Retourne une liste de protefeuilles identifiés par leur [p_isin]
        depuis l'obligation de code [ISIN]
        :param isin:
        :return Portefeuille.p_isin[]:
        """
        liste_portefuille = self.session.query(PanierMd).filter_by(isin=str(isin)).all()
        liste_finale = [el.p_isin for el in liste_portefuille]
        del liste_portefuille
        return liste_finale

    def add_oblig_to_portefeuille(self, p_isin, isin, quantite=1):
        """
        Ajoute une obligation à un portefeuille avec la quantité spécifiée
        :param isin:
        :param p_isin:
        :return:
        """
        pan = self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).first()
        # Si l'oblig n'existe pas
        if pan is None:
            # On ajoute une entrée
            rw = PanierMd(isin=str(isin), p_isin=str(p_isin), quantite=quantite)
            self.session.add(rw)
        # Si oblig Existe, on incrémente
        elif pan is not None:
            qt = pan.quantite
            qt += quantite
            self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).update({'quantite' : qt})

        try:
            self.session.commit()
        except:
            self.session.rollback()

    def delete_oblig_from_portefeuille(self, p_isin, isin):
        """
        supprime définitivement l'actif du portefeuille
        :param isin:
        :param p_isin:
        :return:
        """
        pan = self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).first()
        if pan is not None:
            self.session.delete(pan)
            try:
                self.session.commit()
            except:
                self.session.rollback()

    def remove_oblig_from_portefeuille(self, p_isin, isin, quantite):
        """
        Déduis 'N' d'obligations du portefeuille
        :param p_sisin:
        :param isin:
        :param quantite:
        :return:
        """
        pan = self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).first()
        # Si oblig Existe, on incrémente
        if pan is not None:
            qt = pan.quantite
            if qt <= quantite:
                self.delete_oblig_from_portefeuille(p_isin, isin)
            elif qt > quantite:
                qt -= quantite
            self.session.query(PanierMd).filter_by(p_isin=str(p_isin), isin=str(isin)).update({'quantite': qt})
        try:
            self.session.commit()
        except:
            self.session.rollback()

if __name__ == '__main__':
    pn = Panier()
    pn.add_oblig_to_portefeuille('100200', '100503',9)
    assets = pn.oblig_of_portefeuille('100200')
    for el in assets:
        print el