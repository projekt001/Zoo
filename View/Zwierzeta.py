from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaZwierzeta import TablicaZwierzeta


class Zwierzeta(QtGui.QWidget):
    def __init__(self, kontenerZakladek, kontroler):
        super(Zwierzeta, self).__init__()

        self.tablicaZwierzeta = TablicaZwierzeta(kontenerZakladek,
                                                 kontroler, 
                                                 "ZWIERZETA", 
                                                 self)
        vBoxlayout    = QtGui.QVBoxLayout()
        vBoxlayout.addWidget(self.tablicaZwierzeta)

        hBoxlayout    = QtGui.QHBoxLayout()
        #hBoxlayout.addWidget(pushButtonWindow3)
        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)
        
    def odswierz(self):
        self.tablicaZwierzeta.odswierz()
        