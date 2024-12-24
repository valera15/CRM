from PyQt5 import QtWidgets, QtCore  # из PyQt5 импортируем класс QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow  # QApplication - приложение, QMainWindow - окно
import sys


class Window(QMainWindow):
    def __init__(self):  # конструктор
        super(Window, self).__init__()

        self.setWindowTitle("Шаги к счастью")
        # self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Войти в систему")
        # self.main_text.move(100, 100)
        # self.main_text.setGeometry(QtCore.QRect(1000, 100, 1000, 500))
        # self.main_text.setFixedWidth(1000) # размер надписи
        self.main_text.adjustSize()  # подстраивается под длину надписи (когда не влезает)

        self.btn_vhod = QtWidgets.QPushButton(self)
        self.btn_vhod.move(70, 150)
        self.btn_vhod.setText("Войти")
        # self.btn_vhod.setFixedWidth(200)
        self.btn_vhod.clicked.connect(self.add_label)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(10, 10)
        self.btn_exit.setText("Выйти из системы")
        # self.btn_exit.setFixedWidth(200)  # ширина кнопки
        self.btn_exit.adjustSize()
        self.btn_exit.clicked.connect(self.click_exit)

    def add_label(self):
        self.new_text.setText("Добро пожаловать!")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

    def click_exit(self):  # Метод для выхода
        self.close()  # Закрывает окно и завершает программу


def application():
    app = QApplication(sys.argv)  # создание приложения в целом (настройки для компьютера)
    win = Window()

    win.showFullScreen()  # показывает окно
    sys.exit(app.exec_())  # корректный выход из программы


if __name__ == "__main__":
    application()