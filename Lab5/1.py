import csv
import sys
import re

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui1 import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('rez.csv')
        self.loadSchoolNumbers()
        self.loadClassNumbers()
        self.comboBox.currentTextChanged.connect(self.filterData)
        self.comboBox_2.currentTextChanged.connect(self.filterData)
        self.pushButton_2.clicked.connect(self.resetTable)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def loadSchoolNumbers(self):
        logins = [self.tableWidget.item(i, 2).text() for i in range(self.tableWidget.rowCount())]

        school_numbers = sorted(set(login.split('-')[2] for login in logins))

        self.comboBox.clear()
        self.comboBox.insertItem(0, "")
        self.comboBox.addItems(school_numbers)

    def loadClassNumbers(self):
        logins = [self.tableWidget.item(i, 2).text() for i in range(self.tableWidget.rowCount())]

        class_numbers = sorted(
            set(login.split('-')[3] for login in logins))

        self.comboBox_2.clear()
        self.comboBox_2.insertItem(0, "")
        self.comboBox_2.addItems(class_numbers)

    def filterData(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.showRow(i)
            self.tableWidget.item(i, 2).setBackground(Qt.white)
            login = self.tableWidget.item(i, 2).text().split('-')
            if self.comboBox_2.currentText() != '' and self.comboBox.currentText() != '':
                if self.comboBox_2.currentText() != login[3] or self.comboBox.currentText() != login[2]:
                    self.tableWidget.hideRow(i)
            elif self.comboBox.currentText() != '':
                if self.comboBox.currentText() != login[2]:
                    self.tableWidget.hideRow(i)
            elif self.comboBox_2.currentText() != '':
                if self.comboBox_2.currentText() != login[3]:
                    self.tableWidget.hideRow(i)
        self.paintData()

    def paintData(self):
        id = [i for i in range(self.tableWidget.rowCount()) if
              self.tableWidget.isRowHidden(i) == False]
        scores = [self.tableWidget.item(i, 7).text() for i in range(self.tableWidget.rowCount()) if
                  self.tableWidget.isRowHidden(i) == False]

        data = list(zip(id, scores))

        data.sort(key=lambda x: int(x[1]), reverse=True)
        print(data)

        first_place_score = int(data[0][1])
        second_place_score = int(data[1][1])
        third_place_score = int(data[2][1])

        for i, (id, score) in enumerate(data):
            score = int(score)
            if score == first_place_score:
                self.tableWidget.item(id, 2).setBackground(Qt.red)
            elif score == second_place_score:
                self.tableWidget.item(id, 2).setBackground(Qt.green)
            elif score == third_place_score:
                self.tableWidget.item(id, 2).setBackground(Qt.blue)

    def resetTable(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.showRow(i)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.loadClassNumbers()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
