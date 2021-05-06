import subprocess
import sys
from time import sleep

from PyQt5.QtCore import QRect, QCoreApplication, Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui, QtCore


def start():
    print("hola")


def setting():
    print("hola")


def close():
    sys.exit(0)


def update():
    subprocess.Popen("cmd /c start brave https://discord.com/channels/832310013878861825/837688546080587796")


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("MainWindow.ui", self)
        self.clicks = 0
        self.btnStart.clicked.connect(self.click_counter)
        self.btnSetting.clicked.connect(setting)
        self.btnUpdate.clicked.connect(update)
        self.btnExit.clicked.connect(close)

        self.count = 500
        self.label = QLabel(self)
        self.label.setGeometry(375, 0, 235, 50)
        self.label.setFont(QFont('Times', 18))
        self.label.setStyleSheet("QLabel {color : white; }")
        self.label.setAlignment(Qt.AlignCenter)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        self.count -= 1
        sleep(1)
        text = "Time to repeat: " + str(self.count) + " s"
        self.label.setText(text)
        if self.count == 0:
            self.label.setText("Completed !!!! ")

    def click_counter(self):
        self.clicks += 1
        self.lblCounClicks.setGeometry(QRect(210, 11, 61, 41))
        self.lblCounClicks.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" "
                                                              u"font-size:14pt; font-weight:600; color:#a8a252;\">"
                                                              f"{self.clicks}</span></p></body></html>",
                                                              None))


if __name__ == "__main__":
    app = QApplication([])
    fcu = MainWindow()
    fcu.show()
    app.exec_()
