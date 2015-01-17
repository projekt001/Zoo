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
        zakladkaZwierzat    = Zwierzeta(kontroler)    
        zakladkaWeterynarze = Weterynarze(kontroler)
        zakladkaPozostale   = Pozostale(kontroler)

        self.addTab(zakladkaZwierzat,   "Zwierzeta")
        self.addTab(zakladkaWeterynarze,"Weterynarze")
        self.addTab(zakladkaPozostale,  "Pozostale")
