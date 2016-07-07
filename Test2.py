#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create three toggle buttons.
They will control the background colour of a
QFrame.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication, QGridLayout, QSizePolicy, QLabel, QMainWindow)
from PyQt5.QtGui import (QColor, QPixmap)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.Homepage()

    def Homepage(self):
        self.win = QMainWindow()
        frame = QFrame()
        self.win.setCentralWidget(frame)
        Layout = QGridLayout()
        frame.setLayout(Layout)

        Francais = QPushButton("FR", self)
        Francais.clicked.connect(self.RecetteFR)
        Anglais = QPushButton("AN", self)
        #Anglais.clicked.connect(self.RecetteAN)

        Layout.addWidget(Francais, 0, 0, 1, 2)
        Layout.addWidget(Anglais, 0, 2, 1, 2)

        self.win.show()

    def RecetteFR(self):
        recette1 = QLabel("Recette1")
        recette1.setGeometry(10, 10, 400, 100)
        pixmap = QPixmap("/home/shvonder/Pictures/example.jpg")
        recette1.setPixmap(pixmap)
        self.win.show()


   # def RecetteAN(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())