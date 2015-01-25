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
        self.show()
        
    def wyswietlZakladki(self, kontroler):
    	kontenerZakladek = KontenerZakladek(kontroler)
        screen = QtGui.QDesktopWidget().screenGeometry()
        kontenerZakladek.resize(screen.width(), screen.height())
    	kontenerZakladek.show()
        sys.exit(self.exec_())
