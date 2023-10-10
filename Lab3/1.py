import sys
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QDialog
from ui1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check_password)

    def validate_password(self):
        password = self.lineEdit.text()
        if len(password) < 8:
            return False

        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            return False

        if not re.search(r'\d', password):
            return False

        key_lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        for line in key_lines:
            s = 0
            triple = password[s:s + 3].lower()
            if triple in line and len(triple) == 3:
                return False

        return True

    def check_password(self):
        if self.validate_password():
            self.label_2.setText("ok")
        else:
            self.label_2.setText("error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
