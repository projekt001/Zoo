from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica
from TablicaPozostale import TablicaPozostale


class Pozostale(QtGui.QWidget):
    def __init__(self, uchwytDoBazy, kontroler):
        super(Pozostale, self).__init__()

        vBoxlayout    = QtGui.QVBoxLayout()
        pozywieniaWidget = TablicaPozostale(uchwytDoBazy, kontroler, "POZYWIENIA", self);
        pozywieniaWidget.przyciskPozywienia();
        
        vBoxlayout.addWidget(pozywieniaWidget)
        
        vBoxlayout.addWidget(TablicaPozostale(uchwytDoBazy, kontroler, "CHOROBY", self))
        vBoxlayout.addWidget(TablicaPozostale(uchwytDoBazy, kontroler, "GATUNKI", self))
        vBoxlayout.addWidget(TablicaPozostale(uchwytDoBazy, kontroler, "TYPY_ZAGROD", self))
        vBoxlayout.addWidget(TablicaPozostale(uchwytDoBazy, kontroler, "ZAGRODY", self))
        
        hBoxlayout    = QtGui.QHBoxLayout()


        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)