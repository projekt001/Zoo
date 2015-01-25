from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaLaczaca import TablicaLaczaca

class OknoRozszerzenia(QtGui.QDialog):
    def __init__(self, 
                 kluczGlowny, 
                 nazwaTabeli, 
                 nazwaKolumn, 
                 kontroler, 
                 elementyDoWykluczenia, 
                 opisTabeli,
                 parent):
        super(OknoRozszerzenia, self).__init__(parent)
        self.nazwaTabeli           = nazwaTabeli
        self.kontroler             = kontroler
        self.kluczGlowny           = kluczGlowny
        self.nazwaKolumn           = nazwaKolumn
        self.elementyDoWykluczenia = elementyDoWykluczenia
        self.opisTabeli            = opisTabeli
        
    def closeEvent(self, evnt):
        self.parent().odswierz()
        
class OknoRozszerzeniaPozostale(OknoRozszerzenia):
    def __init__(self, 
                 kluczGlowny, 
                 nazwaTabeli, 
                 nazwaKolumn, 
                 kontroler, 
                 elementyDoWykluczenia, 
                 opisTabeli,
                 parent):
        super(OknoRozszerzeniaPozostale, self).__init__(kluczGlowny, 
                                                        nazwaTabeli, 
                                                        nazwaKolumn, 
                                                        kontroler, 
                                                        elementyDoWykluczenia,
                                                        opisTabeli,
                                                        parent)
    def generujWidok(self):
        
        aktualnaWartosc = self.kontroler.pobierzJedenWiersz(self.nazwaTabeli, self.kluczGlowny)
        
        self.poleTekstowe = []
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.listaWidgetow  = []
        
        for idxPolaTekstowego in range(len(self.nazwaKolumn)):
            self.listaWidgetow.append(QtGui.QLineEdit(str(aktualnaWartosc[idxPolaTekstowego + 1])))
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[idxPolaTekstowego])))
            self.verticalLayout.addWidget(self.listaWidgetow[0])
            
            
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(self.zapisz)
        
    def zapisz(self):
        poleDoZapisania = []
        poleDoZapisania.append(self.listaWidgetow[0].text())
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               poleDoZapisania)
        self.close()
        
class OknoRozszerzeniaZagrody(OknoRozszerzenia):
    def __init__(self, 
                 kluczGlowny, 
                 nazwaTabeli, 
                 nazwaKolumn, 
                 kontroler, 
                 elementyDoWykluczenia, 
                 opisTabeli,
                 parent):
        super(OknoRozszerzeniaZagrody, self).__init__(kluczGlowny, 
                                                      nazwaTabeli, 
                                                      nazwaKolumn, 
                                                      kontroler, 
                                                      elementyDoWykluczenia, 
                                                      opisTabeli,
                                                      parent)
    def generujWidok(self):
        
        
        aktualnaWartosc = self.kontroler.laczTabeleIPobierzWiersz(self.nazwaTabeli, 
                                                                  "TYPY_ZAGROD",
                                                                  "TYPY_ZAGROD_Id",
                                                                  "Id",
                                                                  "Nazwa_Typ_Zagrody",
                                                                   self.kluczGlowny)
        
        self.poleTekstowe = []
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout = QtGui.QVBoxLayout(self)
        
        self.listaWidgetow = []
        self.listaWidgetow.append(QtGui.QLineEdit(str(aktualnaWartosc[1])))
        self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[0])))
        self.verticalLayout.addWidget(self.listaWidgetow[0])
        
        self.listaWidgetow.append(QtGui.QLineEdit(str(aktualnaWartosc[2])))
        self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[1])))
        self.verticalLayout.addWidget(self.listaWidgetow[1])
        
        self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[2])))
        
        
        self.listaWidgetow.append(QtGui.QComboBox())
        self.combo= self.listaWidgetow[2]
        self.combo.addItem(str(aktualnaWartosc[4]))
        
        dane = self.kontroler.pobierzDane("TYPY_ZAGROD")
        
        for indexDodawania in range(len(dane)):
            if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[4])):
                self.combo.addItem(str(dane[indexDodawania][1]))

        self.verticalLayout.addWidget(self.combo)
        self.verticalLayout.addWidget(self.combo)
        self.verticalLayout.addWidget(self.przyciskZapisu)
        
        self.przyciskZapisu.clicked.connect(self.zapisz)
        
    def zapisz(self):
        poleDoZapisania = []
        poleDoZapisania.append(self.listaWidgetow[0].text())
        poleDoZapisania.append(self.listaWidgetow[1].text())
        comboBox = self.listaWidgetow[2]
        poleDoZapisania.append(comboBox.currentText());
        poleDoZapisania[2] = self.kontroler.pobierzIdPoNazwie("TYPY_ZAGROD",
                                                              "Nazwa_Typ_Zagrody",
                                                              poleDoZapisania[2])
        
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               poleDoZapisania)
        self.close()

