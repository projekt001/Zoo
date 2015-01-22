from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaZwierzeta
from Tablica import Tablica


class TablicaZwierzeta(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaZwierzeta, self).__init__(kontroler, parent)
        
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id"])
        self.pobierzDane()
        
        if self.pobierzWymiary():
            self.generacjaTabeli()
            
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def pobierzDane(self):
        self.daneZwierzeta = self.kontroler.pobierzDane(self.nazwaTabeli)
        
    def generacjaTabeli(self):
        self.ustawRozmiar(self.iloscWierszy + 1, 
                          self.iloscKolumn + 1 - len(self.listaNieDoWyswietlenia))
    
        self.setHorizontalHeaderLabels(self.nazwyKolumn)

        for indexWiersza in range(self.iloscWierszy):
            przesuniecie = 0;
            for indexKolumny in range(self.iloscKolumn):
                if not (indexKolumny in self.listaNieDoWyswietlenia):
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneZwierzeta[indexWiersza][indexKolumny]))
                    self.setItem(indexWiersza, indexKolumny - przesuniecie, noweZwierze)
                else:
                    przesuniecie = przesuniecie + 1
                
        
            przyciskDoEdycji = QtGui.QPushButton(self)
            przyciskDoEdycji.setText('edytuj')
            przyciskDoEdycji.kluczGlowny = self.daneZwierzeta[indexWiersza][0];
            przyciskDoEdycji.clicked.connect(self.edytujKolumne)
            self.setCellWidget(indexWiersza, self.iloscKolumn - przesuniecie, przyciskDoEdycji)
        
            
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.kluczGlowny = -1;
        przyciskDodania.clicked.connect(self.on_pushButton_clicked)
        self.setCellWidget(self.iloscWierszy, self.iloscKolumn - przesuniecie, przyciskDodania)
            
            
    def edytujKolumne(self):
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