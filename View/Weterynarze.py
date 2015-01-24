from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaWeterynarze import TablicaWeterynarze


class Weterynarze(QtGui.QWidget):
    def __init__(self, kontroler):
        super(Weterynarze, self).__init__()


        vBoxlayout    = QtGui.QVBoxLayout()
        vBoxlayout.addWidget(TablicaWeterynarze(kontroler, 
                                                "WETERYNARZE", 
                                                self))

        hBoxlayout    = QtGui.QHBoxLayout()
        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)