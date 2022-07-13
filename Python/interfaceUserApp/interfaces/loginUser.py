import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QDesktopWidget,
                               QHBoxLayout, QVBoxLayout, QWidget,
                               QPushButton, QLabel, QLineEdit,
                               QStatusBar)


class UserLoginWindow(QMainWindow):

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
        self.password_LineEdit.setAlignment(Qt.AlignCenter)
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
        self.setFixedSize(UserLoginWindow.window_length, int(UserLoginWindow.window_high/2))
        self.createStatusBar()
        self.centering()

    def centering(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __button_enter_clicked(self):
        print(self.password_LineEdit.text())

    def createStatusBar(self):
        self.status.showMessage("Ready", 2500)
        self.setStatusBar(self.status)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = UserLoginWindow()
    window.show()
    app.exec_()
