import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QDesktopWidget,
                               QVBoxLayout, QHBoxLayout, QWidget,
                               QPushButton, QLabel, QLineEdit,
                               QStatusBar)
from interfaces.basicInterface import BasicInterface
from interfaces.registerUser import RegisterUserWindow
from interface_functions.functions import verify_user


class UserLoginWindow(BasicInterface):

    window_length = 400
    window_high = 400

    def __init__(self):
        super().__init__()

        # Other interfaces
        self.registerWindow = RegisterUserWindow()

        # Creating the widgets of the interface
        self.username_LineEdit = QLineEdit()
        self.password_LineEdit = QLineEdit()
        self.buttonEnter = QPushButton(" Enter ")
        self.buttonRegister = QPushButton(" Register ")
        self.status = QStatusBar()

        # Setting parameter of the widgets
        self.username_LineEdit.setAlignment(Qt.AlignCenter)
        self.username_LineEdit.setMinimumSize(UserLoginWindow.window_length, 25)
        self.password_LineEdit.setAlignment(Qt.AlignCenter)
        self.password_LineEdit.setMinimumSize(UserLoginWindow.window_length, 25)
        self.password_LineEdit.setEchoMode(QLineEdit.Password)
        self.buttonEnter.setMinimumSize(100, 40)
        self.buttonRegister.setMinimumSize(100, 40)

        # Creating horizontal layout buttons
        buttonsLayout = QHBoxLayout()
        # Adding widgets
        buttonsLayout.addWidget(self.buttonEnter)
        buttonsLayout.addWidget(self.buttonRegister)
        # Creating a widget
        widget = QWidget()
        # setting the Layout to the widget
        widget.setLayout(buttonsLayout)

        # Creating the main layout
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignTop)

        # Adding to the main layout the widgets created
        mainLayout.addWidget(QLabel("Username"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.username_LineEdit, stretch=10)
        mainLayout.addWidget(QLabel("Password"),  alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.password_LineEdit, stretch=50)
        mainLayout.addWidget(widget, alignment=Qt.AlignCenter, stretch=50)

        # Setting global widget
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        # setting some actions to the window
        self.buttonEnter.clicked.connect(self.__button_enter_clicked)
        self.buttonRegister.clicked.connect(self.__button_register_clicked)

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
            self.sendMessage("Thanks!", "OK")
        elif ver == (True, False):
            self.sendMessage("Wrong password", "Error")
        elif ver == (False, False):
            self.sendMessage("Wrong email or user is not registered", "Error")

    def __button_register_clicked(self):
        self.registerWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserLoginWindow()
    window.show()
    app.exec_()
