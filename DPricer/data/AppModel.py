# coding=utf-8
__author__ = 'F.Marouane'

import DPricer.configure as cfg
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection


Base = declarative_base()
target_schema = 'production'
# target_schema = 'public'


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
        return self.session

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


class CourbeMd(DeferredReflection, Base):
    """
    Classe de la table Courbe.
    """
    __tablename__ = 'courbe'
    __table_args__ = {'schema': target_schema}


class ObligationMd(DeferredReflection, Base):
    """
        Classe de la table Obligations.
    """
    __tablename__ = 'obligations'
    __table_args__ = {'schema': target_schema}


class EcheancierMd(DeferredReflection, Base):
    """
    Classe de la table Echeancier.
    """
    __tablename__ = 'echeancier'
    __table_args__ = {'schema': target_schema}
    actif = relationship("ObligationMd")


class PanierMd(DeferredReflection, Base):
    """
        Classe de la table Panier.
    """
    __tablename__ = 'panier'
    __table_args__ = {'schema': target_schema}
    portefeuille = relationship("PortefeuilleMd")
    actif = relationship("ObligationMd")


class PortefeuilleMd(DeferredReflection, Base):
    """
        Classe de la table Portefeuille.
    """
    __tablename__ = 'portefeuille'
    __table_args__ = {'schema': target_schema}


class GestionMd(DeferredReflection, Base):
    """
    Classe de la table Gestion.
    """
    __tablename__ = 'gestion'
    __table_args__ = {'schema': target_schema}
    user = relationship("UserMd")
    portefeuille = relationship("PortefeuilleMd")

class UserMd(DeferredReflection, Base):
    """
        Classe de la table Users.
    """
    __tablename__ = 'users'
    __table_args__ = {'schema': target_schema}


class MBI(DeferredReflection, Base):
    """
    Classe du benchmark.
    """
    __tablename__ = 'users'
    __table_args__ = {'schema': target_schema}


### Schema de la BDD ###
"""
TABLE courbe :
        PRIMARY KEY (id)
        id SERIAL,
        date_req DATE NOT NULL,
        transactions VARCHAR(20),
        date_echeance DATE,
        date_valeur DATE,
        taux_pondere FLOAT4,

TABLE obligations :
        PRIMARY KEY (isin)
        isin VARCHAR(15) UNIQUE,
        nom VARCHAR(200),
        nominal FLOAT4,
        taux_facial FLOAT4,
        date_emission DATE,
        date_jouissance DATE,
        maturite DATE,
        spread FLOAT4,
        type VARCHAR(25) DEFAULT 'N',
        echue BOOL DEFAULT False,

TABLE panier :
        PRIMARY KEY (id)
        id SERIAL,
        p_isin VARCHAR(15),
        isin VARCHAR(15),

TABLE portefeuille :
        PRIMARY KEY (p_isin)
        p_isin VARCHAR(15) NOT NULL,
        nom VARCHAR(120),

TABLE gestion :
        PRIMARY KEY (id)
        id SERIAL,
        user_id INT4,
        p_isin VARCHAR(15),

TABLE users :
        id SERIAL,
        PRIMARY KEY (id)
        uname VARCHAR(100),
        password VARCHAR(40),
        mail VARCHAR(50),
        prenom VARCHAR(40),
        nom VARCHAR(40),

TABLE echeancier :
        PRIMARY KEY (id)
        id SERIAL,
        isin VARCHAR(15),
        flux FLOAT4,
        date_flux INT4,"""