class ZwierzetaComboBox(QtGui.QComboBox):
    def __init__(self, parent = None):
        super(ZwierzetaComboBox, self).__init__(parent)
    def pobierzTekst(self):
        return self.currentText()

class ZwierzetaQLineEdit(QtGui.QLineEdit):
    def __init__(self, tekst, parent = None):
        super(ZwierzetaQLineEdit, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()


class OknoRozszerzeniaZwierzeta(OknoRozszerzenia):
    def __init__(self, 
                 kluczGlowny, 
                 nazwaTabeli, 
                 nazwaKolumn, 
                 kontroler, 
                 elementyDoWykluczenia, 
                 opisTabeli,
                 parent):
        super(OknoRozszerzeniaZwierzeta, self).__init__(kluczGlowny, 
                                                        nazwaTabeli, 
                                                        nazwaKolumn, 
                                                        kontroler, 
                                                        elementyDoWykluczenia, 
                                                        opisTabeli,
                                                        parent)
    def generujWidok(self):
        
        tabeleDoLaczenia = ["GATUNKI", "ZAGRODY"]
        aktualnaWartosc = self.kontroler.laczIFiltruj("ZWIERZETA",
                                                     [["GATUNKI", "GATUNEK_Id", "Id"], 
                                                      ["ZAGRODY", "ZAGRODA_Id", "Id"]],
                                                      self.kluczGlowny,
                                                      "ZWIERZETA")
        
        self.listaWidgetow = []
        self.listaWidgetow.append(ZwierzetaQLineEdit(str(aktualnaWartosc[0][1])))
        self.listaWidgetow.append(ZwierzetaQLineEdit(str(aktualnaWartosc[0][2])))
        self.listaWidgetow.append(ZwierzetaQLineEdit(str(aktualnaWartosc[0][3])))
        self.listaWidgetow.append(ZwierzetaQLineEdit(str(aktualnaWartosc[0][4])))
        
        
        
        combo1= ZwierzetaComboBox()
        combo1.addItem(str(aktualnaWartosc[0][8]))
        
        dane = self.kontroler.pobierzDane("GATUNKI")
        
        for indexDodawania in range(len(dane)):
            if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[0][8])):
                combo1.addItem(str(dane[indexDodawania][1]))
                
        self.listaWidgetow.append(combo1) 
        
        combo2= ZwierzetaComboBox()
        combo2.addItem(str(aktualnaWartosc[0][10]))
        
        dane = self.kontroler.pobierzDane("ZAGRODY")
        
        for indexDodawania in range(len(dane)):
            if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[0][10])):
                combo2.addItem(str(dane[indexDodawania][1]))
                
        self.listaWidgetow.append(combo2) 

        self.verticalLayout = QtGui.QVBoxLayout(self)

        for indexKolumny in range(len(self.nazwaKolumn)):
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[indexKolumny])))
            self.verticalLayout.addWidget(self.listaWidgetow[indexKolumny])
            
            
        self.dodajPozywienia()
        self.dodajChoroby()
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(self.zapisz)
        
    def dodajChoroby(self):
        self.verticalLayout.addWidget(QtGui.QLabel("Choroby"))

        self.tabelaChoroby = TablicaLaczaca(self.kontroler, 
                                               [self.kluczGlowny, 0],
                                               ["ZWIERZETA_Id", "CHOROBY_Id"],
                                               ["LACZ_ZWIERZETA_CHOROBY", "ZWIERZETA", "CHOROBY"],
                                               'Nazwa_Choroby')

        
        self.tabelaChoroby.wyswietlTablice();
        self.verticalLayout.addWidget(self.tabelaChoroby)
        
    def dodajPozywienia(self):
        self.verticalLayout.addWidget(QtGui.QLabel("Pozywienia"))

        self.tabelaPozywienia = TablicaLaczaca(self.kontroler, 
                                               [self.kluczGlowny, 0],
                                               ["ZWIERZETA_Id", "POZYWIENIA_Id"],
                                               ["LACZ_ZWIERZETA_POZYWIENIA", "ZWIERZETA", "POZYWIENIA"],
                                               'Nazwa_Pozywienia')
        
        
        self.tabelaPozywienia.wyswietlTablice();
        self.verticalLayout.addWidget(self.tabelaPozywienia)
        
    def zapisz(self):
        polaDoZapisania = []
        for indexPol in range(len(self.listaWidgetow)):
            polaDoZapisania.append(self.listaWidgetow[indexPol].pobierzTekst())
            
        polaDoZapisania[4] = self.kontroler.pobierzIdPoNazwie("GATUNKI",
                                                              "Nazwa_Gatunku",
                                                              polaDoZapisania[4])
        
        polaDoZapisania[5] = self.kontroler.pobierzIdPoNazwie("ZAGRODY",
                                                              "Nazwa_Zagrody",
                                                              polaDoZapisania[5])
        
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               polaDoZapisania)
        self.close()
            

        


