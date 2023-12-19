import sys
from random import choice, randint

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QPolygon, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui3 import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.x, self.y = -1, -1
        self.GOG = None
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black', 'Pink']


    def setupUi(self, Form):
        self.setMouseTracking(True)
        Form.resize(500, 500)


    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.GOG = 1
        elif event.button() == Qt.LeftButton:
            self.GOG = -1
        self.update()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.GOG = 2
        self.update()


    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()


    def drawing(self, qp):
        length = randint(50, 200)
        if self.GOG == 1:
            qp.setBrush(QColor(choice(self.colors)))

            qp.drawRect(self.x - length // 2, self.y - length // 2, length, length)
            ex.show()

        elif self.GOG == -1:
            qp.setBrush(QColor(choice(self.colors)))

            qp.drawEllipse(self.x - length // 2, self.y - length // 2, length,
                           length)

        elif self.GOG == 2:
            qp.setBrush(QColor(choice(self.colors)))

            points = QPolygon(
                [QPoint((self.x + length // 2), (self.y + length // 2)),
                 QPoint(self.x, self.y - length // 2),
                 QPoint(self.x - length // 2,
                        self.y + length // 2)])
            qp.drawPolygon(points)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())