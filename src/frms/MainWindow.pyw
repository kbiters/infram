import subprocess
import sys

from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from SettingWindow import SettingWindow


def start():
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
        self.buttons()

    def buttons(self):
        self.btnStart.clicked.connect(self.click_counter)
        self.btnSetting.clicked.connect(self.setting)
        self.btnUpdate.clicked.connect(update)
        self.btnExit.clicked.connect(close)

    def click_counter(self):
        self.clicks += 1
        self.lblCounClicks.setGeometry(QRect(205, 0, 50, 43))
        self.lblCounClicks.setText(QCoreApplication.translate("MainWindow",
                                                              u"<html><head/><body><p align=\"center\"><span style=\" "
                                                              u"font-size:14pt; font-weight:600; color:#ffff7f;\">"
                                                              f"{self.clicks}</span></p></body></html>",
                                                              None))

    def setting(self):
        self.window = SettingWindow()
        self.window.show()


if __name__ == "__main__":
    app = QApplication([])
    fcu = MainWindow()
    fcu.show()
    app.exec_()
