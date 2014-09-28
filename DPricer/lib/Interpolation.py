# coding=utf-8
__author__ = 'marouane'

import numpy as np
from scipy.interpolate import interp1d


class Interpol(object):
    def __init__(self, liste_taux, liste_maturite):
        self.liste_taux = liste_taux
        self.liste_maturite = liste_maturite

    def i_lineaire(self, cible):
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y)
        return float(fl(cible))

    def i_quadratique(self, cible):
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y, kind='quadratic')
        return float(fl(cible))

    def i_spline(self, cible):
        x, y = np.array(self.liste_maturite), np.array(self.liste_taux)
        fl = interp1d(x, y, kind='cubic')
        return float(fl(cible))
