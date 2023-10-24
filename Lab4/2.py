import sys

from PyQt5.QtGui import QPixmap, QColor, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui2 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_file)
        self.horizontalSlider.valueChanged[int].connect(self.alpha_channel)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.png);;All Files (*)")
        if filename:
            self.pixmap = QPixmap(filename)
            self.pixmap = self.pixmap.scaled(300, 300)
            self.label.setPixmap(self.pixmap)


    def alpha_channel(self):
        image = self.pixmap.toImage()

        for y in range(image.height()):
            for x in range(image.width()):
                color = image.pixelColor(x, y)
                r, g, b, a = color.getRgb()
                color.setRgb(r, g, b, a - self.horizontalSlider.value())

                image.setPixelColor(x, y, color)

        self.mpixmap = QPixmap.fromImage(image)
        self.label.setPixmap(self.mpixmap)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
