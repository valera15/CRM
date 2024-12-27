from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
QLineEdit, QPushButton, QStackedWidget, QCalendarWidget, QTableWidgetItem,
QHeaderView, QTableWidget, QComboBox, QScrollBar)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QComboBox, QLabel, QScrollBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QComboBox, QLabel, QScrollBar, QWidget, QToolBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor

class MainStackedWindow(QMainWindow):
    def __init__(self):
        super(MainStackedWindow, self).__init__()
        self.setWindowTitle("Шаги к счастью")
        self.setGeometry(0, 0, 1920, 1080)

        # Создаем стек виджетов
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Создаем окна
        self.main_window = MainWindow(self)
        self.second_window = SecondWindow(self)

        # Добавляем окна в стек
        self.central_widget.addWidget(self.main_window)
        self.central_widget.addWidget(self.second_window)

        # Устанавливаем начальное окно
        self.central_widget.setCurrentWidget(self.main_window)

    def switch_to_window(self, window):
        """Переключение на указанное окно"""
        if window not in [self.central_widget.widget(i) for i in range(self.central_widget.count())]:
            self.central_widget.addWidget(window)
        self.central_widget.setCurrentWidget(window)


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)

        self.parent = parent

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

        if login == "" and password == "":
            # Переключаемся на второе окно
            self.parent.switch_to_window(self.parent.second_window)
        else:
            self.login_input.clear()
            self.password_input.clear()
            self.login_input.setFocus()


class SecondWindow(QMainWindow):
    def __init__(self, parent):
        super(SecondWindow, self).__init__(parent)

        self.parent = parent

        # Заголовок
        self.title = QLabel(self)
        self.title.setText("Главная страница")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setGeometry(560, 50, 800, 150)
        self.title.setStyleSheet("font-size: 96px;")

        # Календарь
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(1000, 300, 800, 600)
        self.calendar.setStyleSheet("font-size: 24px;")
        self.calendar.setGridVisible(True)

        # Кнопка "Выйти"
        self.logout_button = QPushButton(self)
        self.logout_button.setText("Выйти")
        self.logout_button.setGeometry(1550, 100, 250, 50)
        self.logout_button.setStyleSheet("font-size: 24px;")
        self.logout_button.clicked.connect(self.logout)

        # Создаем квадратные кнопки
        self.create_square_buttons()

    def logout(self):
        # Переключаемся обратно на главное окно
        self.parent.switch_to_window(self.parent.main_window)

    def create_square_buttons(self):
        buttons = [
            ("Список\nтренеров", TrainerListWindow),
            ("Список\nнаправлений", DirectionListWindow),
            ("Список\nучеников", StudentListWindow),
            ("Расписание", ScheduleApp),
            ("Восстановление\nпропуска", PassRecoveryWindow),
            ("Регистрация\nученика", StudentRegistrationWindow),
            ("Продажа\nтренировки", TrainingSaleWindow),
            ("Пропускная\nсистема", AccessControlWindow),
        ]

        x, y = 100, 200
        for text, window_class in buttons:
            button = QPushButton(self)
            button.setText(text)
            button.setGeometry(x, y, 250, 150)
            button.setStyleSheet("font-size: 24px;")
            button.clicked.connect(lambda _, w=window_class: self.open_new_window(w))
            x += 300
            if x > 700:  # Переход на новую строку
                x = 100
                y += 300

    def open_new_window(self, window_class):
        new_window = window_class(self.parent)
        self.parent.switch_to_window(new_window)

    def logout(self):
        # Завершить приложение
        QApplication.quit()
    def logout(self):
        QApplication.quit()

