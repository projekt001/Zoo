from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia
from Tablica import Tablica


class TablicaPozostale(Tablica):
    def __init__(self, uchwytDoBazy, kontroler, nazwaTabeli, parent):
        super(TablicaPozostale, self).__init__(uchwytDoBazy, kontroler, parent)
        
        self.generacjaTabeli(nazwaTabeli)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def generacjaTabeli(self, nazwaTabeli):
        opisZwierzeta = self.kontroler.pobierzOpisTabeli(nazwaTabeli)
        elementyDoWykluczenia = ["Id"]
        listaNieDoWyswietlenia, nazwyKolumn = self.kontroler.pobierzWlasciweDane(opisZwierzeta,
                                                                                 elementyDoWykluczenia)
        daneZwierzeta = self.kontroler.pobierzDane(nazwaTabeli)
        
        self.iloscWierszy  = len(daneZwierzeta)
        
        if(self.iloscWierszy > 0):
            self.iloscKolumn   = len(daneZwierzeta[0])
            
            self.setRowCount(self.iloscWierszy + 1)
            self.setColumnCount(self.iloscKolumn + 1 - len(listaNieDoWyswietlenia))
        
            self.setHorizontalHeaderLabels(nazwyKolumn)
            self.listaKluczy = [];
            for indexWiersza in range(self.iloscWierszy):
                self.przesuniecie = 0;
                for indexKolumny in range(self.iloscKolumn):
                    if not (indexKolumny in listaNieDoWyswietlenia):
                        noweZwierze = QtGui.QTableWidgetItem(str(daneZwierzeta[indexWiersza][indexKolumny]))
                        self.setItem(indexWiersza, indexKolumny - self.przesuniecie, noweZwierze)
                    else:
                        self.przesuniecie = self.przesuniecie + 1
                    
            
                przyciskDoEdycji = QtGui.QPushButton(self)
                przyciskDoEdycji.setText('edytuj')
                przyciskDoEdycji.kluczGlowny = daneZwierzeta[indexWiersza][0];
                przyciskDoEdycji.clicked.connect(self.on_pushButton_clicked)
                self.setCellWidget(indexWiersza, self.iloscKolumn - 1, przyciskDoEdycji)
                
    def przyciskPozywienia(self):
        przyciskDodania = QtGui.QPushButton(self)
        przyciskDodania.setText('dodaj')
        przyciskDodania.clicked.connect(self.dodajPozywienia)
        self.setCellWidget(self.iloscWierszy, self.iloscKolumn - self.przesuniecie, przyciskDodania)
            
    def dodajPozywienia(self):
        widget = self.item(self.iloscWierszy, self.iloscKolumn - self.przesuniecie - 1)
        print widget.text()
        
    def on_pushButton_clicked(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzenia();
        self.dialogTextBrowser.exec_()