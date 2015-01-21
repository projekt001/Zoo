from PyQt4 import QtCore
from PyQt4 import QtGui

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
        
        for idxPolaTekstowego in range(len(self.nazwaKolumn)):
            
            self.poleTekstowe.append(str(aktualnaWartosc[idxPolaTekstowego + 1]))
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[idxPolaTekstowego])))
            self.verticalLayout.addWidget(QtGui.QLineEdit((self.poleTekstowe[idxPolaTekstowego])))
            
            
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(lambda: self.zapisz(self.poleTekstowe))
        
    def zapisz(self, poleDoZapisania):
        print "poleDoZapisania!!! = " + str(poleDoZapisania)
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
        
        print aktualnaWartosc
        
        self.poleTekstowe = []
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout = QtGui.QVBoxLayout(self)
        
        uzyteczneIndexy = [1, 3]
        
        self.poleTekstowe.append(str(aktualnaWartosc[1]))
        self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[0])))
        self.verticalLayout.addWidget(QtGui.QLineEdit(self.poleTekstowe[0]))
        
        self.poleTekstowe.append(str(aktualnaWartosc[3])) 
        self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[1])))
        
        #self.verticalLayout.addWidget(QtGui.QLineEdit(self.poleTekstowe[1]))
        
        self.combo = QtGui.QComboBox()
        self.combo.addItem(str(aktualnaWartosc[3]))
        
        dane = self.kontroler.pobierzDane("TYPY_ZAGROD")
        
        for indexDodawania in range(len(dane)):
            if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[3])):
                self.combo.addItem(str(dane[indexDodawania][1]))

        self.verticalLayout.addWidget(self.combo)
        self.verticalLayout.addWidget(self.combo)
        self.verticalLayout.addWidget(self.przyciskZapisu)
        
        self.przyciskZapisu.clicked.connect(lambda: self.zapisz(self.poleTekstowe, self.combo.currentText()))
        
    def zapisz(self, poleDoZapisania, daneZComboBox):
        
        poleDoZapisania[1] = daneZComboBox
        poleDoZapisania[1] = self.kontroler.pobierzIdPoNazwie("TYPY_ZAGROD",
                                                              "Nazwa_Typ_Zagrody",
                                                              poleDoZapisania[1])
        
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               poleDoZapisania)
        self.close()
            

        
