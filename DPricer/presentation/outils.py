# coding=utf-8
__author__ = 'F.Marouane'

import sys
import datetime as dt

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DPricer.lib.VAN import VAN
from DPricer.lib.Obligation import Obligation
from DPricer.presentation.PyuicFiles.UI_CalculetteFinanciere import Ui_Form


class Calculette(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__()
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.title = 'Outils'
        self.setWindowTitle(self.title)
        self.parent = parent
        # Add some modifs to the form
        self.frequence = dict(Mensuelle=12,
                              Trimestrielle=4,
                              Semestrielle=2)
        self.ui.comboBoxFrequenceCoupon.addItems(self.frequence.keys())
        self.ui.pushButtonObligEval.clicked.connect(self.evalue_obligation)
        self.ui.pushButtonVanEval.clicked.connect(self.evalue_van)

    def validate_float(self, _num):
        if _num == '':
            return 0
        else:
            return float(_num)

    def validate_rate(self, _rate):
        """
        Convert the doubleSpinBox value to a float rate value
        """
        if _rate == '':
            return 0
        else:
            parts = (_rate.split('%')[0]).replace(',', '.')
            return float(parts) / 100

    def convert_qdate(self, _qdate):
        return dt.date(_qdate[0], _qdate[1], _qdate[2])

    def evalue_van(self):
        annuite = self.validate_float(self.ui.LineEditAnnuite.text())
        tx_act = self.validate_float(self.ui.LineEditTauxActualisation.text())
        date_mt = self.convert_qdate(self.ui.DateEditDateAnnuite.date().getDate())
        date_val = self.convert_qdate(self.ui.DateEditDateActualisation.date().getDate())
        van = VAN(annuite, tx_act, date_montant=date_mt, date_valo=date_val)
        self.ui.lineEditVanEval.setText(str(van.evalue()))

    @pyqtSlot()
    def evalue_obligation(self):
        nominal = self.validate_float(self.ui.nominalLineEdit.text())
        tx_facial = self.validate_rate(self.ui.doubleSpinBoxTauxFacial.text())
        tx_act = self.validate_rate(self.ui.doubleSpinBoxTauxActuariel.text())
        spread = self.validate_rate(self.ui.doubleSpinBoxSpread.text())
        date_emission = self.convert_qdate(self.ui.dateEditDateEmission.date().getDate())
        date_jouissance = self.convert_qdate(self.ui.dateEditDateJouissance.date().getDate())
        date_echeance = self.convert_qdate(self.ui.dateEditDateEcheance.date().getDate())
        date_evaluation = self.convert_qdate(self.ui.dateEditDateEvaluation.date().getDate())
        obl = Obligation(nominal, tx_facial, date_emission, date_jouissance, date_echeance,\
                         date_evaluation, spread, tx_act)
        prix = obl.prix()
        self.ui.evaluerLineEdit.setText(str(prix))

if __name__ == '__main__':

    ap = QApplication(sys.argv)
    form = Calculette()
    # form = ImportTaux()
    form.show()
    ap.exec_()