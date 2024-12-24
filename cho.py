from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCalendarWidget
import sys
import datetime


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
        try:
            # Закрытие текущего окна перед открытием нового
            self.close()
            self.new_window = SecondWindow()  # Создаём новое окно
            self.new_window.showFullScreen()  # Показываем новое окно
        except Exception as e:
            print(f"Ошибка при открытии нового окна: {e}")
            QApplication.quit()  # Завершаем программу в случае ошибки


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.setWindowTitle("Главная страница")
        self.setGeometry(0, 0, 1920, 1080)

        # Заголовок
        self.title = QLabel(self)
        self.title.setText("Главная страница")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setGeometry(560, 50, 800, 150)  # Сдвигаем правее, увеличиваем ширину и высоту
        self.title.setStyleSheet("font-size: 96px;")  # Увеличиваем размер шрифта

        # Календарь
        self.create_calendar()

        # Кнопка "Выйти из системы"
        self.logout_button = QPushButton(self)
        self.logout_button.setText("Выйти из системы")
        self.logout_button.setGeometry(1550, 100, 250, 50)
        self.logout_button.setStyleSheet("font-size: 24px;")
        self.logout_button.clicked.connect(self.logout)

        # Создание кнопок с многосрочным текстом
        self.create_square_buttons()

        # Текущее время
        self.create_time_label()

        # Обновление времени каждую секунду
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Обновление каждую секунду

    def create_square_buttons(self):
        buttons = [
            ("Список\nтренеров", 100, 200, TrainerListWindow),
            ("Список\nнаправлений", 400, 200, DirectionListWindow),
            ("Список\nучеников", 700, 200, StudentListWindow),
            ("Расписание", 100, 500, ScheduleWindow),
            ("Восстановление\nпропуска", 400, 500, PassRecoveryWindow),
            ("Регистрация\nученика", 700, 500, StudentRegistrationWindow),
            ("Продажа\nтренировки", 100, 800, TrainingSaleWindow),
            ("Пропускная\nсистема", 400, 800, AccessControlWindow),
        ]

        for text, x, y, window_class in buttons:
            button = QPushButton(self)
            button.setText(text)

            if text == "Пропускная\nсистема":
                button.setGeometry(x, y, 550, 250)  # Увеличиваем ширину кнопки "Пропускная система"
            else:
                button.setGeometry(x, y, 250, 250)  # Оставляем остальные кнопки стандартными

            button.setStyleSheet("font-size: 24px; white-space: pre-wrap;")  # Включаем перенос текста
            button.clicked.connect(lambda _, w=window_class: self.open_new_window(w))

    def open_new_window(self, window_class):
        self.new_window = window_class()
        self.new_window.show()

    def create_calendar(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(1000, 300, 800, 600)  # Сдвигаем календарь ближе к кнопкам
        self.calendar.setStyleSheet("font-size: 24px;")
        self.calendar.setGridVisible(True)

        # Скрыть номера недель с помощью изменения стиля
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        # Убедитесь, что размер календаря подходящий
        self.calendar.setFixedSize(800, 600)  # Устанавливаем фиксированный размер календаря

        self.calendar.setSelectedDate(QtCore.QDate.currentDate())

    def create_time_label(self):
        self.time_label = QLabel(self)
        self.time_label.setGeometry(1250, 200, 300, 100)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 72px;")
        self.update_time()  # Сразу отображаем актуальное время

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Получаем актуальное время
        self.time_label.setText(current_time)

    def logout(self):
        QApplication.quit()  # Закрывает все окна и завершает приложение


class TrainerListWindow(QMainWindow):
    def __init__(self):
        super(TrainerListWindow, self).__init__()
        self.setWindowTitle("Список тренеров")


class DirectionListWindow(QMainWindow):
    def __init__(self):
        super(DirectionListWindow, self).__init__()
        self.setWindowTitle("Список направлений")


class StudentListWindow(QMainWindow):
    def __init__(self):
        super(StudentListWindow, self).__init__()
        self.setWindowTitle("Список учеников")


class ScheduleWindow(QMainWindow):
    def __init__(self):
        super(ScheduleWindow, self).__init__()
        self.setWindowTitle("Расписание")


class PassRecoveryWindow(QMainWindow):
    def __init__(self):
        super(PassRecoveryWindow, self).__init__()
        self.setWindowTitle("Восстановление пропуска")


class StudentRegistrationWindow(QMainWindow):
    def __init__(self):
        super(StudentRegistrationWindow, self).__init__()
        self.setWindowTitle("Регистрация ученика")


class TrainingSaleWindow(QMainWindow):
    def __init__(self):
        super(TrainingSaleWindow, self).__init__()
        self.setWindowTitle("Продажа тренировки")


class AccessControlWindow(QMainWindow):
    def __init__(self):
        super(AccessControlWindow, self).__init__()
        self.setWindowTitle("Пропускная система")


def application():
    try:
        app = QApplication(sys.argv)
        win = MainWindow()

        win.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Ошибка в приложении: {e}")
        sys.exit(1)  # Завершаем приложение с кодом ошибки


if __name__ == "__main__":
    application()
