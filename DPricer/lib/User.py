# coding=utf-8
__author__ = 'F.Marouane'

from ..data.AppModel import UserMd, AppModel
from Gestion import Gestion


class User(object):
    def __init__(self, uname, password):
        md = AppModel()
        self.uname = uname
        self.password = password
        self.nom = ''
        self.prenom = ''
        self.logged = False
        self.uid = None
        self.session = md.get_session()

    def check(self):
        """
        Vérifie si l'utilisateur existe
        :return None or User:
        """
        user = self.session.query(UserMd).filter_by(uname=self.uname, password=self.password).first()
        if user is not None:
            self.logged = True
            self.nom = user.nom
            self.prenom = user.prenom
            self.uid = user.id
        else:
            self.logged = False

    def change_infos(self, mail=None, prenom=None, nom=None):
        dico = dict()
        if mail is not None:
            dico['mail'] = mail
        if prenom is not None:
            dico['prenom'] = prenom
        if nom is not None:
            dico['nom'] = nom
        self.session.query(UserMd).filter_by(id=self.uid).update(dico)
        try:
            self.session.commit()
        except:
            self.session.rollback()

    def user_portfolio(self):
        """
        Charge la liste des portefeuilles gérés par le gestionaire
        (p_isin, nom)
        :return:
        """
        g = Gestion()
        pf_list = g.portefeuille_of_manager(self.uid)
        return pf_list


if __name__ == '__main__':
    u = User('Mero', 'mero')
    print u.user_portfolio()
