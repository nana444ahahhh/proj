import random
from PIL import Image
from random import randint
from PyQt5 import QtCore
im = Image.open("jail.jpeg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = g, 0, 0

im.save("Рианна2.jpg")

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow

from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt


class focuss(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.n = 'corridor.jpg'
        self.setGeometry(100, 200, 1000, 1000)
        self.pixmap = QPixmap('jail.jpeg')
        self.image = QLabel(self)
        self.image.resize(600, 600)
        self.image.move(250, 250)
        self.image.setPixmap(self.pixmap)
        self.r = QPushButton(self)
        self.r.setText("R")
        self.r.resize(100, 70)
        self.r.move(50, 300)

        self.g = QPushButton(self)
        self.g.setText("G")
        self.g.resize(100, 70)
        self.g.move(50, 400)

        self.b = QPushButton(self)
        self.b.setText("B")
        self.b.resize(100, 70)
        self.b.move(50, 500)

        self.vopros = QPushButton(self)
        self.vopros.setText("???")
        self.vopros.resize(100, 70)
        self.vopros.move(50, 600)

        self.all = QPushButton(self)
        self.all.setText("ALL")
        self.all.resize(100, 70)
        self.all.move(50, 700)

        self.dev = QPushButton(self)
        self.dev.setText("90")
        self.dev.resize(200, 50)
        self.dev.move(250, 150)

        self.dev2 = QPushButton(self)
        self.dev2.setText("-90")
        self.dev2.resize(200, 50)
        self.dev2.move(650, 150)

        self.r.clicked.connect(self.redder)
        self.g.clicked.connect(self.greener)
        self.b.clicked.connect(self.bluer)
        self.vopros.clicked.connect(self.mystery)
        self.all.clicked.connect(self.vse)
        self.dev.clicked.connect(self.devv)
        self.dev2.clicked.connect(self.devv2)

    def redder(self):
        im = Image.open("jail.jpeg")
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def greener(self):
        im = Image.open("jail.jpeg")
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        im.save(self.n)

        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def bluer(self):
        im = Image.open("jail.jpeg")
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def mystery(self):
        im = Image.open("drevo.jpg")

        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]

                pixels[i, j] = r, g, b
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def vse(self):
        im = Image.open("jail.jpeg")
        pixels = im.load()  # список с пикселями
        x, y = im.size  # ширина (x) и высота (y) изображения
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def devv(self):
        im = Image.open("jail.jpeg")
        im = im.rotate(90)
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.image.setPixmap(self.pixmap)

    def devv2(self):
        im = Image.open("jail.jpeg")
        im = im.rotate(-90)
        im.save(self.n)
        self.pixmap = QPixmap(self.n)
        self.pixmap1 = self.pixmap.scaled(400, 400, QtCore.KeepAspectRatio)
        self.image.setPixmap(self.pixmap1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = focuss()
    ex.show()
    sys.exit(app.exec())
