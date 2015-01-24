from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia


class Tablica(QtGui.QTableWidget):
    def __init__(self, kontroler, parent):
        QtGui.QTableWidget.__init__(self, parent)
        self.kontroler = kontroler
        
        
    def pobierzInformacjeOTabeli(self, nazwaTabeli):
        self.nazwaTabeli   = nazwaTabeli
        self.opisTabeli = self.kontroler.pobierzOpisTabeli(self.nazwaTabeli)
        
    def pobierzDaneDoWyswietlenia(self, elementyDoWykluczenia):
        self.elementyDoWykluczenia = elementyDoWykluczenia;
        self.listaNieDoWyswietlenia, self.nazwyKolumn = self.kontroler.pobierzWlasciweDane(self.opisTabeli,
                                                                                           self.elementyDoWykluczenia)
        
    def pobierzWymiary(self):
        self.iloscWierszy  = len(self.daneTabeli)
        if(self.iloscWierszy > 0):
            self.iloscKolumn   = len(self.daneTabeli[0])
            return 1
        else:
            return 0
        
        
        
    def ustawRozmiar(self, iloscWierszy, iloscKolumn):
        self.setRowCount(iloscWierszy)
        self.setColumnCount(iloscKolumn)
        
