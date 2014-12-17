# coding=utf-8
__author__ = 'F.Marouane'
import abc


class Person(object):
    def __init__(self, resp=None, est=None):
        self.respect = resp
        self.esteem = est

    def __str__(self):
        return 'This Person has a self.{r} and a self.{e}'.format(r=self.respect, e=self.esteem)


def extrapolate(f_point, l_point, target):
    """
    Retourne la valeur extrapolée de la cible à partir
    des deux derniers points.
    l'extrapolation est linéaire.
    :param f_point: tuple
    :param l_point: tuple
    :param target: float
    :return: float
    """
    dy = l_point[1] - f_point[1]
    dx = l_point[0] - f_point[0]
    try:
        a = float(dy)/dx
    except ZeroDivisionError:
        pass
    b = 0.5 * ((l_point[1] + f_point[1]) - a * (l_point[0] + f_point[0]))
    value = a*target + b
    return value


if __name__ == '__main__':
    # f = Facade()
    # print f._instances
    print 'ok'
