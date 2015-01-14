from PyQt4 import QtCore
from PyQt4 import QtGui
from OknoRozszerzenia import OknoRozszerzenia


class Tablica(QtGui.QTableWidget):
    def __init__(self, uchwytDoBazy, kontroler, parent):
        QtGui.QTableWidget.__init__(self, parent)
        
        self.kontroler         = kontroler
        self.uchwytDoBazy      = uchwytDoBazy
        self.kursorDoBazy      = self.uchwytDoBazy.cursor()
          
        
        
