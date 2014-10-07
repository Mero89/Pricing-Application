# coding=utf-8
__author__ = 'F.Marouane'

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from DPricer.presentation.PyuicFiles.Parametres import Ui_Parametres
from DPricer.lib.User import User


class Parametre(QDialog, Ui_Parametres):
    def __init__(self, parent=None):
        super(Ui_Parametres, self).__init__()
        QDialog.__init__(self)
        self.ui = Ui_Parametres()
        self.ui.setupUi(self)
        title = u'Paramètres'
        self.setWindowTitle(title)
        self.me = User('Mero', 'mero')
        self.me.uid = 2
        self.affiche_info_user()
        self.ui.pushButton.clicked.connect(self.change_infos)
        self.ui.pushButton_2.clicked.connect(self.change_password)

    def affiche_info_user(self):
        infos = self.me.get_infos()
        self.ui.nomLineEdit.setText(infos.nom)
        self.ui.prenomLineEdit.setText(infos.prenom)
        self.ui.unameLineEdit.setText(infos.uname)

    def change_infos(self):
        uname = str(self.ui.unameLineEdit.text())
        nom = str(self.ui.nomLineEdit.text())
        prenom = str(self.ui.prenomLineEdit.text())
        st = self.me.change_infos(uname, prenom, nom)
        if st == 1:
            self.tell_status(u'Modifications éffectuées avec succès.')
        elif st == 0:
            self.tell_status(u'Modifications echouées.')

    def change_password(self):
        old_pass = str(self.ui.ancienMotDePasseLineEdit.text())
        nw_pass = str(self.ui.nouveauMotDePasseLineEdit.text())
        if self.pass_matching():
            stat = self.me.change_password(old_pass, nw_pass)
            if stat:
                self.tell_status(u'Le Mot de passe a été mis à jour.')
                # print u'Le Mot de passe a été mis à jour.'
            else:
                self.tell_status(u"L'ancien mot de passe fourni est incorrecte.")
                # print u"L'ancien mot de passe fourni est incorrecte."
                self.ui.ancienMotDePasseLineEdit.clear()
                self.ui.ancienMotDePasseLineEdit.setFocus()
        else:
            self.tell_status(u'Les Mots de passes sont différents.')
            # print u'Les Mots de passes sont différents.'
            self.ui.nouveauMotDePasseLineEdit.setFocus()

    def pass_matching(self):
        if self.ui.nouveauMotDePasseLineEdit.text() == self.ui.verifierMotDePasseLineEdit.text():
            return True
        else:
            return False

    def tell_status(self, status):
        # self.parent.ui.statusbar.showMessage(status, 3200)
        pass
    def keyPressEvent(self, e):
        # define key event
        if e.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = Parametre()
    form.show()
    ap.exec_()