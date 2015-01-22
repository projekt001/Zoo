from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaZwierzeta import TablicaZwierzeta


class Zwierzeta(QtGui.QWidget):
    def __init__(self, kontroler):
        super(Zwierzeta, self).__init__()


        vBoxlayout    = QtGui.QVBoxLayout()
        vBoxlayout.addWidget(TablicaZwierzeta(kontroler, 
                                              "ZWIERZETA", 
                                              self))

        hBoxlayout    = QtGui.QHBoxLayout()
        #hBoxlayout.addWidget(pushButtonWindow3)
        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)