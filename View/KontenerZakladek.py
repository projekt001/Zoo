from PyQt4 import QtCore
from PyQt4 import QtGui
from Zwierzeta import Zwierzeta
from Weterynarze import Weterynarze
from Pozostale import Pozostale

class KontenerZakladek(QtGui.QTabWidget):
    def __init__(self, kontroler):
        super(KontenerZakladek, self).__init__()
        self.dodajZakladki(kontroler)
    
    def dodajZakladki(self, kontroler):
        self.zakladkaZwierzat    = Zwierzeta(self, kontroler)    
        self.zakladkaWeterynarze = Weterynarze(self, kontroler)
        self.zakladkaPozostale   = Pozostale(self, kontroler)

        self.addTab(self.zakladkaZwierzat,   "Zwierzeta")
        self.addTab(self.zakladkaWeterynarze,"Weterynarze")
        self.addTab(self.zakladkaPozostale,  "Pozostale")
        
    def odswierz(self):
        self.zakladkaZwierzat.odswierz()
        self.zakladkaWeterynarze.odswierz()
        self.zakladkaPozostale.odswierz()
