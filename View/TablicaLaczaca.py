from PyQt4 import QtCore
from PyQt4 import QtGui


class TablicaLaczaca(QtGui.QTableWidget):
    def __init__(self, 
                 kontroler, 
                 wartosciKluczy,
                 nazwyKluczy,
                 nazwyTabeli,
                 nazwa,
                 parent = None):
        
        QtGui.QTableWidget.__init__(self, parent)
        self.kontroler      = kontroler
        self.wartosciKluczy = wartosciKluczy
        self.nazwyTabeli    = nazwyTabeli
        self.nazwyKluczy    = nazwyKluczy
        self.nazwa          = nazwa
        
        
    def pobierzDane(self):
        self.opisZwierzeta = self.kontroler.pobierzOpisTabeli(self.nazwyTabeli[0])
        self.dane = self.kontroler.laczIFiltruj(self.nazwyTabeli[0],
                                                [[self.nazwyTabeli[2], 
                                                  self.nazwyKluczy[1], "Id"]],
                                                self.wartosciKluczy[0],
                                                self.nazwyTabeli[0],
                                                self.nazwyKluczy[0])
        

        
    def ustawRozmiar(self, iloscWierszy, iloscKolumn):
        self.setRowCount(iloscWierszy)
        self.setColumnCount(iloscKolumn)
        
    def wyswietlTablice(self):
        
        self.pobierzDane()
        
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
        
        dane = self.kontroler.pobierzDane(self.nazwyTabeli[2])
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

        self.kontroler.usunWiersz(self.nazwyTabeli[0],
                                  sender.kluczGlowny)
        self.odswierz()
        
    def dodaj(self):
        self.listaDoZapisania = []
        self.listaDoZapisania.append(str(self.wartosciKluczy[0]))
        
        comboBox = self.cellWidget(self.iloscWierszy, 0)
        self.listaDoZapisania.append(str(comboBox.currentText()))
            
        self.listaDoZapisania[1] = str(self.kontroler.pobierzIdPoNazwie(self.nazwyTabeli[2],
                                                                        self.nazwa,
                                                                        self.listaDoZapisania[1]))

        self.kontroler.zapiszWBazie(self.nazwyTabeli[0], 
                                    self.opisZwierzeta, 
                                    self.listaDoZapisania);
        self.odswierz()
        
    def odswierz(self):
        self.ustawRozmiar(0, 0)
        self.wyswietlTablice()


        