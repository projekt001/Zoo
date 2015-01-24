from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaZwierzeta
from Tablica import Tablica


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
        self.nazwyKolumn[4] = "GATUNEK"
        self.nazwyKolumn[5] = "ZAGRODA"
        
    def pobierzDane(self):
        tabeleDoLaczenia = ["GATUNKI", "ZAGRODY"]
        self.daneZwierzeta = self.kontroler.laczIPobierzWszystkie("ZWIERZETA",
                                                                  [["GATUNKI", "GATUNEK_Id", "Id"], 
                                                                   ["ZAGRODY", "ZAGRODA_Id", "Id"]])
    def pobierzIndeksyDoWyswietlenia(self):
        self.listaDoWyswietlenia = [1, 2, 3, 4, 8, 10]
        
    def generacjaTabeli(self):
        
        self.ustawRozmiar(self.iloscWierszy + 1, 
                          len(self.listaDoWyswietlenia) + 1)
    
        self.setHorizontalHeaderLabels(self.nazwyKolumn)

        for indexWiersza in range(self.iloscWierszy):
            przesuniecie = 0;
            wlasciwyIndexKolumny = 0;
            for indexKolumny in range(self.iloscKolumn):
                if indexKolumny in self.listaDoWyswietlenia:
                    print "indexKolumny" + str(indexKolumny)
                    noweZwierze = QtGui.QTableWidgetItem(str(self.daneZwierzeta[indexWiersza][indexKolumny]))
                    self.setItem(indexWiersza, wlasciwyIndexKolumny, noweZwierze)
                    wlasciwyIndexKolumny = wlasciwyIndexKolumny + 1
                
        
            przyciskDoEdycji = QtGui.QPushButton(self)
            przyciskDoEdycji.setText('edytuj/przegladaj')
            przyciskDoEdycji.kluczGlowny = self.daneZwierzeta[indexWiersza][0];
            przyciskDoEdycji.clicked.connect(self.edytujKolumne)
            self.setCellWidget(indexWiersza, len(self.listaDoWyswietlenia), przyciskDoEdycji)
        
            
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.kluczGlowny = -1;
        przyciskDodania.clicked.connect(self.on_pushButton_clicked)
        self.setCellWidget(self.iloscWierszy, len(self.listaDoWyswietlenia), przyciskDodania)
            
            
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
        
    def odswierz(self):
        self.pobierzDane()
        self.pobierzWymiary()
        self.generacjaTabeli();