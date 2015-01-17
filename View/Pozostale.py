from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica
from TablicaPozostale import TablicaPozostale
from TablicaPozostale import TablicaPozostaleZagrody

class Pozostale(QtGui.QWidget):
    def __init__(self, kontroler):
        super(Pozostale, self).__init__()

        vBoxlayout    = QtGui.QVBoxLayout()
        pozywieniaWidget = TablicaPozostale(kontroler, "POZYWIENIA", self);
        
        vBoxlayout.addWidget(pozywieniaWidget)
        
        vBoxlayout.addWidget(TablicaPozostale(kontroler, "CHOROBY", self))
        vBoxlayout.addWidget(TablicaPozostale(kontroler, "GATUNKI", self))
        vBoxlayout.addWidget(TablicaPozostale(kontroler, "TYPY_ZAGROD", self))
        vBoxlayout.addWidget(TablicaPozostaleZagrody(kontroler, "ZAGRODY", self))
        
        hBoxlayout    = QtGui.QHBoxLayout()


        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)