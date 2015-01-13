from PyQt4 import QtCore
from PyQt4 import QtGui
from ZakladkaGlowna import Animals

class KontenerZakladek(QtGui.QTabWidget):
    def __init__(self, uchwytDoBazy):
        super(KontenerZakladek, self).__init__()
        self.dodajZakladki(uchwytDoBazy)

    def dodajZakladki(self, uchwytDoBazy):
        animalsTab1 = Animals(uchwytDoBazy)    
        animalsTab2 = Animals(uchwytDoBazy)
        animalsTab3 = Animals(uchwytDoBazy)

        self.addTab(animalsTab1, "Tab 1")
        self.addTab(animalsTab2,"Tab 2")
        self.addTab(animalsTab3,"Tab 3")
