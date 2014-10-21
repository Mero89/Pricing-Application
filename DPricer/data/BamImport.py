# coding=utf-8
__author__ = 'F.Marouane'

import urllib2
import threading
import datetime as dt
import DPricer.configure as cfg


class ThreadRetrieve(threading.Thread):
    """
    Classe pour télécharger la courbe BAM en mode multi-thread.
    """
    def __init__(self, jour, mois, an):
        threading.Thread.__init__(self)
        if 0 < jour <= 31:
            self.jour = jour
        if 0 < mois <= 12:
            self.mois = mois
        if an > 1950:
            self.an = an
        self.la_date = dt.datetime(day=self.jour, month=self.mois, year=self.an)

    def run(self):
        """
        Execute la fouille en environnement Threadé.
        :return:
        """
        try:
            self.recupere_taux()
        except urllib2.URLError:
            print 'Connection indisponible'

    def recupere_taux(self):
        """
        récupère la courbe de taux depuis le site de la BAM.
        :return:
        """
        request = 'http://www.bkam.ma/wps/PA_1_G_15H/LoadOperationMarMon?dateDe={j}/{m}/{a}&locale=fr'
        delta = dt.timedelta()
        # si la_date est lundi, la requete pointe vers le Vendredi d'avant
        if self.la_date.weekday() == 0:
            delta = dt.timedelta(days=3)
        # Si un jour ouvrable de la semaine, la requete pointe vers le jour d'avant
        elif self.la_date.weekday() in range(1,5):
            delta = dt.timedelta(days=1)
        date_req = self.la_date - delta
        req = request.format(j=date_req.day, m=date_req.month, a=date_req.year)
        # enregistre le fichier Excel avec le nom et date d'évaluation
        filename = cfg.repo_path + '/TauxBAM-{j}-{m}-{a}.xls'.format(j=self.jour, m=self.mois, a=self.an)
        u = urllib2.urlopen(req)
        f = open(filename, 'wb')
        f.write(u.read())
        f.close()
        u.close()
            # try:
            # u = urllib2.urlopen(req)
            # except ValueError:
            #     print 'Valeur de date inconnue'
            # try:
            #     f = open(filename, 'wb')
            #     f.write(u.read())
            #     f.close()
            #     u.close()
            # except IOError:
            #     f.close()
            #     u.close()
            #     print 'lecture impossible du fichier Excel'


def batch_recupere(j, m, a, jj, mm, aa):
    """
    télécharge un ensemble de fichiers entre deus dates données.
    :param j: int
    :param m: int
    :param a: int
    :param jj: int
    :param mm: int
    :param aa: int
    :return:
    """
    start = dt.datetime(year=a, month=m, day=j)
    delta = dt.timedelta(days=1)
    end = dt.datetime(year=aa, month=mm, day=jj)
    if end.date() > dt.datetime.now().date():
        end = dt.datetime.now()
    while start <= end:
        if start.weekday() in range(5):
            TR = ThreadRetrieve(start.day, start.month, start.year)
            TR.start()
            TR.join()
        start += delta


if __name__ == '__main__':
    print 'Test begins here'