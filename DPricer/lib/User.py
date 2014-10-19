# coding=utf-8
__author__ = 'F.Marouane'

from DPricer.data.AppModel import UserMd, AppModel
from Gestion import Gestion


class UniqueUser(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(UniqueUser, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class User(object):
    __metaclass__ = UniqueUser
    __number_of_checks__ = 0

    def __init__(self, uname=None, password=None):
        try:
            self.uname = unicode(uname)
            self.password = unicode(password)
        except (TypeError, ValueError):
            self.uname = u''
            self.password = u''
            pass
        self.nom = u''
        self.prenom = u''
        self.logged = False
        self.uid = None

    def check(self):
        """
        Vérifie si l'utilisateur existe
        :return None or User:
        """
        session = AppModel().get_session()
        user = session.query(UserMd).filter_by(uname=self.uname, password=self.password).first()
        if user and self.__number_of_checks__ == 0:
            self.logged = True
            self.nom = user.nom
            self.prenom = user.prenom
            self.uid = user.id
            self.__number_of_checks__ += 1
        else:
            self.logged = False

    def change_infos(self, uname=None, prenom=None, nom=None):
        dico = dict()
        if uname is not None:
            dico['uname'] = unicode(uname)
        if prenom is not None:
            dico['prenom'] = unicode(prenom)
        if nom is not None:
            dico['nom'] = unicode(nom)
        session = AppModel().get_session()
        session.query(UserMd).filter_by(id=self.uid).update(dico)
        try:
            session.commit()
            return 1
        except:
            session.rollback()
            return 0

    def change_password(self, old_pass, new_pass):
        session = AppModel().get_session()
        mypass = session.query(UserMd).get(self.uid)
        if old_pass == unicode(mypass.password):
            session.query(UserMd).filter_by(id=self.uid).update({'password': new_pass})
            session.commit()
            return 1
        else:
            return 0

    def get_infos(self):
        session = AppModel().get_session()
        infos = session.query(UserMd).get(self.uid)
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
    u.check()
