from PyQt4 import QtCore
from PyQt4 import QtGui
from TablicaZwierzeta import TablicaZwierzeta


class Zwierzeta(QtGui.QWidget):
    def __init__(self, kontroler):
        super(Zwierzeta, self).__init__()

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
        vBoxlayout.addWidget(TablicaZwierzeta(kontroler, self))

        hBoxlayout    = QtGui.QHBoxLayout()
        hBoxlayout.addWidget(pushButtonWindow3)
        hBoxlayout.addWidget(pushButtonWindow4)
        #hBoxlayout.addWidget(TablicaZwierzeta(uchwytDoBazy, kontroler self))

        vBoxlayout.addLayout(hBoxlayout)

        self.setLayout(vBoxlayout)