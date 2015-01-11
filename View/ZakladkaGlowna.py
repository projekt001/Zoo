from PyQt4 import QtCore
from PyQt4 import QtGui
from Tablica import Tablica

data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}

class Animals(QtGui.QWidget):
    def __init__(self):
	super(Animals, self).__init__()

        pushButtonWindow1 = QtGui.QPushButton()
        pushButtonWindow1.setText("Click Me 1!")

        pushButtonWindow2 = QtGui.QPushButton()
        pushButtonWindow2.setText("Click Me 2!")

        pushButtonWindow3 = QtGui.QPushButton()
        pushButtonWindow3.setText("Click Me 3!")

        pushButtonWindow4 = QtGui.QPushButton()
        pushButtonWindow4.setText("Click Me 4!")

    	vBoxlayout	= QtGui.QVBoxLayout()
    	vBoxlayout.addWidget(pushButtonWindow1)
	vBoxlayout.addWidget(pushButtonWindow2)
	vBoxlayout.addWidget(Tablica(data, 5, 3, self))

    	hBoxlayout	= QtGui.QHBoxLayout()
    	hBoxlayout.addWidget(pushButtonWindow3)
	hBoxlayout.addWidget(pushButtonWindow4)
	hBoxlayout.addWidget(Tablica(data, 5, 3, self))

	vBoxlayout.addLayout(hBoxlayout)

	self.setLayout(vBoxlayout)
