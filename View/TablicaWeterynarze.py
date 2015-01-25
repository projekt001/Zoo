from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaWeterynarze
from Tablica import Tablica

class WeterynarzeComboBox(QtGui.QComboBox):
    def __init__(self, parent = None):
        super(WeterynarzeComboBox, self).__init__(parent)
    def pobierzTekst(self):
        return self.currentText()

class WeterynarzeQLineEdit(QtGui.QLineEdit):
    def __init__(self, tekst, parent = None):
        super(WeterynarzeQLineEdit, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()
    
class WeterynarzeQTableWidget(QtGui.QTableWidgetItem):
    def __init__(self, tekst, parent = None):
        super(WeterynarzeQTableWidget, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()
        
class TablicaWeterynarze(Tablica):
    def __init__(self, kontenerZakladek, kontroler, nazwaTabeli, parent):
        super(TablicaWeterynarze, self).__init__(kontroler, parent)
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id"])
        self.przystosujNazwyKolumn()
        self.pobierzDane()
        self.pobierzIndeksyDoWyswietlenia()
        self.kontenerZakladek = kontenerZakladek
        if self.pobierzWymiary():
            self.generacjaTabeli()
            
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    
    def przystosujNazwyKolumn(self):
        self.nazwyKolumn[3] = "Specjalizacja"
        
    def pobierzDane(self):
        self.daneTabeli = self.kontroler.laczIPobierzWszystkie("WETERYNARZE",
                                                              [["SPECJALIZACJE", "SPECJALIZACJE_Id", "Id"]])
    def pobierzIndeksyDoWyswietlenia(self):
        self.listaDoWyswietlenia = [1, 2, 3, 6]
        
    def generacjaTabeli(self):
        
        self.ustawRozmiar(self.iloscWierszy + 1, 
                          len(self.listaDoWyswietlenia) + 2)
    
        self.setHorizontalHeaderLabels(self.nazwyKolumn)

        for indexWiersza in range(self.iloscWierszy):
            przesuniecie = 0;
            wlasciwyIndexKolumny = 0;
            for indexKolumny in range(self.iloscKolumn):
                if indexKolumny in self.listaDoWyswietlenia:
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneTabeli[indexWiersza][indexKolumny]))
                    self.setItem(indexWiersza, wlasciwyIndexKolumny, noweZwierze)
                    wlasciwyIndexKolumny = wlasciwyIndexKolumny + 1
                
            
            self.dodajPrzyciskEdycji(indexWiersza)
            self.dodajPrzyciskUsuniecia(indexWiersza)
            
        self.dodajComboBox("SPECJALIZACJE", 3)
        
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.clicked.connect(self.dodajWiersz)
        self.setCellWidget(self.iloscWierszy, len(self.listaDoWyswietlenia), przyciskDodania)
        
    def dodajComboBox(self, nazwaTabeli, indexKolumny):
        comboBox = QtGui.QComboBox()
        
        dane = self.kontroler.pobierzDane(nazwaTabeli)
        for indexDodawania in range(len(dane)):
            comboBox.addItem(str(dane[indexDodawania][1]))
                
        self.setCellWidget(self.iloscWierszy, indexKolumny, comboBox)
        
    def dodajPrzyciskUsuniecia(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('usun')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.usunWiersz)
        self.setCellWidget(indexWiersza, len(self.listaDoWyswietlenia) + 1, przyciskDoEdycji)
            
    def dodajPrzyciskEdycji(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('edytuj')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.edytujWiersz)
        self.setCellWidget(indexWiersza, len(self.listaDoWyswietlenia), przyciskDoEdycji)
            
    def dodajWiersz(self):
        self.listaWidgetow = []
        self.listaWidgetow.append(self.item(self.iloscWierszy, 0))
        self.listaWidgetow.append(self.item(self.iloscWierszy, 1))
        self.listaWidgetow.append(self.item(self.iloscWierszy, 2))
        self.listaWidgetow.append(self.cellWidget(self.iloscWierszy, 3))
        
        if( (self.listaWidgetow[0] == None) or 
            (self.listaWidgetow[1] == None) or
            (self.listaWidgetow[2] == None) or
            (self.listaWidgetow[3] == None) ):
            print " pole jest puste"
        else:
            
            self.listaDoZapisania = []
            self.listaDoZapisania.append(str(self.listaWidgetow[0].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[1].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[2].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[3].currentText()))
            
            self.listaDoZapisania[3] = str(self.kontroler.pobierzIdPoNazwie("SPECJALIZACJE",
                                                                            "Nazwa_Specjalizacji",
                                                                            self.listaDoZapisania[3]))
            
            self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                        self.opisTabeli, 
                                        self.listaDoZapisania);
            self.kontenerZakladek.odswierz()
            
    def usunWiersz(self):
        sender = self.sender()
        self.kontroler.usunWiersz(self.nazwaTabeli,
                                  sender.kluczGlowny)
        self.kontenerZakladek.odswierz()
        
    def edytujWiersz(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaWeterynarze(sender.kluczGlowny, 
                                                             self.nazwaTabeli,
                                                             self.nazwyKolumn,
                                                             self.kontroler,
                                                             self.elementyDoWykluczenia,
                                                             self.opisTabeli,
                                                             self);
        self.dialogTextBrowser.generujWidok()
        self.dialogTextBrowser.exec_()
        
    def on_pushButton_clicked(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzenia();
        self.dialogTextBrowser.exec_()
        
    def odswierz(self):
        self.ustawRozmiar(0, 0)
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();