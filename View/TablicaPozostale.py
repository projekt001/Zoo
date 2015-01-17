from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia
from Tablica import Tablica


class TablicaPozostale(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaPozostale, self).__init__(kontroler, parent)
        
        if self.pobierzInformacjeOTabeli(nazwaTabeli, ["Id"]):
            self.generacjaTabeli()

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
            
class TablicaPozostaleZagrody(Tablica):
    def __init__(self, kontroler, nazwaTabeli, parent):
        super(TablicaPozostaleZagrody, self).__init__(kontroler, parent)
         
        if self.pobierzInformacjeOTabeli(nazwaTabeli, ["Id"]):
            self.przystosujOpisZagrody();
            self.generacjaTabeli()
    

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    
    def przystosujOpisZagrody(self):
        
        self.daneZwierzeta = self.kontroler.laczTabele("ZAGRODY");
        
        komenda  = "SELECT ZAGRODY.*, TYPY_ZAGROD.Nazwa_Typ_Zagrody FROM ZAGRODY " + \
                   "LEFT JOIN TYPY_ZAGROD " + \
                   "ON ZAGRODY.TYPY_ZAGROD_Id = TYPY_ZAGROD.Id"
                   
        szukanyNaglowek = "TYPY_ZAGROD_Id"
        

        
        for indexWiersza in range(len(self.opisZwierzeta)):
            print self.opisZwierzeta[indexWiersza][0];
            if(self.opisZwierzeta[indexWiersza][0] == szukanyNaglowek):
                indexSzukanegoNaglowka = indexWiersza
                print "self.indexSzukanegoNaglowka = " + str(indexSzukanegoNaglowka)
            
        #self.daneZwierzeta
    
