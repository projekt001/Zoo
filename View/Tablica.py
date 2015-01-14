from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia


class Tablica(QtGui.QTableWidget):
    def __init__(self, uchwytDoBazy, kontroler, parent):
        QtGui.QTableWidget.__init__(self, parent)
        
        self.uchwytDoBazy      = uchwytDoBazy;
        self.kursorDoBazy      = self.uchwytDoBazy.cursor()
        
    def pobierzOpisTabeli(self, nazwaTabeli):
        komenda = "DESCRIBE " + nazwaTabeli
        self.kursorDoBazy.execute(komenda)
        opisZwierzeta = self.kursorDoBazy.fetchall()
        return opisZwierzeta
    
    def pobierzWlasciweDane(self, opisZwierzeta, elementyDoUsuniecia):
        
        listaDanychDoUsuniecia = []
        nazwyKolumn            = []
        
        liczbaKolumn = len(opisZwierzeta)
        for indexKolumny in range(liczbaKolumn):
            if ( self.znajdzElementWLiscie(elementyDoUsuniecia, opisZwierzeta[indexKolumny][0])):
                listaDanychDoUsuniecia.append(indexKolumny)
            else:
                nazwyKolumn.append(str(opisZwierzeta[indexKolumny][0]))
        return listaDanychDoUsuniecia, nazwyKolumn
                

        
    def pobierzDane(self, nazwaTabeli):
        komenda = "SELECT * FROM " +  nazwaTabeli
        self.kursorDoBazy.execute(komenda)
        daneZwierzeta = self.kursorDoBazy.fetchall()
        #daneZwierzeta = self.konwertujDoListy(daneZwierzeta)
        
        #liczbaWierszy = len(daneZwierzeta)
        #for indexWiersza in range(liczbaWierszy):
            #for idx, indexDanych in enumerate(listaDanychDoUsuniecia):
                #wiersz = daneZwierzeta[indexWiersza]
                #wiersz.pop(indexDanych)
                #daneZwierzeta[indexWiersza] = wiersz
                
        return daneZwierzeta
    
    
    def znajdzElementWLiscie(self, znaczniki, element):
        return [item for item in range(len(znaczniki)) if znaczniki[item] == element]
        
    def konwertujDoListy(self, dane):
        return list(map(self.konwertujDoListy, dane)) if isinstance(dane, (list, tuple)) else dane
    
    def on_pushButton_clicked(self):
        sender = self.sender()
        self.dialogTextBrowser = OknoRozszerzenia();
        self.dialogTextBrowser.exec_()
        
        
        
