#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from KontenerZakladek import KontenerZakladek

class GlowneOkno(QtGui.QApplication):
    def __init__(self, kontroler):
        super(GlowneOkno, self).__init__(sys.argv)
        self.setApplicationName('Aplikacja Zarządcy Zoo')
        self.wyswietlZakladki(kontroler);

    def wyswietlZakladki(self, kontroler):
    	kontenerZakladek = KontenerZakladek(kontroler)
    	kontenerZakladek.show()
        sys.exit(self.exec_())
