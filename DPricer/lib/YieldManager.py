# coding=utf-8
__author__ = 'F.Marouane'

import os
import datetime as dt

import DPricer.data.BamImport as Bi
import DPricer.data.Excel as Xl
from DPricer import configure as cfg


class YieldManager(object):
    """
    Classe qui gère les tentatives de connection
    et la fouille de la courbe adéquate.
    """
    def __init__(self, _date=None):
        if _date is not None:
            if type(_date) is str:
                self._date = dt.datetime.strptime(_date, '%d/%m/%Y').date()
            if self._date >= dt.date.today():
                self._date = dt.date.today()
            else:
                self._date = _date
        elif _date is None:
            self._date = dt.date.today()
        self.last_date_from_auto_import = None

    def import_auto(self, _date=None):
        """
        importe un fichier depuis la BAM
        :param _date: datetime.date
        """
        global date_req
        if _date is None:
            date_req = self._date
        elif _date is not None:
            date_req = _date
        max_times = 7  # Nbre Maximal de tentatives de recherche
        delta = dt.timedelta(days=1)
        for i in range(1, max_times):
            self.last_date_from_auto_import = None
            j, m, a = date_req.day, date_req.month, date_req.year
            # nom du fichier téléchargé
            filename = cfg.repo_path + '/' + cfg.filename.format(j=j, m=m, a=a)
            # Telecharge le fichier demandé
            tr = Bi.ThreadRetrieve(jour=j, mois=m, an=a)
            tr.start()
            tr.join()
            # Vérifie le fichier téléchargé
            try:
                test = Xl.read_courbe_bam(filename)
            except IOError:
                pass
            if test != list():  # Stop
                Xl.commit_courbe_bam(filename, _date)
                self.last_date_from_auto_import = date_req
                break
            date_req -= delta

    @staticmethod
    def import_manuel(excel_path):
        """
        importe un fichier manuellement
        :param excel_path: str
        :return:
        """
        Xl.commit_courbe_bam(excel_path)

    def multi_import_auto(self, s_date, e_date):
        """
        importe plusieurs coubes de taux
        :param s_date: datetime.date
        :param e_date: datetime.date
        :return:
        """
        step = dt.timedelta(days=1)
        flag = e_date
        if e_date > dt.date.today():
            flag = dt.date.today()
        while flag >= s_date:
            if flag.weekday() in range(5):
                self.import_auto(flag)
                if self.last_date_from_auto_import is not None:
                    flag = self.last_date_from_auto_import - step

    @staticmethod
    def clean_repository():
        """ Vide le dossier des fichiers Excel """
        repo_path = cfg.repo_path
        xcl_list = Xl.list_excel_files(repo_path)
        for elm in xcl_list:
            full_path = os.path.join(repo_path, elm)
            os.remove(full_path)

if __name__ == '__main__':
    start = dt.date(2014, 8, 1)
    end = dt.date(2014, 8, 16)
    YM = YieldManager()
    YM.clean_repository()
    YM.multi_import_auto(start, end)

