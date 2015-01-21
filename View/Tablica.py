from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia


class Tablica(QtGui.QTableWidget):
    def __init__(self, kontroler, parent):
        QtGui.QTableWidget.__init__(self, parent)
        self.kontroler = kontroler
        
        
    def pobierzInformacjeOTabeli(self, nazwaTabeli):
        self.nazwaTabeli   = nazwaTabeli
        self.opisZwierzeta = self.kontroler.pobierzOpisTabeli(self.nazwaTabeli)
        
    def pobierzDaneDoWyswietlenia(self, elementyDoWykluczenia):
        self.elementyDoWykluczenia = elementyDoWykluczenia;
        self.listaNieDoWyswietlenia, self.nazwyKolumn = self.kontroler.pobierzWlasciweDane(self.opisZwierzeta,
                                                                                           self.elementyDoWykluczenia)
        
    def pobierzWymiary(self):
        self.iloscWierszy  = len(self.daneZwierzeta)
        if(self.iloscWierszy > 0):
            self.iloscKolumn   = len(self.daneZwierzeta[0])
            return 1
        else:
            return 0
        
    def odswierz(self):
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();
        
        
    def ustawRozmiar(self, iloscWierszy, iloscKolumn):
        self.setRowCount(iloscWierszy)
        self.setColumnCount(iloscKolumn)
        
