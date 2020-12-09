from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
import sys, mainLayout
from functionality import *
from main import *


class MainWindow(QMainWindow, mainLayout.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tray_icon.setIcon(QtGui.QIcon("images/logo.png"))
        self.setWindowIcon(QtGui.QIcon("images/logo.png"))
        self.setWindowTitle("Arduino Keyboard")
        self.changeButtonColor()
        self.profileButton_1.clicked.connect(self.chooseFirst)
        self.profileButton_2.clicked.connect(self.chooseSecond)
        self.profileButton_3.clicked.connect(self.chooseThird)
        self.profileButton_custom.clicked.connect(self.chooseCustom)
        self.funct = Functionality(3)
        self.profileButton_3.setStyleSheet('QPushButton {background-color: red; color: black;}')

    def chooseFirst(self):
        if self.funct.profile != 1:
            self.funct = Functionality(1)
            self.changeButtonColor()
            self.profileButton_1.setStyleSheet('QPushButton {background-color: red; color: white;}')
        print(self.funct.hotkeys)

    def chooseSecond(self):
        if self.funct.profile != 2:
            self.funct = Functionality(2)
            self.changeButtonColor()
            self.profileButton_2.setStyleSheet('QPushButton {background-color: red; color: white;}')
        print(self.funct.hotkeys)

    def chooseThird(self):
        if self.funct.profile != 3:
            self.funct = Functionality(3)
            self.changeButtonColor()
            self.profileButton_3.setStyleSheet('QPushButton {background-color: red; color: white;}')
        print(self.funct.hotkeys)

    def chooseCustom(self):
        pass

    def changeButtonColor(self):
        self.profileButton_1.setStyleSheet('QPushButton {background-color: white; color: black;}')
        self.profileButton_2.setStyleSheet('QPushButton {background-color: white; color: black;}')
        self.profileButton_3.setStyleSheet('QPushButton {background-color: white; color: black;}')
