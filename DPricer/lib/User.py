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

    def change_infos(self, uname=None, prenom=None, nom=None):
        dico = dict()
        if uname is not None:
            dico['uname'] = uname
        if prenom is not None:
            dico['prenom'] = prenom
        if nom is not None:
            dico['nom'] = nom
        self.session.query(UserMd).filter_by(id=self.uid).update(dico)
        try:
            self.session.commit()
            return 1
        except:
            self.session.rollback()
            return 0

    def change_password(self, old_pass, new_pass):
        mypass = self.session.query(UserMd).get(self.uid)
        if old_pass == str(mypass.password):
            self.session.query(UserMd).filter_by(id=self.uid).update({'password': new_pass})
            self.session.commit()
            return 1
        else:
            return 0

    def get_infos(self):
        infos = self.session.query(UserMd).get(self.uid)
        return infos

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
