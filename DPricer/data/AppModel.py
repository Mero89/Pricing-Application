# coding=utf-8
__author__ = 'F.Marouane'

import DPricer.configure as cfg
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy import *

Base = declarative_base()
target_schema = 'production'
# target_schema = 'public'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AppModel(object):
    __metaclass__ = Singleton

    def __init__(self):
        try:
            create_engine(cfg.pg_dbstring)
        except sqlalchemy.exc.ArgumentError:
            pass
        self.engine = create_engine(cfg.pg_dbstring)
        DeferredReflection.prepare(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_engine(self):
        return self.engine

    def get_session(self):
        return self.session

    def close_session(self):
        self.session.close()

    def start_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()


class CourbeMd(DeferredReflection, Base):
    __tablename__ = 'courbe'
    __table_args__ = {'schema': target_schema}


class ObligationMd(DeferredReflection, Base):
    __tablename__ = 'obligations'
    __table_args__ = {'schema': target_schema}


class EcheancierMd(DeferredReflection, Base):
    __tablename__ = 'echeancier'
    __table_args__ = {'schema': target_schema}


class PanierMd(DeferredReflection, Base):
    __tablename__ = 'panier'
    __table_args__ = {'schema': target_schema}


class PortefeuilleMd(DeferredReflection, Base):
    __tablename__ = 'portefeuille'
    __table_args__ = {'schema': target_schema}


class GestionMd(DeferredReflection, Base):
    __tablename__ = 'gestion'
    __table_args__ = {'schema': target_schema}


class UserMd(DeferredReflection, Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': target_schema}

"""
### Schema de la BDD ###

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
        date_flux INT4,
"""