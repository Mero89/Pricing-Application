# coding=utf-8


class VAN(object):
    """
    Classe pour calculer la valeur Actuelle Nette d'un flux futur.
    """
    def __init__(self, montant, taux_actualisation, date_valo, date_montant,periode=0):
        self.montant = montant
        self.tx_actualisation = taux_actualisation
        self.date_valo = date_valo
        self.date_montant = date_montant
        self.periode = periode
        self.base = 365
        if date_valo.year % 4 == 0:
            self.base = 366

    def is_valide(self):
        """
        Teste si la date fournie est valide.
        :return: bool
        """
        if self.date_montant > self.date_valo:
            return True
        elif self.date_montant <= self.date_valo:
            return False

    def is_actuariel(self):
        """
        Vérifie si le flux sera actualisé en actuariel
        :return: bool
        """
        if (self.date_montant - self.date_valo).days >= 365:
            return True
        elif (self.date_montant - self.date_valo).days < 365:
            return False

    def evalue(self):
        """
        Evalue la VAN du flus désiré.
        :return: float
        """
        if not self.is_valide():
            return 0
        elif self.is_valide():
            if self.is_actuariel():
                diff = float((self.date_montant - self.date_valo).days)
                value = self.montant * pow(1+self.tx_actualisation,-diff/self.base)
                return value
            elif not self.is_actuariel():
                diff = float((self.date_montant - self.date_valo).days)
                value = self.montant / (1 + (self.tx_actualisation*diff/self.base))
                return value