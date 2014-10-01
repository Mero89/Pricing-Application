# coding=utf-8
__author__ = 'F.Marouane'

from decimal import *
import xlrd
import os
from DPricer.data.AppModel import AppModel, CourbeMd, ObligationMd
import datetime as dt
import xlwt


### Procédures Courbe de Taux BAM  ###

def read_courbe_bam(path_to_file):
    """
    retourne une liste de lignes contenues dans le fichier BAM d'excel
    :param path_to_file:
    :return:
    """
    if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
        try:
            wbook = xlrd.open_workbook(path_to_file)
            sheet = wbook.sheet_by_index(0)
            f_row = 4  # n-1, index starts from 0
            num_rows = sheet.nrows - f_row
            a = list()
            for i in range(num_rows - 1):
                a.append([str(r) for r in sheet.row_values(i + 4)])
            for el in a:
                el[2] = Decimal(el[2][:-1].replace(',', '.')) / 100
            # retourne une liste de rows
            # row => (date_valeur, transactions, taux_pondere, date_echeance)
            return a
        except IOError:
            print 'le fichier est introuvable'


def get_date_courbe(path_to_file):
    date_transaction = get_date_transaction(path_to_file)
    if date_transaction.weekday() == 4:
        delta = dt.timedelta(days=3)
    else:
        delta = dt.timedelta(days=1)
    # retourne la date figurant dans le fichier +1 jour
    return date_transaction + delta


def get_date_transaction(path_to_file):
    try:
        wbook = xlrd.open_workbook(path_to_file)
    except IOError:
        print 'Erreur fichier introuvable'
        return None
    sheet = wbook.sheet_by_index(0)
    cel = sheet.cell(1, 0).value
    date_transaction = dt.datetime.strptime(cel.split(':')[1], '%d/%m/%Y')
    return date_transaction


def is_exists(_date):
    """
    Vérifie si la courbe de taux existe déjà dans la BDD
    :param _date:
    :return:
    """
    md = AppModel()
    session = md.get_session()
    existe = session.query(CourbeMd).filter_by(date_req=_date).first()
    return existe


def commit_courbe_bam(excel_path, _date=None):
    """
    Enregistre la courbe de taux BAM dans la base de données
    :param excel_path: chemin vers le fichier
    :param _date: date de la courbe
    :return:
    """
    if _date is None:
        _date = get_date_courbe(excel_path)
    elif type(_date) is str:
        _date = dt.datetime.strptime(_date, '%d/%m/%Y')
    rows = read_courbe_bam(excel_path)
    d_transaction = get_date_transaction(excel_path)
    md = AppModel()
    session = md.get_session()
    existe = is_exists(_date)
    if existe is None:
        if rows != list():
            for rw in rows:
                courbe = CourbeMd()
                courbe.date_req = _date
                courbe.date_echeance = rw[0]
                courbe.transactions = rw[1]
                courbe.taux_pondere = rw[2]
                courbe.date_valeur = rw[3]
                courbe.date_transaction = d_transaction
                session.add(courbe)
            try:
                session.commit()
            except ValueError:
                return False


def list_excel_files(path_to_folder):
    """
    retourne une liste de fichiers excels sous forme de liste.
    :param path_to_folder:
    :return: list():
    """
    pf = path_to_folder
    liste_dir = os.listdir(pf)
    liste_excel = list()
    for elm in liste_dir:
        ext = os.path.splitext(elm)[1]
        if ext == '.xls' or ext == '.xlsx':
            liste_excel.append(elm)
    return liste_excel


### Procédure pour importer liste d'actifs depuis Excel  ###

def import_obligation(excel_path):
    """
    Importe le portefeuille depuis le fichier Excel vers la base de données
    :param excel_path: chemin du fichier Excel
    :return:
    """
    if os.path.exists(excel_path):
        # parcoure le fichier Excel
        try:
            xlrd.open_workbook(excel_path)
        except IOError:
            pass
        wbook = xlrd.open_workbook(excel_path, encoding_override='utf-8')
        sheet = wbook.sheet_by_name('Portfolio')
        start_row = 1
        a = list()
        for i in range(start_row, sheet.nrows - 1):
            a.append(sheet.row_values(i))
        for row in a:
            if row[5] != '' and row[6] != '' and row[7] != '':
                d_em = xlrd.xldate_as_tuple(int(row[5]), wbook.datemode)
                d_js = xlrd.xldate_as_tuple(int(row[6]), wbook.datemode)
                d_ech = xlrd.xldate_as_tuple(int(row[7]), wbook.datemode)
                row[5] = dt.date(year=d_em[0], month=d_em[1], day=d_em[2])
                row[6] = dt.date(year=d_js[0], month=d_js[1], day=d_js[2])
                row[7] = dt.date(year=d_ech[0], month=d_ech[1], day=d_ech[2])
            if type(row[1]) is type(str) and row[1] != '':
                row[1] = str(int(row[1]))

        # enregistre Les données
        md = AppModel()
        session = md.get_session()
        for rw in a:
            if rw[1] != '' and rw[0] != '':
                oblig = ObligationMd()
                oblig.isin = rw[0]
                oblig.nom = rw[1]
                oblig.nominal = rw[2]
                oblig.taux_facial = rw[3]
                oblig.spread = rw[4]
                oblig.date_emission = rw[5]
                oblig.date_jouissance = rw[6]
                oblig.maturite = rw[7]
                oblig.type = rw[8]
                session.add(oblig)
                try:
                    session.commit()
                except Exception:
                    session.rollback()