class TrainerListWindow(QMainWindow):
    def __init__(self, parent):
        super(TrainerListWindow, self).__init__(parent)
        self.parent = parent

        # Центральный виджет и общий layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        self.title_label = QLabel("Список тренеров", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(self.title_label)

        # Верхний слой: строка поиска и кнопки
        top_layout = QHBoxLayout()

        # Строка поиска
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Поиск...")
        self.search_bar.setStyleSheet("font-size: 24px;")
        self.search_bar.setFixedWidth(300)
        self.search_bar.textChanged.connect(self.filter_table)
        top_layout.addWidget(self.search_bar)

        # Кнопка "Назад"
        self.back_button = QPushButton(self)
        self.back_button.setText("⟸")
        self.back_button.setStyleSheet("font-size: 24px; padding: 10px;")
        self.back_button.clicked.connect(lambda: self.parent.switch_to_window(self.parent.second_window))
        top_layout.addWidget(self.back_button)

        # Кнопки управления записями
        self.add_button = QPushButton("Добавить")
        self.add_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.add_button.clicked.connect(self.add_record)  # Подключить обработчик
        top_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Редактировать")
        self.edit_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.edit_button.clicked.connect(self.edit_record)  # Подключить обработчик
        top_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.delete_button.clicked.connect(self.delete_record)  # Подключить обработчик
        top_layout.addWidget(self.delete_button)

        # Добавление отступов
        top_layout.addStretch()
        main_layout.addLayout(top_layout)

        # Таблица
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Номер пропуска",
            "ФИО",
            "Дата рождения",
            "Номер телефона",
            "Направление",
            "Количество проведенных тренировок",
            "Численность учеников"
        ])
        self.table.setRowCount(10)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        # Заполнение таблицы тестовыми данными
        for row in range(10):
            for col in range(7):
                self.table.setItem(row, col, QTableWidgetItem(f"Данные {row + 1}-{col + 1}"))

    def filter_table(self):
        search_text = self.search_bar.text().lower()
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

    # Обработчики для кнопок управления записями
    def add_record(self):
        print("Добавить запись")  # Реализуйте добавление записи

    def edit_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Редактировать запись:", selected_items[0].text())  # Реализуйте редактирование записи
        else:
            print("Не выбрана запись для редактирования")

    def delete_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Удалить запись:", selected_items[0].text())  # Реализуйте удаление записи
        else:
            print("Не выбрана запись для удаления")


class DirectionListWindow(QMainWindow):
    def __init__(self, parent):
        super(DirectionListWindow, self).__init__(parent)
        self.parent = parent

        # Центральный виджет и общий layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        self.title_label = QLabel("Список направлений", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(self.title_label)

        # Верхний слой: строка поиска и кнопки
        top_layout = QHBoxLayout()

        # Строка поиска
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Поиск...")
        self.search_bar.setStyleSheet("font-size: 24px;")
        self.search_bar.setFixedWidth(300)
        self.search_bar.textChanged.connect(self.filter_table)
        top_layout.addWidget(self.search_bar)

        # Кнопка "Назад"
        self.back_button = QPushButton(self)
        self.back_button.setText("⟸")
        self.back_button.setStyleSheet("font-size: 24px; padding: 10px;")
        self.back_button.clicked.connect(lambda: self.parent.switch_to_window(self.parent.second_window))
        top_layout.addWidget(self.back_button)

        # Кнопки управления записями
        self.add_button = QPushButton("Добавить")
        self.add_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.add_button.clicked.connect(self.add_record)  # Подключить обработчик
        top_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Редактировать")
        self.edit_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.edit_button.clicked.connect(self.edit_record)  # Подключить обработчик
        top_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.delete_button.clicked.connect(self.delete_record)  # Подключить обработчик
        top_layout.addWidget(self.delete_button)

        # Добавление отступов
        top_layout.addStretch()
        main_layout.addLayout(top_layout)

        # Таблица
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([
            "ФИО тренера",
            "Направление",
            "Свободные места"
        ])
        self.table.setRowCount(10)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        # Заполнение таблицы тестовыми данными
        for row in range(10):
            for col in range(7):
                self.table.setItem(row, col, QTableWidgetItem(f"Данные {row + 1}-{col + 1}"))

    def filter_table(self):
        search_text = self.search_bar.text().lower()
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

    # Обработчики для кнопок управления записями
    def add_record(self):
        print("Добавить запись")  # Реализуйте добавление записи

    def edit_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Редактировать запись:", selected_items[0].text())  # Реализуйте редактирование записи
        else:
            print("Не выбрана запись для редактирования")

    def delete_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Удалить запись:", selected_items[0].text())  # Реализуйте удаление записи
        else:
            print("Не выбрана запись для удаления")

