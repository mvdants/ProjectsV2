import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QDesktopWidget,
                               QVBoxLayout, QWidget,
                               QPushButton, QLabel, QLineEdit,
                               QStatusBar)
from interfaces.basicInterface import BasicInterface
from interface_functions.functions import verify_user


class UserLoginWindow(BasicInterface):

    window_length = 400
    window_high = 400

    def __init__(self):
        super().__init__()

        # Creating the widgets of the interface
        self.username_LineEdit = QLineEdit()
        self.password_LineEdit = QLineEdit()
        self.buttonEnter = QPushButton(" Enter ")
        self.status = QStatusBar()

        # Setting parameter of the widgets
        self.username_LineEdit.setAlignment(Qt.AlignCenter)
        self.username_LineEdit.setMinimumSize(UserLoginWindow.window_length, 25)
        self.password_LineEdit.setAlignment(Qt.AlignCenter)
        self.password_LineEdit.setMinimumSize(UserLoginWindow.window_length, 25)
        self.password_LineEdit.setEchoMode(QLineEdit.Password)
        self.buttonEnter.setMinimumSize(100, 40)

        # Creating the main layout
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignTop)

        # Adding to the main layout the widgets created
        mainLayout.addWidget(QLabel("Username"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.username_LineEdit)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(QLabel("Password"),  alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.password_LineEdit)
        mainLayout.addSpacing(50)
        mainLayout.addWidget(self.buttonEnter)
        mainLayout.addSpacing(10)

        # Setting global widget
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        # setting some actions to the window
        self.buttonEnter.clicked.connect(self.__button_enter_clicked)

        # Set some setting the the window
        self.setWindowTitle("User Login")
        self.setMinimumSize(UserLoginWindow.window_length, int(UserLoginWindow.window_high/2))
        self.createStatusBar()
        self.centering()

    def centering(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __button_enter_clicked(self):
        ver = verify_user(self.username_LineEdit.text(), self.password_LineEdit.text())
        if ver == (True, True):
            self.status.setStyleSheet("color: green")  # Changing the color
            self.status.showMessage("Thanks!")
        elif ver == (True, False):
            self.status.setStyleSheet("color: red")  # Changing the color
            self.status.showMessage("Wrong password")
        elif ver == (False, False):
            self.status.setStyleSheet("color: red")  # Changing the color
            self.status.showMessage("Wrong email or user is not registered")

    def createStatusBar(self):
        self.status.showMessage("Ready", 2500)
        self.setStatusBar(self.status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserLoginWindow()
    window.show()
    app.exec_()
