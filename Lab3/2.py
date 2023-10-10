import sys
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QDialog
from ui1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.validate_password)

    def validate_password(self):
        password = self.lineEdit.text()
        try:
            assert len(password) > 8

            assert re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password)

            assert re.search(r'\d', password)

            key_lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
            for line in key_lines:
                s = 0
                triple = password[s:s + 3].lower()
                assert not triple in line and len(triple) == 3

            self.label_2.setText("ok")

        except AssertionError:
            self.label_2.setText("error")




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
