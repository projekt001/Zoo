from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica
from TablicaPozostale import TablicaPozostale
from TablicaPozostale import TablicaPozostaleZagrody

class Pozostale(QtGui.QWidget):
    def __init__(self, kontenerZakladek, kontroler):
        super(Pozostale, self).__init__()

        hBoxlayout1  = QtGui.QHBoxLayout()
        hBoxlayout2  = QtGui.QHBoxLayout()
        
        vBoxlayout1  = QtGui.QVBoxLayout()
        vBoxlayout1.addWidget(QtGui.QLabel("POZYWIENIA"))
        self.tablicaPozywienia = TablicaPozostale(kontenerZakladek, kontroler, "POZYWIENIA", self)
        vBoxlayout1.addWidget(self.tablicaPozywienia)
        
        vBoxlayout2  = QtGui.QVBoxLayout()
        vBoxlayout2.addWidget(QtGui.QLabel("CHOROBY"))
        self.tablicaChoroby = TablicaPozostale(kontenerZakladek, kontroler, "CHOROBY", self)
        vBoxlayout2.addWidget(self.tablicaChoroby)
        
        vBoxlayout3  = QtGui.QVBoxLayout()
        vBoxlayout3.addWidget(QtGui.QLabel("GATUNKI"))
        self.tablicaGatunki = TablicaPozostale(kontenerZakladek, kontroler, "GATUNKI", self)
        vBoxlayout3.addWidget(self.tablicaGatunki)
        
        hBoxlayout1.addLayout(vBoxlayout1)
        hBoxlayout1.addLayout(vBoxlayout2)
        hBoxlayout1.addLayout(vBoxlayout3)
        
        vBoxlayout4  = QtGui.QVBoxLayout()
        vBoxlayout4.addWidget(QtGui.QLabel("SPECJALIZACJE"))
        self.tablicaSpecjalizacje = TablicaPozostale(kontenerZakladek, kontroler, "SPECJALIZACJE", self)
        vBoxlayout4.addWidget(self.tablicaSpecjalizacje)
        
        vBoxlayout5  = QtGui.QVBoxLayout()
        vBoxlayout5.addWidget(QtGui.QLabel("TYPY ZAGROD"))
        self.tablicaTypyZagrod = TablicaPozostale(kontenerZakladek, kontroler, "TYPY_ZAGROD", self)
        vBoxlayout5.addWidget(self.tablicaTypyZagrod)

        vBoxlayout6  = QtGui.QVBoxLayout()
        vBoxlayout6.addWidget(QtGui.QLabel("ZAGRODY"))
        self.tablicaPozostaleZagrody = TablicaPozostaleZagrody(kontenerZakladek, kontroler, "ZAGRODY", self)
        vBoxlayout6.addWidget(self.tablicaPozostaleZagrody)
        
        hBoxlayout2.addLayout(vBoxlayout4)
        hBoxlayout2.addLayout(vBoxlayout5)
        hBoxlayout2.addLayout(vBoxlayout6)
        
        vBoxlayout  = QtGui.QVBoxLayout()

        vBoxlayout.addLayout(hBoxlayout1)
        vBoxlayout.addLayout(hBoxlayout2)

        self.setLayout(vBoxlayout)
        
    def odswierz(self):
        self.tablicaPozywienia.odswierz()
        self.tablicaChoroby.odswierz()
        self.tablicaGatunki.odswierz()
        self.tablicaSpecjalizacje.odswierz()
        self.tablicaTypyZagrod.odswierz()
        self.tablicaPozostaleZagrody.odswierz()