#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from KontenerZakladek import KontenerZakladek

class GlowneOkno(QtGui.QApplication):
    def __init__(self):
        super(GlowneOkno, self).__init__(sys.argv)
        self.setApplicationName('Aplikacja Zarządcy Zoo')
        self.wyswietlZakladki();

    def wyswietlZakladki(self):
    	kontenerZakladek = KontenerZakladek()
    	kontenerZakladek.show()
    	sys.exit(self.exec_())
<<<<<<< HEAD

=======
>>>>>>> d0a4587b2b08f95c89fe676c69eac34209f20ac2
