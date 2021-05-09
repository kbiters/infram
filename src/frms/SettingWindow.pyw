import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


def save():
    print("hola")


def back():
    sys.exit(0)


class SettingWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("SettingWindow.ui", self)
        self.buttons()

    def buttons(self):
        self.btnSave.clicked.connect(save)
        self.btnBack.clicked.connect(back)


if __name__ == "__main__":
    app = QApplication([])
    fcu = SettingWindow()
    fcu.show()
    app.exec_()
