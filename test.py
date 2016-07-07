import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication, QMainWindow, QGridLayout, QSizePolicy, QLabel, QVBoxLayout)
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.accueil()

    def accueil(self):

        self.win = QMainWindow()
        frame = QFrame()
        self.win.setCentralWidget(frame)
        layout = QGridLayout()
        frame.setLayout(layout)

        button_fr = QPushButton("FR")
        button_an = QPushButton("AN")
        bienvenue = QLabel("Bienvenue / Welcome")
        font = QFont('SignPainter-HouseScript', 20, QFont.Light)
        bienvenue.setFont(font)
        bienvenue.setAlignment(Qt.AlignCenter)
        bienvenue.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_fr.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_an.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        image = QLabel()
        image.setPixmap(QPixmap("images.png"))

        layout.addWidget(bienvenue, 0, 0, 1, 2)
        layout.addWidget(button_fr, 1, 0, 1, 1)
        layout.addWidget(button_an, 1, 1, 1, 1)
        layout.addWidget(image, 2, 1, 1, 1)


        self.win.col = QColor(0, 0, 0)

        self.win.show()
        #self.win.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    page1 = App()
    sys.exit(app.exec_())