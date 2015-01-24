from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaZwierzeta
from Tablica import Tablica

class ZwierzetaComboBox(QtGui.QComboBox):
    def __init__(self, parent = None):
        super(ZwierzetaComboBox, self).__init__(parent)
    def pobierzTekst(self):
        return self.currentText()

class ZwierzetaQLineEdit(QtGui.QLineEdit):
    def __init__(self, tekst, parent = None):
        super(ZwierzetaQLineEdit, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()
    
class ZwierzetaQTableWidget(QtGui.QTableWidgetItem):
    def __init__(self, tekst, parent = None):
        super(ZwierzetaQTableWidget, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()
        
class TablicaZwierzeta(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaZwierzeta, self).__init__(kontroler, parent)
        
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id"])
        self.przystosujNazwyKolumn()
        self.pobierzDane()
        self.pobierzIndeksyDoWyswietlenia()
        
        if self.pobierzWymiary():
            self.generacjaTabeli()
            
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    
    def przystosujNazwyKolumn(self):
        self.nazwyKolumn[4] = "Gatunek"
        self.nazwyKolumn[5] = "Zagroda"
        
    def pobierzDane(self):
        self.daneTabeli = self.kontroler.laczIPobierzWszystkie("ZWIERZETA",
                                                                  [["GATUNKI", "GATUNEK_Id", "Id"], 
                                                                   ["ZAGRODY", "ZAGRODA_Id", "Id"]])
    def pobierzIndeksyDoWyswietlenia(self):
        self.listaDoWyswietlenia = [1, 2, 3, 4, 8, 10]
        
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
            
        self.dodajComboBox("GATUNKI", 4)
        self.dodajComboBox("ZAGRODY", 5)
        
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
        self.listaWidgetow.append(self.item(self.iloscWierszy, 3))
        
        self.listaWidgetow.append(self.cellWidget(self.iloscWierszy, 4))
        self.listaWidgetow.append(self.cellWidget(self.iloscWierszy, 5))
        
        if( (self.listaWidgetow[0] == None) or 
            (self.listaWidgetow[1] == None) or
            (self.listaWidgetow[2] == None) or
            (self.listaWidgetow[3] == None) or
            (self.listaWidgetow[4] == None) or
            (self.listaWidgetow[5] == None) ):
            print " pole jest puste"
        else:
            
            self.listaDoZapisania = []
            self.listaDoZapisania.append(str(self.listaWidgetow[0].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[1].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[2].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[3].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[4].currentText()))
            self.listaDoZapisania.append(str(self.listaWidgetow[5].currentText()))
            
            self.listaDoZapisania[4] = str(self.kontroler.pobierzIdPoNazwie("GATUNKI",
                                                                            "Nazwa_Gatunku",
                                                                            self.listaDoZapisania[4]))
            
            self.listaDoZapisania[5] = str(self.kontroler.pobierzIdPoNazwie("ZAGRODY",
                                                                            "Nazwa_Zagrody",
                                                                             self.listaDoZapisania[5]))
            
            self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                        self.opisZwierzeta, 
                                        self.listaDoZapisania);
            self.odswierz()
            
    def usunWiersz(self):
        sender = self.sender()
        self.kontroler.usunWiersz(self.nazwaTabeli,
                                  sender.kluczGlowny)
        self.odswierz()
        
    def edytujWiersz(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaZwierzeta(sender.kluczGlowny, 
                                                           self.nazwaTabeli,
                                                           self.nazwyKolumn,
                                                           self.kontroler,
                                                           self.elementyDoWykluczenia,
                                                           self.opisZwierzeta,
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