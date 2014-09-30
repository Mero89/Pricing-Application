# coding=utf-8
__author__ = 'F.Marouane'

from ..data.AppModel import AppModel, GestionMd, PortefeuilleMd


class Gestion(object):
    """
    La classe Gestion prend en charge l'ensemble des opérations qui concernent
    l'interaction entre le gestionnaire et les portefeuilles.
    Opérations:
            • Ajout/Modif/Suppression des portefeuilles gérés
            • Liste les portefeuilles gérés par le gestionnaire.
            • Liste les gestionnaires gérant un portefeuille donné.
    """
    def __init__(self):
        md = AppModel()
        self.session = md.get_session()

    def portefeuille_of_manager(self, uid):
        """
        Retourne la liste des portefeuilles gérés par le gestionnaire.
        :param uid:
        :return:
        """
        res = self.session.query(GestionMd).filter_by(uid=uid).all()
        liste_portefeuilles = [pf.p_isin for pf in res]
        p_res = [self.session.query(PortefeuilleMd).filter_by(p_isin=el).first() for el in liste_portefeuilles]
        return p_res

    def manager_of_portefeuille(self, p_isin):
        """
        Retourne la liste des gestionnaires gérant un portefeuille donné.
        :param p_isin:
        :return:
        """
        res = self.session.query(GestionMd).filter_by(p_isin=str(p_isin)).all()
        liste_managers = [m.uid for m in res]
        return liste_managers

    def add_portofolio(self, uid, p_isin):
        # vérifie si le portefeuille n'est pas déjà géré
        check = self.session.query(GestionMd).filter_by(uid=uid,p_isin=str(p_isin)).first()
        if check is None:
            row = GestionMd(uid=uid, p_isin=str(p_isin))
            self.session.add(row)
            try:
                self.session.commit()
            except:
                self.session.rollback()

    def delete_portofolio(self, uid, p_isin):
        # vérifie si le portefeuille est géré
        row = self.session.query(GestionMd).filter_by(uid=uid, p_isin=str(p_isin)).first()
        if row is not None:
            self.session.delete(row)
            try:
                self.session.commit()
            except:
                self.session.rollback()

if __name__ == '__main__':
    print 'tous les tests ont été réalisés'
    # g = Gestion()
    # col = g.portefeuille_of_manager(1)
    # col = g.manager_of_portefeuille(1)
    # g.add_portofolio(1,200300)
    # g.delete_portofolio(1,100200)
    # for el in col:
    #     print el.uid