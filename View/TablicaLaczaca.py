from PyQt4 import QtCore
from PyQt4 import QtGui


class TablicaLaczaca(QtGui.QTableWidget):
    def __init__(self, 
                 kontroler, 
                 kluczLewaTabela, 
                 kluczPrawaTabela,
                 nazwaTabeli, 
                 nazwaTabeliPrawej,  
                 nazwaTabeliLewej,
                 parent = None):
        
        QtGui.QTableWidget.__init__(self, parent)
        self.kontroler = kontroler
        self.kluczLewaTabela = kluczLewaTabela
        self.kluczPrawaTabela = kluczPrawaTabela
        self.nazwaTabeliPrawej = nazwaTabeliPrawej
        self.nazwaTabeliLewej = nazwaTabeliLewej
        self.nazwaTabeli = nazwaTabeli
        
        
        
    def pobierzDane(self):
        self.opisZwierzeta = self.kontroler.pobierzOpisTabeli(self.nazwaTabeli)
        self.dane = self.kontroler.laczIFiltruj(self.nazwaTabeli,
                                                [[self.nazwaTabeliPrawej, 
                                                self.kluczPrawaTabela, "Id"]],
                                                self.kluczLewaTabela,
                                                self.nazwaTabeli,
                                                "ZWIERZETA_Id")

        
    def ustawRozmiar(self, iloscWierszy, iloscKolumn):
        self.setRowCount(iloscWierszy)
        self.setColumnCount(iloscKolumn)
        
    def wyswietlTablice(self):
        
        self.pobierzDane()
        
        print "MMMMMMMMMMMMM " + str(self.dane)
        self.iloscWierszy = len(self.dane) 
        self.ustawRozmiar(self.iloscWierszy + 1, 2)
    
        for indexWiersza in range(self.iloscWierszy):
            nowyItem = QtGui.QTableWidgetItem(str(self.dane[indexWiersza][4]))
            self.setItem(indexWiersza, 0, nowyItem)
            
            self.dodajPrzyciskUsuniecia(indexWiersza)
            
        self.dodajComboBox()
        
        przyciskUsuniecia = QtGui.QPushButton(self)
        przyciskUsuniecia.setText('dodaj')
        przyciskUsuniecia.clicked.connect(self.dodaj)
        self.setCellWidget(self.iloscWierszy, 1, przyciskUsuniecia)
            
    
            
    def dodajComboBox(self):
        comboBox = QtGui.QComboBox()
        
        dane = self.kontroler.pobierzDane("POZYWIENIA")
        for indexDodawania in range(len(dane)):
            comboBox.addItem(str(dane[indexDodawania][1]))
                
        self.setCellWidget(self.iloscWierszy, 0, comboBox)
        
    def dodajPrzyciskUsuniecia(self,
                               indexWiersza):
        przyciskUsuniecia = QtGui.QPushButton(self)
        przyciskUsuniecia.setText('usun')
        przyciskUsuniecia.kluczGlowny = self.dane[indexWiersza][0]
        przyciskUsuniecia.clicked.connect(self.usun)
        self.setCellWidget(indexWiersza, 1, przyciskUsuniecia)
        
    def usun(self):
        sender = self.sender()

        self.kontroler.usunWiersz(self.nazwaTabeli,
                                  sender.kluczGlowny)
        self.odswierz()
        
    def dodaj(self):
        self.listaDoZapisania = []
        self.listaDoZapisania.append(str(self.kluczLewaTabela))
        
        comboBox = self.cellWidget(self.iloscWierszy, 0)
        self.listaDoZapisania.append(str(comboBox.currentText()))
            
        self.listaDoZapisania[1] = str(self.kontroler.pobierzIdPoNazwie("POZYWIENIA",
                                                                        "Nazwa_Pozywienia",
                                                                        self.listaDoZapisania[1]))
        print "!!!!!!listaDoZapisania =" + str(self.listaDoZapisania)
            
        self.kontroler.zapiszWBazie(self.nazwaTabeli, 
                                    self.opisZwierzeta, 
                                    self.listaDoZapisania);
        self.odswierz()
        
    def odswierz(self):
        self.ustawRozmiar(0, 0)
        self.wyswietlTablice()


        