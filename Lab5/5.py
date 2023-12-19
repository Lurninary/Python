import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeyEvent, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui5 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ufo = QPixmap("ufo.png").scaled(100, 100)
        self.ufo_position = self.width() // 2, self.height() // 2

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_A:
            self.ufo_position = ((self.ufo_position[0] - 25) % self.height(), self.ufo_position[1])
        elif event.key() == Qt.Key_D:
            self.ufo_position = ((self.ufo_position[0] + 25) % self.height(), self.ufo_position[1])
        elif event.key() == Qt.Key_W:
            self.ufo_position = (self.ufo_position[0], (self.ufo_position[1] - 25) % self.height())
        elif event.key() == Qt.Key_S:
            self.ufo_position = (self.ufo_position[0], (self.ufo_position[1] + 25) % self.height())

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(*self.ufo_position, self.ufo)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())