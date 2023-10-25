import sys

from PyQt6 import QtWidgets, QtGui

from bmiGui import Ui_BMIFenster

class bmiAnwendung(QtWidgets.QMainWindow, Ui_BMIFenster):
    def __init__(self, parent=None):
        super(bmiAnwendung, self).__init__(parent=parent)
        self.setupUi(self)

    def btn_click(self):
        bmiAnwendung.bmiBerechnen(self)
        self.labelBMAusgabe.setText(str(bmiAnwendung.bmiBerechnen(self)))
        bmiAnwendung.updateBild(self, bmiAnwendung.bmiBerechnen(self))
        pass

    def bmiBerechnen(self):
        gewicht = self.eingabeGewicht.value()
        groesse = self.eingabeGroesse.value() / 100
        bmi = gewicht / (groesse * groesse)
        bmi = round(bmi, 2)
        return bmi

    def updateBild(self, bmi):
        if bmi < 18.5:
            self.labelBild.setPixmap(QtGui.QPixmap("bmiRessourcen/Grenbone.png"))
        elif 18.5 <= bmi < 24.9:
            self.labelBild.setPixmap(QtGui.QPixmap("bmiRessourcen/Grenbone.png"))
        elif 25 <= bmi < 29.9:
            self.labelBild.setPixmap(QtGui.QPixmap("bmiRessourcen/Lama.png"))
        else:
            self.labelBild.setPixmap(QtGui.QPixmap("bmiRessourcen/test.png"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = bmiAnwendung()
    form.show()
    sys.exit(app.exec())
