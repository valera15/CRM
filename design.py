from PyQt5 import QtWidgets # из PyQt5 импортируем класс QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow # QApplication - приложение, QMainWindow - окно
import sys

def application():
    app = QApplication(sys.argv) # создание приложения в целом (настройки для компьютера)
    window = QMainWindow()

    window.setWindowTitle("Шаги к счастью")
    window.setGeometry(300, 250, 350, 200)

    window.show()
    sys.exit(app.exec_()) # корректный выход из программы

if __name__ == "__main__":
    application()