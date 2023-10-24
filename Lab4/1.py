import sys

from PyQt5.QtGui import QPixmap, QColor, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.c_transform = 0
        self.pushButton.clicked.connect(self.open_file)
        self.buttonGroup.buttonClicked.connect(self.one_channel)
        self.pushButton_2.clicked.connect(self.rotate)
        self.pushButton_3.clicked.connect(self.rotate)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.png);;All Files (*)")
        if filename:
            self.pixmap = QPixmap(filename)
            self.label.setPixmap(self.pixmap)

    def one_channel(self):
        image = self.pixmap.toImage()

        for y in range(image.height()):
            for x in range(image.width()):
                color = image.pixelColor(x, y)
                if self.checkBox.isChecked():
                    r, g, b, a = color.getRgb()
                    color.setRgb(r, 0, 0, 0)
                elif self.checkBox_2.isChecked():
                    r, g, b, a = color.getRgb()
                    color.setRgb(0, g, 0, 0)
                else:
                    r, g, b, a = color.getRgb()
                    color.setRgb(0, 0, b, 0)

                image.setPixelColor(x, y, color)

        self.mpixmap = QPixmap.fromImage(image)
        transform = QTransform()
        transform.rotate(self.c_transform)
        self.mpixmap = self.mpixmap.transformed(transform)
        self.label.setPixmap(self.mpixmap)

    def rotate(self):
        transform = QTransform()
        if self.sender() == self.pushButton_2:
            transform.rotate(-90)
            self.c_transform -= 90
            self.mpixmap = self.mpixmap.transformed(transform)
        else:
            transform.rotate(90)
            self.c_transform += 90
            self.mpixmap = self.mpixmap.transformed(transform)

        self.label.setPixmap(self.mpixmap)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
