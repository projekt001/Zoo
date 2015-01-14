from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia
from Tablica import Tablica


class TablicaPozostale(Tablica):
    def __init__(self, uchwytDoBazy, kontroler, parent):
        super(TablicaPozostale, self).__init__(uchwytDoBazy, kontroler, parent)
        self.generacjaTabeli()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
    def generacjaTabeli(self):
        opisZwierzeta = self.pobierzOpisTabeli("ZWIERZETA")
        elementyDoWykluczenia = ["Id"]
        listaNieDoWyswietlenia, nazwyKolumn = self.pobierzWlasciweDane(opisZwierzeta,
                                                                       elementyDoWykluczenia)
        daneZwierzeta = self.pobierzDane("ZWIERZETA")
        
        iloscWierszy  = len(daneZwierzeta)
        
        
        
        if(iloscWierszy > 0):
            iloscKolumn   = len(daneZwierzeta[0])
            
            self.setRowCount(iloscWierszy + 1)
            self.setColumnCount(iloscKolumn + 1 - len(listaNieDoWyswietlenia))
        
            self.setHorizontalHeaderLabels(nazwyKolumn)
            self.listaKluczy = [];
            for indexWiersza in range(iloscWierszy):
                przesuniecie = 0;
                for indexKolumny in range(iloscKolumn):
                    if not (indexKolumny in listaNieDoWyswietlenia):
                        noweZwierze = QtGui.QTableWidgetItem(str(daneZwierzeta[indexWiersza][indexKolumny]))
                        self.setItem(indexWiersza, indexKolumny - przesuniecie, noweZwierze)
                    else:
                        przesuniecie = przesuniecie + 1
                    
            
                przyciskDoEdycji = QtGui.QPushButton(self)
                przyciskDoEdycji.setText('edytuj')
                przyciskDoEdycji.kluczGlowny = daneZwierzeta[indexWiersza][0];
                przyciskDoEdycji.clicked.connect(self.on_pushButton_clicked)
                self.setCellWidget(indexWiersza, iloscKolumn - 1, przyciskDoEdycji)
            
                
            przyciskDodania = QtGui.QPushButton(self)
            przyciskDodania.setText('dodaj')
            przyciskDodania.kluczGlowny = -1;
            przyciskDodania.clicked.connect(self.on_pushButton_clicked)
            self.setCellWidget(iloscWierszy, iloscKolumn - przesuniecie, przyciskDodania)