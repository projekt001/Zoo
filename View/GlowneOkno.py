#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from ZakladkaGlowna import Animals


class KontenerZakladek(QtGui.QTabWidget):
    def __init__(self):
        super(KontenerZakladek, self).__init__()
        self.addTabs()

    def addTabs(self):
        animalsTab1 = Animals()	
    	animalsTab2 = Animals()
    	animalsTab3 = Animals()

    	self.addTab(animalsTab1,"Tab 1")
    	self.addTab(animalsTab2,"Tab 2")
    	self.addTab(animalsTab3,"Tab 3")

  

class GlowneOkno(QtGui.QApplication):
    def __init__(self):
        #QtGui.QApplication.__init__(sys.argv)
        super(GlowneOkno, self).__init__(sys.argv)
        self.setApplicationName('Aplikacja Zarządcy Zoo')
        self.wyswietlZakladki();

    def wyswietlZakladki(self):
    	kontenerZakladek = KontenerZakladek()
    	kontenerZakladek.show()
    	sys.exit(self.exec_())
