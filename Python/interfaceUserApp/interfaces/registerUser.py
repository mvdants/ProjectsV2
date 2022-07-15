import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QDesktopWidget,
                               QVBoxLayout, QWidget, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QRadioButton, QDateTimeEdit)
from interfaces.basicInterface import BasicInterface
from interface_functions.functions import verify_user


class RegisterUserWindow(BasicInterface):

    def __init__(self):
        super().__init__()

        # Creating widgets
        self.name_LineEdit = QLineEdit()
        self.surname_LineEdit = QLineEdit()
        self.birthday_DateTimeEdit = QDateTimeEdit()
        self.female_RadioButton = QRadioButton("Female")
        self.male_RadioButton = QRadioButton("Male")
        self.email_LineEdit = QLineEdit()
        self.password_LineEdit = QLineEdit()
        self.password_VerificationLineEdit = QLineEdit()
        self.buttonApply = QPushButton("Apply")
        self.buttonCancel = QPushButton("Cancel")

        # Setting parameter of the widgets
        # Centering alignment
        self.name_LineEdit.setAlignment(Qt.AlignCenter)
        self.surname_LineEdit.setAlignment(Qt.AlignCenter)
        self.email_LineEdit.setAlignment(Qt.AlignCenter)
        self.password_LineEdit.setAlignment(Qt.AlignCenter)
        self.password_VerificationLineEdit.setAlignment(Qt.AlignCenter)

        # Hiding password
        self.password_LineEdit.setEchoMode(QLineEdit.Password)
        self.password_VerificationLineEdit.setEchoMode(QLineEdit.Password)

        # Date
        self.birthday_DateTimeEdit.setDisplayFormat("dd.MM.yyyy")
        self.birthday_DateTimeEdit.setAlignment(Qt.AlignCenter)

        # Widgets Sizes
        self.name_LineEdit.setMinimumSize(super().widget_length, super().widget_high)
        self.surname_LineEdit.setMinimumSize(super().widget_length, super().widget_high)
        self.email_LineEdit.setMinimumSize(super().widget_length, super().widget_high)
        self.password_LineEdit.setMinimumSize(super().widget_length, super().widget_high)
        self.password_VerificationLineEdit.setMinimumSize(super().widget_length, super().widget_high)
        self.birthday_DateTimeEdit.setMinimumSize(super().widget_length/2, super().widget_high*1.25)

        # SubLayout radio buttons
        radioLayout = QHBoxLayout()
        radioLayout.addWidget(QLabel("Gender: "))
        radioLayout.addWidget(self.female_RadioButton)
        radioLayout.addWidget(self.male_RadioButton)
        self.radioWidget = QWidget()
        self.radioWidget.setLayout(radioLayout)

        # SubLayout push buttons
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.buttonApply)
        buttonsLayout.addWidget(self.buttonCancel)
        self.buttonsWidget = QWidget()
        self.buttonsWidget.setLayout(buttonsLayout)

        # Creating the main layout
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignTop)

        # Adding to the main layout the widgets created
        mainLayout.addWidget(QLabel("Digit your name"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.name_LineEdit, stretch=20, alignment=Qt.AlignCenter)
        mainLayout.addWidget(QLabel("Digit your surname"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.surname_LineEdit, stretch=20, alignment=Qt.AlignCenter)
        mainLayout.addWidget(QLabel("Choose your birthday"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.birthday_DateTimeEdit, alignment=Qt.AlignCenter, stretch=20)
        mainLayout.addWidget(self.radioWidget, alignment=Qt.AlignCenter, stretch=20)
        mainLayout.addWidget(QLabel("Digit your E-mail"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.email_LineEdit, alignment=Qt.AlignCenter, stretch=20)
        mainLayout.addWidget(QLabel("Digit your password"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.password_LineEdit, alignment=Qt.AlignCenter, stretch=20)
        mainLayout.addWidget(QLabel("Digit your password again"), alignment=Qt.AlignCenter)
        mainLayout.addWidget(self.password_VerificationLineEdit, alignment=Qt.AlignCenter, stretch=50)
        mainLayout.addWidget(self.buttonsWidget, alignment=Qt.AlignCenter, stretch=20)

        # Setting global widget
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        # Set some setting the the window
        self.setWindowTitle("User Register")
        self.setMinimumSize(super().window_length, int(super().window_high / 2))
        self.createStatusBar()
        self.centering()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterUserWindow()
    window.show()
    app.exec_()
