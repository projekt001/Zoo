from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia


class Tablica(QtGui.QTableWidget):
    def __init__(self, kontroler, parent):
        QtGui.QTableWidget.__init__(self, parent)
        self.kontroler         = kontroler
        
        
    def pobierzInformacjeOTabeli(self, nazwaTabeli):
        self.nazwaTabeli = nazwaTabeli
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
          
          
    def generacjaTabeli(self):

        self.ustawRozmiar(self.iloscWierszy + 1, 
                          self.iloscKolumn + 1 - len(self.listaNieDoWyswietlenia))
    
        self.setHorizontalHeaderLabels(self.nazwyKolumn)
        for indexWiersza in range(self.iloscWierszy):
            self.przesuniecie = 0;
            for indexKolumny in range(self.iloscKolumn):
                if not (indexKolumny in self.listaNieDoWyswietlenia):
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneZwierzeta[indexWiersza][indexKolumny]))
                    noweZwierze.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.setItem(indexWiersza, indexKolumny - self.przesuniecie, noweZwierze)
                else:
                    self.przesuniecie = self.przesuniecie + 1
            print "indexWiersza" + str(indexWiersza)
            self.przyciskEdycji(indexWiersza)

        self.przyciskDodaniaWiersza();
           
                           
    def przyciskDodaniaWiersza(self):
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.clicked.connect(self.dodajWiersz)
        self.setCellWidget(self.iloscWierszy, self.iloscKolumn - self.przesuniecie, przyciskDodania)
            
    def dodajWiersz(self):
        widget = self.item(self.iloscWierszy, 
                           self.iloscKolumn - self.przesuniecie - 1)

        self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                    self.opisZwierzeta, 
                                    [widget.text()]);
        self.odswierz()
        
    def odswierz(self):
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();
        
        
    def ustawRozmiar(self, iloscWierszy, iloscKolumn):
        self.setRowCount(iloscWierszy)
        self.setColumnCount(iloscKolumn)
        
