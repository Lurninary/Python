import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui4 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coords = [self.btn.x(), self.btn.y()]
        self.btn.clicked.connect(self.moveButton)

    def moveButton(self):
        self.coords[0] = random.randint(0, self.width() - self.btn.width())
        self.coords[1] = random.randint(0, self.height() - self.btn.height())
        self.btn.move(*self.coords)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())