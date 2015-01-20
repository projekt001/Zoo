from PyQt4 import QtCore
from PyQt4 import QtGui

class OknoRozszerzenia(QtGui.QDialog):
    def __init__(self, parent):
        super(OknoRozszerzenia, self).__init__(parent)

        
class OknoRozszerzeniaPozostale(OknoRozszerzenia):
    def __init__(self, kluczGlowny, nazwaTabeli, nazwaKolumn, kontroler, elementyDoWykluczenia, parent):
        super(OknoRozszerzeniaPozostale, self).__init__(parent) 
        self.nazwaTabeli = nazwaTabeli
        self.kontroler = kontroler
        self.kluczGlowny = kluczGlowny
        self.nazwaKolumn = nazwaKolumn
        self.elementyDoWykluczenia = elementyDoWykluczenia
        
    def generujWidok(self):
        
        aktualnaWartosc = self.kontroler.pobierzJedenWiersz(self.nazwaTabeli, self.kluczGlowny)
        
        self.poleTekstowe = []
        
        self.przyciskZapisu = QtGui.QPushButton("zapisz")
        self.verticalLayout = QtGui.QVBoxLayout(self)
        
        for idxPolaTekstowego in range(len(self.nazwaKolumn)):
            self.poleTekstowe.append(QtGui.QLineEdit(str(aktualnaWartosc[idxPolaTekstowego + 1])))
            self.verticalLayout.addWidget(QtGui.QLabel(str(self.nazwaKolumn[idxPolaTekstowego])))
            self.verticalLayout.addWidget(self.poleTekstowe[idxPolaTekstowego])
            
            
        self.verticalLayout.addWidget(self.przyciskZapisu)
        self.przyciskZapisu.clicked.connect(lambda: self.zapisz(self.poleTekstowe))
        
    def closeEvent(self, evnt):
        self.parent().odswierz()
            
    def zapisz(self, poleDoZapisania):
        self.kontroler.modyfikujWartoscWTabeli(self.nazwaTabeli,
                                               self.nazwaKolumn,
                                               self.kluczGlowny, 
                                               poleDoZapisania)
        self.close()
        