from PyQt4 import QtCore
from PyQt4 import QtGui
from ZakladkaGlowna import Animals

class KontenerZakladek(QtGui.QTabWidget):
    def __init__(self):
        super(KontenerZakladek, self).__init__()
        self.dodajZakladki()

    def dodajZakladki(self):
        animalsTab1 = Animals()    
        animalsTab2 = Animals()
        animalsTab3 = Animals()

<<<<<<< HEAD

        self.addTab(animalsTab1, "Tab 1")
=======
        self.addTab(animalsTab1,"Tab 1")
>>>>>>> d0a4587b2b08f95c89fe676c69eac34209f20ac2
        self.addTab(animalsTab2,"Tab 2")
        self.addTab(animalsTab3,"Tab 3")