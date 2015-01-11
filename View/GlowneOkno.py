#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4 import QtCore, QtGui
from ZakladkaGlowna import Animals


class GlowneOkno(QtGui.QTabWidget):

    def __init__(self):
        super(GlowneOkno, self).__init__()
	self.addTabs()

    def addTabs(self):

	animalsTab1 = Animals()	
    	animalsTab2 = Animals()
    	animalsTab3 = Animals()

    	self.addTab(animalsTab1,"Tab 1")
    	self.addTab(animalsTab2,"Tab 2")
    	self.addTab(animalsTab3,"Tab 3")

  

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = GlowneOkno()
    main.show()

    sys.exit(app.exec_())
