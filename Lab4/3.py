import random
import sys
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

from ui3 import Ui_MainWindow


random.seed(123)

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.n = 3
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.n, ok_pressed = QInputDialog.getInt(
            self, "Введите кол-во цветов", "Сколько цветов флаг?",
            3, 1, 15, 1)
        if ok_pressed:
            self.label.setText(f"Флаг из {self.n} цветов")
        self.repaint()

    def draw_flag(self, qp):
        higth = 70
        for i in range(self.n):
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawRect(80, higth, 280, 60)
            higth += 60



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
