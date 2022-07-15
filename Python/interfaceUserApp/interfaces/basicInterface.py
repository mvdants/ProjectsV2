from PySide2.QtWidgets import (QMainWindow, QDesktopWidget, QStatusBar)


class BasicInterface(QMainWindow):

    window_length = 400
    window_high = 400
    widget_high = 25
    widget_length = 300

    def __init__(self):
        super().__init__()
        self.status = QStatusBar()

    def centering(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createStatusBar(self):
        self.status.showMessage("Ready", 2500)
        self.setStatusBar(self.status)
