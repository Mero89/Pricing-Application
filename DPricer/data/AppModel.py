# coding=utf-8
__author__ = 'F.Marouane'

import DPricer.configure as cfg
import sqlalchemy
from sqlalchemy import Integer, Column, Date, Float, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection


Base = declarative_base()
# target_schema = 'production'
target_schema = 'VAR'


class Singleton(type):
    """
    Représente la classe Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Retourne le Meme objet si celui-ci hérite du singleton.
        :type args: list
        :type kwargs: dict
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AppModel(object):
    """
    Classe qui gère les opérations de la BDD.
    Utilise SqlAlchemy comme back-end.
    """
    __metaclass__ = Singleton
    __session__ = {}

    def __init__(self):
        try:
            sqlalchemy.create_engine(cfg.pg_dbstring)
        except sqlalchemy.exc.ArgumentError:
            pass
        self.engine = sqlalchemy.create_engine(cfg.pg_dbstring)
        DeferredReflection.prepare(self.engine)
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

    def get_engine(self):
        """
            retourne l'engine utilisé pour la connection à la BDD.
        """
        return self.engine

    def get_session(self):
        """
            retourne la session instanciée.
        """
        if 'session' not in self.__session__:
            self.__session__['session'] = self.session
        return self.__session__['session']

    def close_session(self):
        """
            Ferme la session du Modele
        """
        self.session.close()

    def start_session(self):
        """
        retourne un nouvel objet session.
        """
        session_maker = sessionmaker(bind=self.engine)
        return session_maker()


class CourbeMd(Base):
    """
    Classe de la table Courbe.
    """
    __tablename__ = 'courbe'
    __table_args__ = {'schema': target_schema}

    id = Column(Integer, primary_key=True)
    date_req = Column(Date)
    transactions = Column(String)
    date_echeance = Column(Date)
    date_valeur = Column(Date)
    taux_pondere = Column(Float)
    date_transaction = Column(Date)


class ObligationMd(Base):
    """
        Classe de la table Obligations.
    """
    __tablename__ = 'obligations'
    __table_args__ = {'schema': target_schema}

    isin = Column(String(15), primary_key=True)
    nom = Column(String(200))
    nominal = Column(Float)
    taux_facial = Column(Float)
    date_emission = Column(Date)
    date_jouissance = Column(Date)
    maturite = Column(Date)
    spread = Column(Float)
    type = Column(String(25))
    echue = Column(sqlalchemy.Boolean)
    forcee = Column(sqlalchemy.Boolean)
    # echeancier = relationship('EcheancierMd', backref='ObligationMd')


class EcheancierMd(Base):
    """
    Classe de la table Echeancier.
    """
    __tablename__ = 'echeancier'
    __table_args__ = {'schema': target_schema}

    id = Column(Integer, primary_key=True)
    isin = Column(String(15), sqlalchemy.ForeignKey(ObligationMd.isin))
    amortissement = Column(Float)
    coupon = Column(Float)
    date_coupon = Column(Date)


class PortefeuilleMd(Base):
    """
    Classe de la table Portefeuille.
    """
    __tablename__ = 'portefeuille'
    __table_args__ = {'schema': target_schema}

    p_isin = Column(String(15), primary_key=True)
    nom = Column(String(120))
    isin_mcl = Column(String(30))
    categorie = Column(String(20))
    valeur_liquidative = Column(Float)


class UserMd(Base):
    """
    Classe de la table Users.
    """
    __tablename__ = 'users'
    __table_args__ = {'schema': target_schema}

    id = Column(Integer, primary_key=True)
    uname = Column(String(100))
    password = Column(String(40))
    mail = Column(String(50))
    prenom = Column(String(40))
    nom = Column(String(40))


class PanierMd(Base):
    """
    Classe de la table Panier.
    """
    __tablename__ = 'panier'
    __table_args__ = {'schema': target_schema}

    id = Column(Integer, primary_key=True)
    p_isin = Column(String(15), sqlalchemy.ForeignKey(PortefeuilleMd.p_isin))
    isin = Column(String(15), sqlalchemy.ForeignKey(ObligationMd.isin))
    quantite = Column(Integer)


class GestionMd(Base):
    """
    Classe de la table Gestion.
    """
    __tablename__ = 'gestion'
    __table_args__ = {'schema': target_schema}
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, sqlalchemy.ForeignKey(UserMd.id))
    p_isin = Column(String(15), sqlalchemy.ForeignKey(PortefeuilleMd.p_isin))

# Gestion = sqlalchemy.Table('gestion', Base.metadata,
#                            Column('p_isin', String(15), sqlalchemy.ForeignKey('PortefeuilleMd.p_isin')),
#                            Column('uid', Integer, sqlalchemy.ForeignKey('UserMd.id')))


class Benchmark(object):  # Base):
    """
    Classe du benchmark.
    """
    __tablename__ = 'benchmark'
    __table_args__ = {'schema': target_schema}
    id = Column(Integer, primary_key=True)


class Perfs(Base):
    __tablename__= 'perfs'
    __table_args__ = {'schema': target_schema}

    date_observation = Column(Date, primary_key=True)
    p_isin = Column(String(15))
    valeur = Column(Float)