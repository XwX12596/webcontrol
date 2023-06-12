# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene
from PyQt5.QtGui import QPixmap

from ui_form import Ui_PiCam

from functions import fetch, warning, angUPD, intUPD, getImage

class PiCam(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PiCam()
        self.ui.setupUi(self)
        self.UI_connect()
        self.window_init()
        self.url=''

    def window_init(self):
        self.scene = QGraphicsScene()

    def UI_connect(self):
        self.ui.fetch.clicked.connect(self.fetch)
        self.ui.warning.clicked.connect(self.warning)
        self.ui.int_BTN.clicked.connect(self.intUPD)
        self.ui.ang_BTN.clicked.connect(self.angUPD)
        self.ui.link.clicked.connect(self.link)

    def link(self):
        self.url = self.ui.ip_LE.text()
        self.ui.ip_LB.setText("connected")
    def fetch(self):
        fetch(self.url)
        getImage(self.url)
        self.pic = QPixmap("./image/result.jpg") 
        self.scene.addPixmap(self.pic.scaled(800, 450))
        self.ui.pic.setScene(self.scene)
    def warning(self):
        warning(self.url)
    def intUPD(self):
        time = self.ui.int_LE.text()
        if time != '':
            intUPD(time, self.url)
        else:
            self.ui.int_LE.setText("Please Enter A Interval Number!")
    def angUPD(self):
        ang = self.ui.ang_LE.text()
        if ang != '':
            angUPD(ang, self.url)
        else:
            self.ui.ang_LE.setText("Please Enter A Angle Number!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = PiCam()
    widget.show()
    sys.exit(app.exec())
