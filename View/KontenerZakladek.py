from PyQt4 import QtCore
from PyQt4 import QtGui
from Zwierzeta import Zwierzeta
from Weterynarze import Weterynarze
from Pozostale import Pozostale

class KontenerZakladek(QtGui.QTabWidget):
    def __init__(self, uchwytDoBazy):
        super(KontenerZakladek, self).__init__()
        self.dodajZakladki(uchwytDoBazy)

    def dodajZakladki(self, uchwytDoBazy):
        zakladkaZwierzat    = Zwierzeta(uchwytDoBazy)    
        zakladkaWeterynarze = Weterynarze(uchwytDoBazy)
        zakladkaPozostale   = Pozostale(uchwytDoBazy)

        self.addTab(zakladkaZwierzat,   "Zwierzeta")
        self.addTab(zakladkaWeterynarze,"Weterynarze")
        self.addTab(zakladkaPozostale,  "Pozostale")