class StudentListWindow(QMainWindow):
    def __init__(self, parent):
        super(StudentListWindow, self).__init__(parent)
        self.parent = parent

        # Центральный виджет и общий layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        self.title_label = QLabel("Список учеников", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(self.title_label)

        # Верхний слой: строка поиска и кнопки
        top_layout = QHBoxLayout()

        # Строка поиска
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Поиск...")
        self.search_bar.setStyleSheet("font-size: 24px;")
        self.search_bar.setFixedWidth(300)
        self.search_bar.textChanged.connect(self.filter_table)
        top_layout.addWidget(self.search_bar)

        # Кнопка "Назад"
        self.back_button = QPushButton(self)
        self.back_button.setText("⟸")
        self.back_button.setStyleSheet("font-size: 24px; padding: 10px;")
        self.back_button.clicked.connect(lambda: self.parent.switch_to_window(self.parent.second_window))
        top_layout.addWidget(self.back_button)

        # Кнопки управления записями
        self.edit_button = QPushButton("Редактировать")
        self.edit_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.edit_button.clicked.connect(self.edit_record)  # Подключить обработчик
        top_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.setStyleSheet("font-size: 20px; padding: 5px;")
        self.delete_button.clicked.connect(self.delete_record)  # Подключить обработчик
        top_layout.addWidget(self.delete_button)

        # Добавление отступов
        top_layout.addStretch()
        main_layout.addLayout(top_layout)

        # Таблица
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Номер пропуска",
            "ФИО",
            "Дата рождения",
            "Номер телефона",
            "Направление и тренер",
            "Количество тренировок"
        ])
        self.table.setRowCount(10)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        # Заполнение таблицы тестовыми данными
        for row in range(10):
            for col in range(7):
                self.table.setItem(row, col, QTableWidgetItem(f"Данные {row + 1}-{col + 1}"))

    def filter_table(self):
        search_text = self.search_bar.text().lower()
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

    # Обработчики для кнопок управления записями
    def add_record(self):
        print("Добавить запись")  # Реализуйте добавление записи

    def edit_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Редактировать запись:", selected_items[0].text())  # Реализуйте редактирование записи
        else:
            print("Не выбрана запись для редактирования")

    def delete_record(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            print("Удалить запись:", selected_items[0].text())  # Реализуйте удаление записи
        else:
            print("Не выбрана запись для удаления")





class ScheduleApp(QMainWindow):
    def __init__(self, parent=None):
        super(ScheduleApp, self).__init__(parent)
        self.parent = parent  # Сохраняем родительское окно
        self.setWindowTitle("Расписание тренировок")
        self.showFullScreen()  # Включаем полноэкранный режим
        self.init_ui()

    def init_ui(self):
        # Основной лейаут
        main_layout = QHBoxLayout()  # Горизонтальный лейаут для размещения элементов слева и справа

        # Контейнер для кнопки "Назад" (в левый верхний угол)
        back_button = QPushButton("Назад")
        back_button.setFixedSize(100, 40)
        back_button.clicked.connect(self.on_back_button_click)

        # Размещаем кнопку в верхнем левом углу
        back_button_layout = QHBoxLayout()
        back_button_layout.setContentsMargins(0, 0, 0, 0)  # Убираем отступы
        back_button_layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Добавляем кнопку в основной лейаут
        main_layout.addLayout(back_button_layout)

        # Контейнер для таблицы расписания (слева)
        schedule_layout = QVBoxLayout()
        self.schedule_table = QTableWidget(8, 7)
        self.schedule_table.setHorizontalHeaderLabels(["пн", "вт", "ср", "чт", "пт", "сб", "вс"])
        self.schedule_table.setVerticalHeaderLabels(["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"])
        self.schedule_table.setSelectionMode(QTableWidget.SingleSelection)
        self.schedule_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.schedule_table.itemSelectionChanged.connect(self.update_schedule)

        # Увеличиваем размер таблицы расписания
        for col in range(7):  # 7 столбцов
            self.schedule_table.setColumnWidth(col, 120)  # Увеличиваем ширину столбцов

        # Увеличиваем высоту строк
        for row in range(8):  # 8 строк
            self.schedule_table.setRowHeight(row, 80)

        # Устанавливаем фиксированный размер таблицы
        self.schedule_table.setFixedSize(840, 640)  # Увеличиваем размер таблицы
        schedule_layout.addWidget(self.schedule_table)
        main_layout.addLayout(schedule_layout)

        # Контейнер для текста (по центру)
        text_layout = QVBoxLayout()

        # Для каждого комбобокса, метки и лейаута устанавливаем фиксированные размеры
        hall_layout = QHBoxLayout()
        self.hall_combo = QComboBox()
        self.hall_combo.addItems(["1", "2", "3"])
        hall_layout.addWidget(QLabel("№ зала"))
        hall_layout.addWidget(self.hall_combo)
        text_layout.addLayout(hall_layout)

        # Устанавливаем фиксированный размер для комбобокса
        self.hall_combo.setFixedSize(100, 30)

        pass_layout = QHBoxLayout()
        self.pass_combo = QComboBox()
        self.pass_combo.addItems(["100", "101", "102"])
        pass_layout.addWidget(QLabel("№ пропуска"))
        pass_layout.addWidget(self.pass_combo)
        text_layout.addLayout(pass_layout)

        # Устанавливаем фиксированный размер для комбобокса
        self.pass_combo.setFixedSize(100, 30)

        trainer_layout = QHBoxLayout()
        self.trainer_combo = QComboBox()
        self.trainer_combo.addItems(["Иванов", "Петров", "Сидоров"])
        trainer_layout.addWidget(QLabel("ФИО тренера"))
        trainer_layout.addWidget(self.trainer_combo)
        text_layout.addLayout(trainer_layout)

        # Устанавливаем фиксированный размер для комбобокса
        self.trainer_combo.setFixedSize(100, 30)

        # Устанавливаем фиксированный размер для меток
        for i in range(text_layout.count()):
            widget = text_layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                widget.setFixedSize(100, 30)  # Устанавливаем размер для меток

        text_layout.setContentsMargins(20, 20, 20, 20)  # Устанавливаем отступы
        text_layout.setSpacing(10)  # Интервал между элементами

        # Добавляем текстовый контейнер в основной лейаут
        main_layout.addLayout(text_layout)

        # Контейнер для таблицы тренеров (справа)
        extra_trainers_layout = QVBoxLayout()
        self.extra_trainers_table = QTableWidget(3, 2)
        self.extra_trainers_table.setHorizontalHeaderLabels(["ФИО тренера", "Цвет"])
        self.extra_trainers_table.setItem(0, 0, QTableWidgetItem("Иванов"))
        self.extra_trainers_table.setItem(0, 1, QTableWidgetItem("blue"))
        self.extra_trainers_table.setItem(1, 0, QTableWidgetItem("Петров"))
        self.extra_trainers_table.setItem(1, 1, QTableWidgetItem("green"))
        self.extra_trainers_table.setItem(2, 0, QTableWidgetItem("Сидоров"))
        self.extra_trainers_table.setItem(2, 1, QTableWidgetItem("red"))
        self.extra_trainers_table.setFixedWidth(200)  # Устанавливаем фиксированную ширину таблицы тренеров

        # Привязываем таблицу тренеров к верху
        extra_trainers_layout.addWidget(QLabel("Таблица тренеров (дублированная)"))
        extra_trainers_layout.addWidget(self.extra_trainers_table)

        # Устанавливаем фиксированный размер для таблицы тренеров
        self.extra_trainers_table.setFixedSize(200, 200)

        # Устанавливаем отступы для контейнера
        extra_trainers_layout.setContentsMargins(20, 20, 20, 20)
        extra_trainers_layout.setSpacing(10)

        # Устанавливаем фиксированный размер для контейнера с таблицей тренеров
        extra_trainers_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)

        # Добавляем контейнер с таблицей тренеров в основной лейаут
        main_layout.addLayout(extra_trainers_layout)

        # Контейнер для кнопки "Обновить" (в правый нижний угол)
        button_layout = QVBoxLayout()
        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(self.refresh_schedule)
        button_layout.addWidget(self.update_button)

        # Устанавливаем фиксированный размер для кнопки
        self.update_button.setFixedSize(100, 40)  # Пример для кнопки

        # Центрируем кнопку
        button_layout.setAlignment(Qt.AlignCenter)

        # Добавляем кнопку в правый нижний угол
        extra_trainers_layout.addLayout(button_layout)  # Добавляем кнопку в правую секцию

        # Центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Таймер для обновления
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_update_schedule)
        self.timer.start(3000)  # Обновление каждые 3 секунды

    def on_back_button_click(self):
        """Действие при нажатии на кнопку 'Назад'."""
        print("Кнопка 'Назад' нажата")
        if self.parent:
            self.parent.switch_to_window(self.parent.second_window)  # Возвращаемся на главное меню



    def update_schedule(self):
        selected_items = self.schedule_table.selectedItems()
        if selected_items:
            trainer = self.trainer_combo.currentText()
            color_name = self.get_trainer_color(trainer)
            for item in selected_items:
                current_color = item.background().color()
                if current_color == QColor(color_name):
                    item.setBackground(QColor("white"))
                else:
                    item.setBackground(QColor(color_name))
        else:
            print("Выберите ячейку в таблице расписания!")

    def auto_update_schedule(self):
        for row in range(self.schedule_table.rowCount()):
            for col in range(self.schedule_table.columnCount()):
                item = self.schedule_table.item(row, col)
                if item is None:
                    item = QTableWidgetItem()
                    self.schedule_table.setItem(row, col, item)

    def get_trainer_color(self, trainer):
        """Функция получения цвета тренера."""
        if trainer == "Иванов":
            return "blue"
        elif trainer == "Петров":
            return "green"
        elif trainer == "Сидоров":
            return "red"
        return None

    def refresh_schedule(self):
        """Обновление расписания."""
        print("Обновление расписания...")
        self.auto_update_schedule()



