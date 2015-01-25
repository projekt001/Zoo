from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaPozostale
from OknoRozszerzenia import OknoRozszerzeniaZagrody
from Tablica import Tablica


class TablicaPozostale(Tablica):
    def __init__(self, kontenerZakladek, kontroler, nazwaTabeli, parent):
        super(TablicaPozostale, self).__init__(kontroler, parent)
        
        self.kontenerZakladek = kontenerZakladek
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id"])
        self.pobierzDane()
        
        if self.pobierzWymiary():
            self.generacjaTabeli()

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def przyciskEdycji(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('edytuj')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.edytujKolumne)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie, przyciskDoEdycji)
        
    def edytujKolumne(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaPozostale(sender.kluczGlowny, 
                                                           self.nazwaTabeli,
                                                           self.nazwyKolumn,
                                                           self.kontroler,
                                                           self.elementyDoWykluczenia,
                                                           self.opisTabeli,
                                                           self);
        self.dialogTextBrowser.generujWidok()
        self.dialogTextBrowser.exec_()
        
        
    
    def pobierzDane(self):
        self.daneTabeli = self.kontroler.pobierzDane(self.nazwaTabeli)
        
        
    def generacjaTabeli(self):

        self.ustawRozmiar(self.iloscWierszy + 1, 
                          self.iloscKolumn + 2 - len(self.listaNieDoWyswietlenia))
    
        self.nazwyKolumnDoWyswietlenia = self.nazwyKolumn
        self.nazwyKolumnDoWyswietlenia[0] = "Nazwa" 
        self.setHorizontalHeaderLabels(self.nazwyKolumn)
        
        for indexWiersza in range(self.iloscWierszy):
            self.przesuniecie = 0;
            for indexKolumny in range(self.iloscKolumn):
                if not (indexKolumny in self.listaNieDoWyswietlenia):
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneTabeli[indexWiersza][indexKolumny]))
                    noweZwierze.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.setItem(indexWiersza, indexKolumny - self.przesuniecie, noweZwierze)
                else:
                    self.przesuniecie = self.przesuniecie + 1
            self.przyciskEdycji(indexWiersza)
            self.przyciskUsuniecia(indexWiersza)
            
        self.przyciskDodaniaWiersza();
        
        
    def przyciskUsuniecia(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('usun')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.usunWiersz)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie + 1, przyciskDoEdycji) 
                           
    def przyciskDodaniaWiersza(self):
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.clicked.connect(self.dodajWiersz)
        self.setCellWidget(self.iloscWierszy, self.iloscKolumn - self.przesuniecie, przyciskDodania)
            
    def usunWiersz(self):
        sender = self.sender()
        self.kontroler.usunWiersz(self.nazwaTabeli,
                                  sender.kluczGlowny)
        self.kontenerZakladek.odswierz()
        
    def odswierz(self):
        self.ustawRozmiar(0, 0)
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();
        
    def dodajWiersz(self):
        widget = self.item(self.iloscWierszy, 
                           self.iloscKolumn - self.przesuniecie - 1)
        if(widget == None):
            print " pole jest puste"
        else:
            self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                        self.opisTabeli, 
                                        [str(widget.text())]);
            self.kontenerZakladek.odswierz()
            
            
class TablicaPozostaleZagrody(Tablica):
    def __init__(self, kontenerZakladek, kontroler, nazwaTabeli, parent):
        super(TablicaPozostaleZagrody, self).__init__(kontroler, parent)
        
        self.kontenerZakladek = kontenerZakladek
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id", "TYPY_ZAGROD_Id"])
        
        self.pobierzDane();
        self.nazwyKolumn.append("Typ Zagrody")
        if self.pobierzWymiary():
            self.generacjaTabeli()

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def odswierz(self):
        self.ustawRozmiar(0, 0)
        self.usunComboBox()
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();
    
        
    def pobierzDane(self):
        self.daneTabeli = self.kontroler.laczTabele("ZAGRODY", 
                                                       "TYPY_ZAGROD", 
                                                       "TYPY_ZAGROD_Id",
                                                       "Id",
                                                       "Nazwa_Typ_Zagrody");
                                                       
    def przyciskEdycji(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('edytuj')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.edytujKolumne)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie, przyciskDoEdycji)
        
    def edytujKolumne(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaZagrody(sender.kluczGlowny, 
                                                           self.nazwaTabeli,
                                                           self.nazwyKolumn,
                                                           self.kontroler,
                                                           self.elementyDoWykluczenia,
                                                           self.opisTabeli,
                                                           self);
        self.dialogTextBrowser.generujWidok()
        self.dialogTextBrowser.exec_()
        
        
    def generacjaTabeli(self):

        self.ustawRozmiar(self.iloscWierszy + 1, 
                          self.iloscKolumn + 2 - len(self.listaNieDoWyswietlenia))
    
        self.setHorizontalHeaderLabels(self.nazwyKolumn)
        for indexWiersza in range(self.iloscWierszy):
            self.przesuniecie = 0;
            for indexKolumny in range(self.iloscKolumn):
                if not (indexKolumny in self.listaNieDoWyswietlenia):
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneTabeli[indexWiersza][indexKolumny]))
                    noweZwierze.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.setItem(indexWiersza, indexKolumny - self.przesuniecie, noweZwierze)
                else:
                    self.przesuniecie = self.przesuniecie + 1
                    
            self.przyciskUsuniecia(indexWiersza)
            self.przyciskEdycji(indexWiersza)
            
        self.dodajComboBox()
        self.przyciskDodaniaWiersza();
           
    def przyciskUsuniecia(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('usun')
        przyciskDoEdycji.kluczGlowny = self.daneTabeli[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.usunWiersz)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie + 1, przyciskDoEdycji)
         
    def usunWiersz(self):
        sender = self.sender()
        self.kontroler.usunWiersz(self.nazwaTabeli,
                                  sender.kluczGlowny)
        self.odswierz()
        
    def usunComboBox(self):
        self.removeCellWidget(self.iloscWierszy, 2)
        
    def dodajComboBox(self):
        comboBox = QtGui.QComboBox()
        
        dane = self.kontroler.pobierzDane("TYPY_ZAGROD")
        for indexDodawania in range(len(dane)):
                comboBox.addItem(str(dane[indexDodawania][1]))
                
        self.setCellWidget(self.iloscWierszy, 2, comboBox)
        
    def przyciskDodaniaWiersza(self):
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.clicked.connect(self.dodajWiersz)
        self.setCellWidget(self.iloscWierszy, self.iloscKolumn - self.przesuniecie, przyciskDodania)
            
    def dodajWiersz(self):
        self.listaWidgetow = []
        self.listaWidgetow.append(self.item(self.iloscWierszy, 0))
        self.listaWidgetow.append(self.item(self.iloscWierszy, 1))
        self.listaWidgetow.append(self.cellWidget(self.iloscWierszy, 2))
        
        if( (self.listaWidgetow[0] == None) or 
            (self.listaWidgetow[1] == None) or
            (self.listaWidgetow[2] == None) ):
            print " pole jest puste"
        else:
            
            self.listaDoZapisania = []
            self.listaDoZapisania.append(str(self.listaWidgetow[0].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[1].text()))
            self.listaDoZapisania.append(str(self.listaWidgetow[2].currentText()))
            
            self.listaDoZapisania[2] = str(self.kontroler.pobierzIdPoNazwie("TYPY_ZAGROD",
                                                                            "Nazwa_Typ_Zagrody",
                                                                            self.listaDoZapisania[2]))
            
            self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                        self.opisTabeli, 
                                        self.listaDoZapisania);
            self.odswierz()
        
