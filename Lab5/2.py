import datetime
import sqlite3
import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QLineEdit, QPushButton, QGridLayout, \
    QLabel, QComboBox, QMessageBox
from PyQt5.uic.uiparser import QtWidgets, QtCore

from ui2 import Ui_MainWindow

class Dialog(QDialog):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить запись")

        # Создаем поля ввода для каждого столбца таблицы
        self.title_line = QLineEdit(data[1] if data else '')
        self.year_line = QLineEdit()
        self.duration_line = QLineEdit(data[2] if data else '')
        self.genre_combo = QComboBox()

        # Получаем список жанров из базы данных и заполняем ComboBox
        self.connection = sqlite3.connect("films_db.sqlite")
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title FROM genres")
        genres = cursor.fetchall()
        for genre in genres:
            self.genre_combo.addItem(genre[1], genre[0])

        # Устанавливаем выбранный элемент в соответствии с текущим значением жанра в записи
        index = self.genre_combo.findData(data[3] if data else '')
        if index >= 0:
            self.genre_combo.setCurrentIndex(index)

        # Создаем кнопки "Сохранить" и "Отмена"
        self.add_button = QPushButton("Сохранить")
        self.cancel_button = QPushButton("Отмена")
        self.add_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # Создаем сетку для размещения элементов управления
        layout = QGridLayout()
        layout.addWidget(QLabel("Название фильма:"), 0, 0)
        layout.addWidget(self.title_line, 0, 1)
        layout.addWidget(QLabel("Год:"), 1, 0)
        layout.addWidget(self.year_line, 1, 1)
        layout.addWidget(QLabel("Продолжительность:"), 2, 0)
        layout.addWidget(self.duration_line, 2, 1)
        layout.addWidget(QLabel("Жанр:"), 3, 0)
        layout.addWidget(self.genre_combo, 3, 1)
        layout.addWidget(self.add_button, 4, 0)
        layout.addWidget(self.cancel_button, 4, 1)

        self.setLayout(layout)

    def accept(self):
        # Проверяем корректность года
        try:
            year = int(self.year_line.text())
            duration = int(self.duration_line.text())
            if year > datetime.datetime.now().year:
                raise ValueError("Неверно введён год!")
            if duration < 0:
                raise ValueError("Неверно введена длительность! ")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))
            return

        # Вызываем родительский метод accept() для закрытия диалога
        super().accept()

    def get_data(self):
        # Получаем данные из полей ввода
        title = self.title_line.text()
        year = self.year_line.text()
        duration = self.duration_line.text()
        genre = self.genre_combo.currentData()

        return (title, year, duration, genre)
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("films_db.sqlite")
        self.populate_table("SELECT films.id, films.title, films.duration, genres.title\
                                    FROM films JOIN genres ON films.genre == genres.id")
        self.add.clicked.connect(self.add_record)
        self.edit.clicked.connect(self.edit_record)
    def populate_table(self, query, values=None):
        cursor = self.connection.cursor()
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)

        name_of_columns = [e[0] for e in cursor.description]
        self.tableWidget.setColumnCount(len(name_of_columns))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(name_of_columns)

        for i, row in enumerate(cursor):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add_record(self):
        dialog = Dialog(None, self)
        if dialog.exec_():
            title, year, duration, genre = dialog.get_data()

            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO films (title, year, duration, genre) VALUES (?, ?, ?, ?)", (title, year, duration, genre))
            self.connection.commit()

            self.populate_table("SELECT films.id, films.title, films.duration, genres.title\
                                                FROM films JOIN genres ON films.genre == genres.id")

    def edit_record(self):
        cursor = self.connection.cursor()
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return

        data = [cursor.execute("SELECT films.id, films.title, films.duration, genres.title\
                                                FROM films WHERE films.id=?", self.tableWidget.item(selected_row, 0).text())[i] for i in range(4)]
        dialog = Dialog(data, self)
        if dialog.exec_():
            title, duration, genre = dialog.get_data()

            cursor.execute("UPDATE films SET title=?, duration=?, genre=? WHERE id=?",
                           (title, duration, genre, data[0]))
            self.connection.commit()

            self.populate_table("SELECT films.id, films.title, films.duration, genres.title\
                                                            FROM films JOIN genres ON films.genre == genres.id")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())