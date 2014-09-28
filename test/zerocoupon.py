# coding=utf-8
__author__ = 'F.Marouane'

from math import sqrt, pow
from DPricer.lib.Courbe import Courbe


def price(tf, ta, p):
    px = []
    for i in range(1, p):
        px.append(tf/pow((1+ta), i))
    else:
        px.append((1+tf)/pow(1+ta, p))
    return sum(px)


def price_zc(tf, zc_list):
    px = []
    for zc in list(enumerate(zc_list, 1)):
        print zc[0], '<==>', zc[1]
        px.append(tf/pow((1+zc[1]), zc[0]))
    return sum(px)


def main():
    'cible = 3.353674'
    c = Courbe('15/9/2014')
    tf = .05
    zc1 = [c.taux_lineaire(365)]
    px = price(tf, c.taux_lineaire(730), 2)
    inter = px - (tf/(1+zc1[0]))
    print inter
    inter_zc = px - price_zc(tf, zc1)
    print inter_zc
    zc2 = pow((1+tf)/inter, 1./2) - 1
    # z2 = price_zc(tf, zc1)
    # print z2*100
    print 'px => ', px, 'taux 2ANS =>', c.taux_lineaire(730)
    print zc2 * 100
    print c.zero_coupon()



if __name__ == '__main__':
    main()
