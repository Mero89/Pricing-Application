# coding=utf-8
__author__ = 'F.Marouane'

import urllib2
import threading
import datetime as dt
import DPricer.configure as cfg


class ThreadRetrieve(threading.Thread):
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
        try:
            self.retrieveTaux()
        except urllib2.URLError:
            print 'Connection indisponible'

    def retrieveTaux(self):
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


def batchRetrieve(j, m, a, jj, mm, aa):
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


def test_retrieve_Taux():
    # TR = ThreadRetrieve(21, 8, 2014)
    # TR.start()
    # TR.join()
    batchRetrieve(17, 8, 2014, 22, 8, 2014)

if __name__ == '__main__':
    test_retrieve_Taux()