class PassRecoveryWindow(QMainWindow):
    def __init__(self, parent):
        super(PassRecoveryWindow, self).__init__(parent)
        self.parent = parent
        self.create_back_button()

class StudentRegistrationWindow(QMainWindow):
    def __init__(self, parent):
        super(StudentRegistrationWindow, self).__init__(parent)
        self.parent = parent
        self.create_back_button()

class TrainingSaleWindow(QMainWindow):
    def __init__(self, parent):
        super(TrainingSaleWindow, self).__init__(parent)
        self.parent = parent
        self.create_back_button()

class AccessControlWindow(QMainWindow):
    def __init__(self, parent):
        super(AccessControlWindow, self).__init__(parent)
        self.parent = parent
        self.create_back_button()

# Добавляем метод для кнопки "Назад"
def create_back_button(self):
    self.back_button = QPushButton(self)
    self.back_button.setText("⟸")
    self.back_button.setGeometry(50, 10, 80, 60)
    self.back_button.setStyleSheet("font-size: 48px;")
    self.back_button.clicked.connect(lambda: self.parent.switch_to_window(self.parent.second_window))


# Привязываем метод ко всем окнам
for cls in [TrainerListWindow, DirectionListWindow, StudentListWindow, ScheduleApp,
            PassRecoveryWindow, StudentRegistrationWindow, TrainingSaleWindow, AccessControlWindow]:
    cls.create_back_button = create_back_button


def application():
    app = QApplication(sys.argv)
    main_window = MainStackedWindow()
    main_window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
