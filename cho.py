from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Шаги к счастью")
        self.setGeometry(0, 0, 1920, 1080)

        # Заголовок
        self.main_text = QLabel(self)
        self.main_text.setText("Войти в систему")
        self.main_text.setAlignment(QtCore.Qt.AlignCenter)
        self.main_text.setGeometry(460, 100, 1000, 200)
        self.main_text.setStyleSheet("font-size: 96px;")

        # Поле для ввода логина
        self.login_label = QLabel(self)
        self.login_label.setText("Логин")
        self.login_label.setAlignment(QtCore.Qt.AlignRight)
        self.login_label.setGeometry(560, 350, 300, 100)
        self.login_label.setStyleSheet("font-size: 72px;")

        self.login_input = QLineEdit(self)
        self.login_input.setGeometry(880, 350, 500, 100)
        self.login_input.setStyleSheet("font-size: 72px;")

        # Поле для ввода пароля
        self.password_label = QLabel(self)
        self.password_label.setText("Пароль")
        self.password_label.setAlignment(QtCore.Qt.AlignRight)
        self.password_label.setGeometry(560, 500, 300, 100)
        self.password_label.setStyleSheet("font-size: 72px;")

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(880, 500, 500, 100)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("font-size: 72px;")

        # Кнопка входа
        self.btn_vhod = QPushButton(self)
        self.btn_vhod.setText("Войти")
        self.btn_vhod.setGeometry(810, 650, 400, 150)
        self.btn_vhod.setStyleSheet("font-size: 72px;")
        self.btn_vhod.clicked.connect(self.validate_login)

    def validate_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if login == "abc" and password == "123":
            self.open_new_window()
        else:
            # Очищаем поля для ввода
            self.login_input.clear()
            self.password_input.clear()

            # Ставим фокус на поле логина для нового ввода
            self.login_input.setFocus()

    def open_new_window(self):
        self.new_window = SecondWindow()
        self.new_window.showFullScreen()
        self.close()

class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.setWindowTitle("Добро пожаловать!")
        self.setGeometry(0, 0, 1920, 1080)

        welcome_label = QLabel(self)
        welcome_label.setText("Добро пожаловать в систему!")
        welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        welcome_label.setGeometry(460, 400, 1000, 200)
        welcome_label.setStyleSheet("font-size: 96px;")

def application():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()