### Générer le fichier Template d'excel ###

def create_template(path, filename):
    if os.path.exists(path):
        w = xlwt.Workbook(encoding='utf-8')
        s = w.add_sheet('Exemple')
        row = s.row(0)
        style = xlwt.easyxf('font: name Menlo, bold True, height 280, colour blue;')
        warning = xlwt.easyxf('font: name Menlo, bold True, height 320, colour red;'
                              'alignment: vertical top, wrap True')

        row.write(0, 'Code ISIN', style)
        row.write(1, 'NOM', style)
        row.write(2, 'Nominal', style)
        row.write(3, 'Taux Facial', style)
        row.write(4, 'Spread', style)
        row.write(5, 'Date emission', style)
        row.write(6, 'Date de jouissance', style)
        row.write(7, 'Date echeance', style)
        row.write(8, 'Type', style)
        s.write_merge(0, 4, 10, 14,
                      'Pour le type mettre sans faute un des choix suivants: < N >, < AMC >, <REV>, < AMCRev >',
                      warning)
        final_path = os.path.join(path, filename)
        w.save(final_path)


### Exporter données vers Excel ###
def export_to_excel(headers, data, path, filename):
    """
    :param headers: list
    :param data: list
    :param path: path
    :return: excel file
    """
    header_style = xlwt.easyxf('font: name Menlo, bold True, height 280, colour blue;')
    if os.path.exists(path):
        w = xlwt.Workbook()
        s = w.add_sheet('Export')
        row = s.row(0)
        ### write header ###
        for el in headers:
            idx = headers.index(el)
            row.write(idx, str(el), header_style)
        ### write data ###
        for rw in data:
            row_idx = data.index(rw)+1
            row = s.row(row_idx)
            for col in rw:
                col_idx = rw.index(col)
                row.write(col_idx, col)
        ### save filename on path ###
        final_path = os.path.join(path, filename)
        w.save(final_path)


### tests ###


def test_read_courbe_bam():
    file_path = '/Users/mar/Desktop/pylab/repo/OperationMarSecon.xls'
    a = read_courbe_bam(file_path)
    print a


def print_list(mylist):
    for el in mylist:
        print el


def test_import_obligation():
    # file_path = '/Users/mar/Dropbox/DTM/Projets/Societe Generale/Bond_Pricing_Tool.xls'
    file_path = '/Users/mar/Desktop/Template.xls'
    workbook = xlrd.open_workbook(file_path, encoding_override='utf-8')
    sheet = workbook.sheet_by_name('Portfolio')
    a = list()
    for i in range(1, sheet.nrows - 1):
        a.append(sheet.row_values(i))
    for row in a:
        if row[5] != '' and row[6] != '' and row[7] != '':
            d_em = xlrd.xldate_as_tuple(int(row[5]), workbook.datemode)
            d_js = xlrd.xldate_as_tuple(int(row[6]), workbook.datemode)
            d_ech = xlrd.xldate_as_tuple(int(row[7]), workbook.datemode)
            row[5] = dt.date(year=d_em[0], month=d_em[1], day=d_em[2])
            row[6] = dt.date(year=d_js[0], month=d_js[1], day=d_js[2])
            row[7] = dt.date(year=d_ech[0], month=d_ech[1], day=d_ech[2])
        if type(row[1]) is type(str) and row[1] != '':
            row[1] = str(int(row[1]))
    print_list(a)


def main():
    repo = '/Users/mar/PycharmProjects/DPricer/DPricer/data/repository'
    xcl_files = list_excel_files(repo)
    for xcl in xcl_files:
        full_path = os.path.join(repo, xcl)
        commit_courbe_bam(full_path)


def test():
    dd = get_date_courbe('/Users/mar/PycharmProjects/DPricer/DPricer/data/repository/TauxBAM-28-8-2014.xls')
    print dd


if __name__ == '__main__':
    create_template('/users/mar/Desktop')