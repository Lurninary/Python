import sys
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QDialog
from ui5 import Ui_MainWindow


class NumberError(Exception):
    pass


class InvalidFormat(NumberError):
    pass


class CountryCode(NumberError):
    pass


class OperatorError(NumberError):
    pass


class LengthError(NumberError):
    pass


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Check)

    def validateNumber(self, number):
        ref_number = self.RefactorNumber(number)

        MTC = list(range(910, 920, 1)) + list(range(980, 990, 1))
        Megafon = list(range(920, 940, 1))
        Beline = list(range(902, 907, 1)) + list(range(960, 970, 1))

        if not (number.count('(') == number.count(')')):
            raise InvalidFormat

        if '--' in number or number[-1] == '-':
            raise InvalidFormat

        if not (number[:2] == "+7" or number[0] == '8'):
            raise CountryCode

        if len(ref_number[1:]) != 11:
            raise LengthError

        if not (int(ref_number[2:5]) in MTC or int(ref_number[2:5]) in Megafon or int(ref_number[2:5]) in Beline):
            raise OperatorError

        return True

    def RefactorNumber(self, number):

        temp = ''
        if number[0] == '8':
            number = '+7' + number[1:]

        print(number)

        for i in number:
            if not (i in "-() "):
                temp += i
            print(i)

        return temp

    def Check(self):
        number = self.lineEdit.text()

        try:
            ref_number = self.RefactorNumber(number)
            if self.validateNumber(number):
                self.plainTextEdit.appendPlainText(f'{number} ----- {ref_number}')
        except InvalidFormat:
            self.plainTextEdit.appendPlainText(f'{number} ----- Неверный формат')
        except CountryCode:
            self.plainTextEdit.appendPlainText(f'{number} ----- Неверный код страны')
        except LengthError:
            self.plainTextEdit.appendPlainText(f'{number} ----- Неверное количество цифр')
        except OperatorError:
            self.plainTextEdit.appendPlainText(f'{number} ----- Не определяется оператор сотовой связи')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
