from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica


class Pozostale(QtGui.QWidget):
    def __init__(self, uchwytDoBazy):
        super(Pozostale, self).__init__()

        pushButtonWindow1 = QtGui.QPushButton()
        pushButtonWindow1.setText("Click Me 1!")

        pushButtonWindow2 = QtGui.QPushButton()
        pushButtonWindow2.setText("Click Me 2!")

        pushButtonWindow3 = QtGui.QPushButton()
        pushButtonWindow3.setText("Click Me 3!")

        pushButtonWindow4 = QtGui.QPushButton()
        pushButtonWindow4.setText("Click Me 4!")

        vBoxlayout    = QtGui.QVBoxLayout()
        vBoxlayout.addWidget(pushButtonWindow1)
        vBoxlayout.addWidget(pushButtonWindow2)
        #vBoxlayout.addWidget(Tablica(uchwytDoBazy, self))

        hBoxlayout    = QtGui.QHBoxLayout()
        hBoxlayout.addWidget(pushButtonWindow3)
        hBoxlayout.addWidget(pushButtonWindow4)
        #hBoxlayout.addWidget(Tablica(uchwytDoBazy, self))

        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)