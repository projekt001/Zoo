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
        print daneZwierzeta
        iloscWierszy  = len(daneZwierzeta)
        iloscKolumn   = len(daneZwierzeta[0])
        
        self.setRowCount(iloscWierszy + 1)
        self.setColumnCount(iloscKolumn + 1 - len(listaNieDoWyswietlenia))
        
        
        for indexWiersza in range(iloscWierszy):
            przesuniecie = 0;
            for indexKolumny in range(iloscKolumn):
                if not (indexKolumny in listaNieDoWyswietlenia):
                    noweZwierze = QtGui.QTableWidgetItem(daneZwierzeta[indexWiersza][indexKolumny])
                    self.setItem(indexWiersza, indexKolumny - przesuniecie, noweZwierze)
                else:
                    przesuniecie = przesuniecie + 1
            
            if(indexWiersza == 0):
                przyciskDoEdycji1 = QtGui.QPushButton(self)
                przyciskDoEdycji1.setText('edytuj')
                przyciskDoEdycji1.wartosc = daneZwierzeta[indexWiersza][0]
                print 'dodano = '+ str(daneZwierzeta[indexWiersza][0])
                dupa = str(daneZwierzeta[0][0])
                przyciskDoEdycji1.clicked.connect(lambda: self.on_pushButton_clicked(przyciskDoEdycji1.wartosc))
                self.setCellWidget(0, 1, przyciskDoEdycji1)
                
            if(indexWiersza == 1):
                przyciskDoEdycji2 = QtGui.QPushButton(self)
                przyciskDoEdycji2.setText('edytuj')
                print 'dodano = '+ str(daneZwierzeta[indexWiersza][0])
                dupa = str(daneZwierzeta[1][0])
                przyciskDoEdycji2.clicked.connect(lambda: self.on_pushButton_clicked(dupa))
                self.setCellWidget(1, 1, przyciskDoEdycji2)
            
        przyciskDoEdycji = QtGui.QPushButton(self)
        przyciskDoEdycji.setText('dodaj')
        przyciskDoEdycji.clicked.connect(lambda: self.on_pushButton_clicked(str(daneZwierzeta[0][0])))
        self.setCellWidget(iloscWierszy, iloscKolumn - przesuniecie, przyciskDoEdycji)
            
    def pobierzDane(self, opisZwierzeta):
        znaczniki    = ['Id']
        
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
    
    def on_pushButton_clicked(self, jeden):
        print 'jeden' + str(jeden)
        self.dialogTextBrowser = OknoRozszerzenia();
        self.dialogTextBrowser.exec_()
        
    def dodajRekordy(self):
        try:
            self.cursor.execute("""INSERT INTO ZWIERZETA (`Nazwa_Zwierzecia`) VALUES('Hipopotam')""")
            self.cursor.execute("""INSERT INTO ZWIERZETA (`Nazwa_Zwierzecia`) VALUES('Zyrafa')""")
            self.cursor.execute("""INSERT INTO ZWIERZETA (`Nazwa_Zwierzecia`) VALUES('Tygrys')""")
             
            self.cursor.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('Buraki')""")
            self.cursor.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('Marchew')""")
            self.cursor.execute("""INSERT INTO POZYWIENIA (Nazwa_Pozywienia) VALUES('JABLKA')""")
             
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(1, 1)""")
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(1, 2)""")
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(1, 3)""")
             
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(2, 1)""")
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(2, 2)""")
            self.cursor.execute("""INSERT INTO LACZ_ZWIERZETA_POZYWIENIA(ZWIERZETA_Id, POZYWIENIA_Id) VALUES(2, 3)""")
            
            self.cursor.execute("""DELETE FROM ZWIERZETA WHERE Id=1""")

        except Warning, e:
            print str(e)
            
        self.mysql.commit();
