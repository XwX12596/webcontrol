import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl
from ui_form import Ui_streamUI

class streamUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_streamUI()
        self.ui.setupUi(self)
        self.UiConnect()

    def UiConnect(self):
        self.ui.link.clicked.connect(self.linkstart)
        self.ui.ip_LE.textChanged.connect(self.OnUrlChanged)

    def linkstart(self): 
        self.ui.web.load(QUrl("https://www.baidu.com"))

    def OnUrlChanged(self):
        self.ui.url_LE.setText("http://" + self.ui.ip_LE.text() + ":25565")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = streamUI()
    widget.show()
    sys.exit(app.exec())
