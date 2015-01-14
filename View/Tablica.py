from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia

class Tablica(QtGui.QTableWidget):
    def __init__(self, uchwytDoBazy, parent):
        QtGui.QTableWidget.__init__(self, parent)
        
        self.uchwytDoBazy      = uchwytDoBazy;
        self.kursorDoBazy      = self.uchwytDoBazy.cursor()
        
        
        self.generacjaTabeli()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def generacjaTabeli(self):
        opisZwierzeta = self.pobierzOpisTabeli()
        listaNieDoWyswietlenia, nazwyKolumn = self.pobierzDane(opisZwierzeta)
        daneZwierzeta = self.pobierzDaneZwierzat()
        
        iloscWierszy  = len(daneZwierzeta)
        
        
        if(iloscWierszy > 0):
            iloscKolumn   = len(daneZwierzeta[0])
            
            self.setRowCount(iloscWierszy + 1)
            self.setColumnCount(iloscKolumn + 1 - len(listaNieDoWyswietlenia))
        
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
            
            
    def pobierzDane(self, opisZwierzeta):
        znaczniki    = ['Id', ]
        
        listaDanychDoUsuniecia = []
        nazwyKolumn            = []
        
        liczbaKolumn = len(opisZwierzeta)
        for indexKolumny in range(liczbaKolumn):
            if ( self.znajdzElementWLiscie(znaczniki, opisZwierzeta[indexKolumny][0])):
                listaDanychDoUsuniecia.append(indexKolumny)
            else:
                nazwyKolumn.append(str(opisZwierzeta[indexKolumny][0]))
        return listaDanychDoUsuniecia, nazwyKolumn
                
    def pobierzOpisTabeli(self):
        self.kursorDoBazy.execute("DESCRIBE ZWIERZETA")
        opisZwierzeta = self.kursorDoBazy.fetchall()
        return opisZwierzeta
        
    def pobierzDaneZwierzat(self):
        
        self.kursorDoBazy.execute("SELECT * FROM ZWIERZETA")
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
        
