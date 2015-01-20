from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzeniaPozostale
from Tablica import Tablica


class TablicaPozostale(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaPozostale, self).__init__(kontroler, parent)
        
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
        przyciskDoEdycji.kluczGlowny = self.daneZwierzeta[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.edytujKolumne)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie, przyciskDoEdycji)
        
    def edytujKolumne(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaPozostale(sender.kluczGlowny, 
                                                           self.nazwaTabeli,
                                                           self.nazwyKolumn,
                                                           self.kontroler,
                                                           self.elementyDoWykluczenia,
                                                           self);
        self.dialogTextBrowser.generujWidok()
        self.dialogTextBrowser.exec_()
    
    def pobierzDane(self):
        self.daneZwierzeta = self.kontroler.pobierzDane(self.nazwaTabeli)
            
class TablicaPozostaleZagrody(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaPozostaleZagrody, self).__init__(kontroler, parent)
            
        self.pobierzInformacjeOTabeli(nazwaTabeli)
        self.pobierzDaneDoWyswietlenia(["Id", "TYPY_ZAGROD_Id"])
        
        self.pobierzDane();
        self.nazwyKolumn.append("Typ Zagrody")
        if self.pobierzWymiary():
            self.generacjaTabeli()
            

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    

    def pobierzDane(self):
        self.daneZwierzeta = self.kontroler.laczTabele("ZAGRODY", 
                                                       "TYPY_ZAGROD", 
                                                       "TYPY_ZAGROD_Id",
                                                       "Id",
                                                       "Nazwa_Typ_Zagrody");
                                                       
    def przyciskEdycji(self, indexWiersza):
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('edytuj')
        przyciskDoEdycji.kluczGlowny = self.daneZwierzeta[indexWiersza][0];
        przyciskDoEdycji.clicked.connect(self.edytujKolumne)
        self.setCellWidget(indexWiersza, self.iloscKolumn - self.przesuniecie, przyciskDoEdycji)
        
    def edytujKolumne(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzeniaPozostale(sender.kluczGlowny, 
                                                           self.nazwaTabeli,
                                                           self.nazwyKolumn,
                                                           self.kontroler,
                                                           self.elementyDoWykluczenia,
                                                           self);
        self.dialogTextBrowser.generujWidok()
        self.dialogTextBrowser.exec_()
