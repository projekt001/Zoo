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
#****************************************

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
        
        
        aktualnaWartosc = self.kontroler.laczTabeleIPobierzWiersz(self.nazwaTabeli, 
                                                                  "TYPY_ZAGROD",
                                                                  "TYPY_ZAGROD_Id",
                                                                  "Id",
                                                                  "Nazwa_Typ_Zagrody",
                                                                   self.kluczGlowny)
        
        #self.poleTekstowe = []
        

        
        #self.listaWidgetow = []
        self.verticalLayout = QtGui.QVBoxLayout(self)
        for indexKolumny in range(len(self.nazwaKolumn)):
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[indexKolumny])))
            
        #self.listaWidgetow.append(QtGui.QLineEdit(str(aktualnaWartosc[1])))
        #self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[0])))
        #self.verticalLayout.addWidget(self.listaWidgetow[0])
        
        #self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[1])))
        
        #self.listaWidgetow.append(QtGui.QComboBox())
        #self.combo= self.listaWidgetow[1]
        #self.combo.addItem(str(aktualnaWartosc[3]))
        
        #dane = self.kontroler.pobierzDane("TYPY_ZAGROD")
        
        #for indexDodawania in range(len(dane)):
            #if (str(dane[indexDodawania][1]) != str(aktualnaWartosc[3])):
                #self.combo.addItem(str(dane[indexDodawania][1]))

        #self.verticalLayout.addWidget(self.combo)
        #self.verticalLayout.addWidget(self.combo)
        
        
        
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(self.zapisz)
        
    def zapisz(self):
        poleDoZapisania = []
        poleDoZapisania.append(self.listaWidgetow[0].text())
        comboBox = self.listaWidgetow[1]
        poleDoZapisania.append(comboBox.currentText());
        poleDoZapisania[1] = self.kontroler.pobierzIdPoNazwie("TYPY_ZAGROD",
                                                              "Nazwa_Typ_Zagrody",
                                                              poleDoZapisania[1])
        
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.opisTabeli,
                                               self.kluczGlowny, 
                                               poleDoZapisania)
        self.close()
            

        
