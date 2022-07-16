from PySide2.QtWidgets import (QMainWindow, QDesktopWidget, QStatusBar)
from typing import Union, Literal


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

    def sendMessage(self, message: str, status: Union[Literal["OK", "Warning", "Error"]] = "OK"):
        if status == "OK":
            self.status.setStyleSheet("color: green")  # Changing the color
            self.status.showMessage(message)

        elif status == "Warning":
            self.status.setStyleSheet("color: yellow")  # Changing the color
            self.status.showMessage(message)

        elif status == "Error":
            self.status.setStyleSheet("color: red")  # Changing the color
            self.status.showMessage(message)

        else:
            raise TypeError("One parameter is not on the correct type")
