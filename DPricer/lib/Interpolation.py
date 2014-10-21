# coding=utf-8
__author__ = 'marouane'

import numpy as np
from scipy.interpolate import interp1d


class Interpol(object):
    """
    Classe qui retourne le taux correspondant à la maturité fournie.
    """
    def __init__(self, liste_taux, liste_maturite):
        """
        Initialise la liste taux et la liste des maturités.
        :type liste_taux: list
        :type liste_maturite: list
        """
        self.liste_taux = liste_taux
        self.liste_maturite = liste_maturite

    def i_lineaire(self, cible):
        """
        Méthode qui retourne le taux d'actualisation par interpolation linéaire.
        :type cible: float
        :return: float
        """
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y)
        return float(fl(cible))

    def i_quadratique(self, cible):
        """
        Méthode qui retourne le taux d'actualisation par interpolation quadratique.
        :type cible: float
        :return: float
        """
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y, kind='quadratic')
        return float(fl(cible))

    def i_spline(self, cible):
        """
        Méthode qui retourne le taux d'actualisation par interpolation en Spline Cubiques.
        :type cible: float
        :return: float
        """
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y, kind='cubic')
        return float(fl(cible))