class WeterynarzeComboBox(QtGui.QComboBox):
    def __init__(self, parent = None):
        super(WeterynarzeComboBox, self).__init__(parent)
    def pobierzTekst(self):
        return self.currentText()

class WeterynarzeQLineEdit(QtGui.QLineEdit):
    def __init__(self, tekst, parent = None):
        super(WeterynarzeQLineEdit, self).__init__(tekst, parent)
    def pobierzTekst(self):
        return self.text()


class OknoRozszerzeniaWeterynarze(OknoRozszerzenia):
    def __init__(self, 
                 kluczGlowny, 
                 nazwaTabeli, 
                 nazwaKolumn, 
                 kontroler, 
                 elementyDoWykluczenia, 
                 opisTabeli,
                 parent):
        super(OknoRozszerzeniaWeterynarze, self).__init__(kluczGlowny, 
                                                        nazwaTabeli, 
                                                        nazwaKolumn, 
                                                        kontroler, 
                                                        elementyDoWykluczenia, 
                                                        opisTabeli,
                                                        parent)
    def generujWidok(self):
        
        aktualnaWartosc = self.kontroler.laczIFiltruj("WETERYNARZE",
                                                     [["SPECJALIZACJE", "SPECJALIZACJE_Id", "Id"]],
                                                      self.kluczGlowny,
                                                      "WETERYNARZE")
        
        self.listaWidgetow = []
        self.listaWidgetow.append(WeterynarzeQLineEdit(str(aktualnaWartosc[0][1])))
        self.listaWidgetow.append(WeterynarzeQLineEdit(str(aktualnaWartosc[0][2])))
        self.listaWidgetow.append(WeterynarzeQLineEdit(str(aktualnaWartosc[0][3])))
        
        
        
        combo1= WeterynarzeComboBox()
        combo1.addItem(str(aktualnaWartosc[0][6]))
        
        dane = self.kontroler.pobierzDane("SPECJALIZACJE")
        
        for indexDodawania in range(len(dane)):
            if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[0][6])):
                combo1.addItem(str(dane[indexDodawania][1]))
                
        self.listaWidgetow.append(combo1)

        self.verticalLayout = QtGui.QVBoxLayout(self)

        for indexKolumny in range(len(self.nazwaKolumn)):
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[indexKolumny])))
            self.verticalLayout.addWidget(self.listaWidgetow[indexKolumny])
            
            
        self.dodajZagrody()
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(self.zapisz)
        
    def dodajZagrody(self):
        self.verticalLayout.addWidget(QtGui.QLabel("Zagrody"))

        self.tabelaZagrody= TablicaLaczaca(self.kontroler, 
                                            [self.kluczGlowny, 0],
                                            ["WETERYNARZE_Id", "ZAGRODY_Id"],
                                            ["LACZ_WETERYNARZE_ZAGRODY", "WETERYNARZE", "ZAGRODY"],
                                            'Nazwa_Zagrody')
        
        self.tabelaZagrody.wyswietlTablice();
        self.verticalLayout.addWidget(self.tabelaZagrody)
        
        
    def zapisz(self):
        polaDoZapisania = []
        for indexPol in range(len(self.listaWidgetow)):
            polaDoZapisania.append(self.listaWidgetow[indexPol].pobierzTekst())
            
        polaDoZapisania[3] = self.kontroler.pobierzIdPoNazwie("SPECJALIZACJE",
                                                              "Nazwa_Specjalizacji",
                                                              polaDoZapisania[3])
        

        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               polaDoZapisania)
        self.close()