from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica
from TablicaPozostale import TablicaPozostale
from TablicaPozostale import TablicaPozostaleZagrody

class Pozostale(QtGui.QWidget):
    def __init__(self, kontroler):
        super(Pozostale, self).__init__()

        hBoxlayout1  = QtGui.QHBoxLayout()
        hBoxlayout2  = QtGui.QHBoxLayout()
        
        vBoxlayout1  = QtGui.QVBoxLayout()
        vBoxlayout1.addWidget(QtGui.QLabel("POZYWIENIA"))
        vBoxlayout1.addWidget(TablicaPozostale(kontroler, "POZYWIENIA", self))
        
        vBoxlayout2  = QtGui.QVBoxLayout()
        vBoxlayout2.addWidget(QtGui.QLabel("CHOROBY"))
        vBoxlayout2.addWidget(TablicaPozostale(kontroler, "CHOROBY", self))
        
        vBoxlayout3  = QtGui.QVBoxLayout()
        vBoxlayout3.addWidget(QtGui.QLabel("GATUNKI"))
        vBoxlayout3.addWidget(TablicaPozostale(kontroler, "GATUNKI", self))
        
        hBoxlayout1.addLayout(vBoxlayout1)
        hBoxlayout1.addLayout(vBoxlayout2)
        hBoxlayout1.addLayout(vBoxlayout3)
        
        vBoxlayout4  = QtGui.QVBoxLayout()
        vBoxlayout4.addWidget(QtGui.QLabel("SPECJALIZACJE"))
        vBoxlayout4.addWidget(TablicaPozostale(kontroler, "SPECJALIZACJE", self))
        
        vBoxlayout5  = QtGui.QVBoxLayout()
        vBoxlayout5.addWidget(QtGui.QLabel("TYPY ZAGROD"))
        vBoxlayout5.addWidget(TablicaPozostale(kontroler, "TYPY_ZAGROD", self))

        vBoxlayout6  = QtGui.QVBoxLayout()
        vBoxlayout6.addWidget(QtGui.QLabel("ZAGRODY"))
        vBoxlayout6.addWidget(TablicaPozostaleZagrody(kontroler, "ZAGRODY", self))
        
        hBoxlayout2.addLayout(vBoxlayout4)
        hBoxlayout2.addLayout(vBoxlayout5)
        hBoxlayout2.addLayout(vBoxlayout6)
        
        vBoxlayout  = QtGui.QVBoxLayout()

        vBoxlayout.addLayout(hBoxlayout1)
        vBoxlayout.addLayout(hBoxlayout2)

        self.setLayout(vBoxlayout)