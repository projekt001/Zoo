from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia



class Tablica(QtGui.QTableWidget):
    def __init__(self, data, row, column, parent):
	QtGui.QTableWidget.__init__(self, row, column, parent)

        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def generateQTable(self):
 
        btn1 = QtGui.QPushButton()
        btn1.setText('1')
        btn1.clicked.connect(self.on_pushButton_clicked)
 
        btn2 = QtGui.QPushButton()
        btn2.setText('2')
 
 	self.dialogTextBrowser = OknoRozszerzenia();
        horHeaders = []
 
        znacznik1 = "1"
        znacznik2 = "2"
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                if (item == znacznik1):
                    self.setCellWidget(0, 0, btn1)
                elif (item == znacznik2):
                    self.setCellWidget(0, 1, btn2)
                else:
                    print item
                    newitem = QtGui.QTableWidgetItem(item)
                    self.setItem(m, n, newitem)
 
        self.setHorizontalHeaderLabels(horHeaders)
 
    def setmydata(self):
        self.generateQTable();
 
 
    def on_pushButton_clicked(self):
        self.dialogTextBrowser.exec_()
