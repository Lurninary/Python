import sys
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QDialog
from ui1 import Ui_MainWindow


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check_password)

    def validate_password(self, password):
        if len(password) < 8:
            raise LengthError

        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            raise LetterError

        if not re.search(r'\d', password):
            raise DigitError

        key_lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        for line in key_lines:
            for i in range(len(password)):
                triple = password[i:i+3].lower()
                if triple in line and len(triple) == 3:
                    raise SequenceError

        return True

    def check_password(self):
        try:
            if self.validate_password(self.lineEdit.text()):
                self.label_2.setText("ok")
        except Exception:
            print(sys.exc_info())
            self.label_2.setText("error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
