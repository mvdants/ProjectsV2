from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QVBoxLayout, QWidget, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QRadioButton, QDateTimeEdit)
from interfaces.basicInterface import BasicInterface
from interface_functions.functions import create_user, get_all_user_email, verify_email_exist
from support.user import User


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
        self.birthday_DateTimeEdit.setMinimumSize(super().widget_length / 2, super().widget_high * 1.25)

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

        # Signals
        self.buttonApply.clicked.connect(self.__buttonApply_clicked)
        self.buttonCancel.clicked.connect(self.__buttonCancel_clicked)

    @staticmethod
    def __check2passwords(password1: str, password2: str) -> bool:
        return True if password1 == password2 else False

    @staticmethod
    def __check_email_already_exist(email: str) -> bool:
        return True if verify_email_exist(get_all_user_email(), email) else False

    def __check_form(self) -> bool:
        if self.name_LineEdit:
            if self.surname_LineEdit:
                if self.female_RadioButton.isChecked() or self.male_RadioButton.isChecked():
                    if self.email_LineEdit:
                        if self.password_LineEdit:
                            return True
                        else:
                            self.sendMessage("Please fill the password field", status="Error")
                    else:
                        self.sendMessage("Please fill the 'email' field", status="Error")
                else:
                    self.sendMessage("Please choose one option of gender field", status="Error")
            else:
                self.sendMessage("Please fill the 'surname' field", status="Error")
        else:
            self.sendMessage("Please fill the 'name' field", status="Error")

    def __buttonApply_clicked(self):
        filled_form = self.__check_form()
        email_not_exist = not self.__check_email_already_exist(self.email_LineEdit.text())
        equal_passwords = self.__check2passwords(
            self.password_LineEdit.text(), self.password_VerificationLineEdit.text())

        if filled_form:
            if email_not_exist:
                if equal_passwords:
                    create_user(
                        User(
                            name=self.name_LineEdit.text(),
                            surname=self.surname_LineEdit.text(),
                            birthday=self.birthday_DateTimeEdit.text(),
                            gender="male" if self.male_RadioButton.isChecked() else "female",
                            email=self.email_LineEdit.text(),
                            password=self.password_LineEdit.text()
                        ).user2json()
                    )
                    self.sendMessage("Your account has been created!")
                else:
                    self.sendMessage("The passwords are not identical", "Error")
            else:
                self.sendMessage("This email was already used", "Error")

    def __buttonCancel_clicked(self):
        self.status.showMessage("Operation canceled")
        self.close()


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = RegisterUserWindow()
    window.show()
    app.exec_()
