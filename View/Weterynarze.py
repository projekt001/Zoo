from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaWeterynarze import TablicaWeterynarze


class Weterynarze(QtGui.QWidget):
    def __init__(self, kontenerZakladek, kontroler):
        super(Weterynarze, self).__init__()


        vBoxlayout    = QtGui.QVBoxLayout()
        self.tablicaWeterynarze = TablicaWeterynarze(kontenerZakladek,
                                                     kontroler, 
                                                     "WETERYNARZE", 
                                                     self)
        vBoxlayout.addWidget(self.tablicaWeterynarze)

        hBoxlayout    = QtGui.QHBoxLayout()
        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)
        
    def odswierz(self):
        self.tablicaWeterynarze.odswierz()