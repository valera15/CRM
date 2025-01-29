from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QComboBox, QSpinBox, QCheckBox, QScrollBar, QToolBar,
    QStackedWidget, QCalendarWidget, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import sys



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
        self.main_text.setAlignment(Qt.AlignCenter)
        self.main_text.setGeometry(460, 100, 1000, 200)
        self.main_text.setStyleSheet("font-size: 96px;")

        # Поле для ввода логина
        self.login_label = QLabel(self)
        self.login_label.setText("Логин")
        self.main_text.setAlignment(Qt.AlignCenter)
        self.login_label.setGeometry(560, 350, 300, 100)
        self.login_label.setStyleSheet("font-size: 72px;")

        self.login_input = QLineEdit(self)
        self.login_input.setGeometry(880, 350, 500, 100)
        self.login_input.setStyleSheet("font-size: 72px;")

        # Поле для ввода пароля
        self.password_label = QLabel(self)
        self.password_label.setText("Пароль")
        self.main_text.setAlignment(Qt.AlignCenter)
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
        self.title.setAlignment(Qt.AlignCenter)
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
    def __init__(self, parent=None):
        super(PassRecoveryWindow, self).__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # Настройка главного виджета
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создание кнопки "Назад"
        back_button = QPushButton("Назад", self)
        back_button.setStyleSheet("font-size: 28px;")  # Увеличенный шрифт
        back_button.setFixedWidth(200)  # Увеличенная ширина
        back_button.setFixedHeight(50)  # Увеличенная высота
        back_button.clicked.connect(self.go_back)  # Обработчик нажатия

        # Создание заголовка
        title_label = QLabel("Восстановление пропуска", self)
        title_label.setStyleSheet("font-size: 72px; font-weight: bold;")  # Увеличенный шрифт
        title_label.setAlignment(Qt.AlignCenter)

        # Поле для ввода ФИО
        fio_label = QLabel("ФИО ученика:", self)
        fio_label.setStyleSheet("font-size: 24px;")
        self.fio_input = QLineEdit(self)
        self.fio_input.setFixedWidth(600)
        self.fio_input.setFixedHeight(50)
        self.fio_input.setStyleSheet("font-size: 24px;")

        # Поле для ввода номера пропуска
        pass_label = QLabel("Номер потерянного пропуска:", self)
        pass_label.setStyleSheet("font-size: 24px;")
        self.pass_input = QLineEdit(self)
        self.pass_input.setFixedWidth(600)
        self.pass_input.setFixedHeight(50)
        self.pass_input.setStyleSheet("font-size: 24px;")

        # Поле для ввода номера телефона
        phone_label = QLabel("Номер телефона:", self)
        phone_label.setStyleSheet("font-size: 24px;")
        self.phone_input = QLineEdit(self)
        self.phone_input.setFixedWidth(600)
        self.phone_input.setFixedHeight(50)
        self.phone_input.setStyleSheet("font-size: 24px;")

        # Кнопка для поиска
        find_button = QPushButton("Найти", self)
        find_button.setStyleSheet("font-size: 28px;")  # Увеличенный шрифт
        find_button.setFixedWidth(400)  # Увеличенная ширина
        find_button.setFixedHeight(70)  # Увеличенная высота
        find_button.clicked.connect(self.on_find_clicked)  # Обработчик нажатия

        # Расположение виджетов в сетке
        layout = QGridLayout()
        layout.addWidget(fio_label, 0, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.fio_input, 0, 1, alignment=Qt.AlignLeft)
        layout.addWidget(pass_label, 1, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.pass_input, 1, 1, alignment=Qt.AlignLeft)
        layout.addWidget(phone_label, 2, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.phone_input, 2, 1, alignment=Qt.AlignLeft)
        layout.addWidget(find_button, 3, 0, 1, 2, alignment=Qt.AlignCenter)

        # Верхний контейнер для кнопки "Назад" и заголовка
        top_layout = QVBoxLayout()
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.addStretch()
        top_layout.addLayout(back_button_layout)
        top_layout.addWidget(title_label)  # Размещение заголовка
        top_layout.addStretch()  # Добавляем пространство снизу

        # Основной контейнер
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)  # Верхняя часть
        main_layout.addLayout(layout)  # Основная форма
        main_layout.addStretch()

        # Установка контейнера как основного макета
        central_widget.setLayout(main_layout)

    def go_back(self):
        if self.parent:
            self.parent.switch_to_window(self.parent.second_window)  # Возвращаемся на главное меню

    def on_find_clicked(self):
        fio = self.fio_input.text().strip()
        pass_number = self.pass_input.text().strip()
        phone_number = self.phone_input.text().strip()

        if fio or pass_number or phone_number:
            print(f"Поиск информации по введённым данным:\nФИО: {fio}\nПропуск: {pass_number}\nТелефон: {phone_number}")
        else:
            print("Ошибка: все поля пустые. Введите хотя бы одно значение.")


class StudentRegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(StudentRegistrationWindow, self).__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # Настройка главного виджета
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создание кнопки "Назад"
        back_button = QPushButton("Назад", self)
        back_button.setStyleSheet("font-size: 28px;")  # Увеличенный шрифт
        back_button.setFixedWidth(200)  # Увеличенная ширина
        back_button.setFixedHeight(50)  # Увеличенная высота
        back_button.clicked.connect(self.go_back)  # Обработчик нажатия

        # Создание заголовка
        title_label = QLabel("Регистрация ученика", self)
        title_label.setStyleSheet("font-size: 72px; font-weight: bold;")  # Увеличенный шрифт
        title_label.setAlignment(Qt.AlignCenter)

        # Создание остальных виджетов
        fio_label = QLabel("ФИО ученика:", self)
        fio_label.setStyleSheet("font-size: 24px;")
        self.fio_input = QLineEdit(self)
        self.fio_input.setFixedWidth(600)
        self.fio_input.setFixedHeight(50)
        self.fio_input.setStyleSheet("font-size: 24px;")

        birthdate_label = QLabel("Дата рождения:", self)
        birthdate_label.setStyleSheet("font-size: 24px;")
        self.birthdate_input = QLineEdit(self)
        self.birthdate_input.setFixedWidth(600)
        self.birthdate_input.setFixedHeight(50)
        self.birthdate_input.setStyleSheet("font-size: 24px;")

        phone_label = QLabel("Номер телефона:", self)
        phone_label.setStyleSheet("font-size: 24px;")
        self.phone_input = QLineEdit(self)
        self.phone_input.setFixedWidth(600)
        self.phone_input.setFixedHeight(50)
        self.phone_input.setStyleSheet("font-size: 24px;")

        pass_label = QLabel("Номер нового пропуска:", self)
        pass_label.setStyleSheet("font-size: 24px;")
        self.pass_input = QLineEdit(self)
        self.pass_input.setFixedWidth(600)
        self.pass_input.setFixedHeight(50)
        self.pass_input.setStyleSheet("font-size: 24px;")

        register_button = QPushButton("Зарегистрировать", self)
        register_button.setStyleSheet("font-size: 28px;")  # Увеличенный шрифт
        register_button.setFixedWidth(400)  # Увеличенная ширина
        register_button.setFixedHeight(70)  # Увеличенная высота

        # Расположение виджетов в сетке
        layout = QGridLayout()
        layout.addWidget(fio_label, 0, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.fio_input, 0, 1, alignment=Qt.AlignLeft)
        layout.addWidget(birthdate_label, 1, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.birthdate_input, 1, 1, alignment=Qt.AlignLeft)
        layout.addWidget(phone_label, 2, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.phone_input, 2, 1, alignment=Qt.AlignLeft)
        layout.addWidget(pass_label, 3, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.pass_input, 3, 1, alignment=Qt.AlignLeft)
        layout.addWidget(register_button, 4, 0, 1, 2, alignment=Qt.AlignCenter)

        # Верхний контейнер для кнопки "Назад" и заголовка
        top_layout = QVBoxLayout()
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.addStretch()
        top_layout.addLayout(back_button_layout)
        top_layout.addWidget(title_label)  # Размещение заголовка
        top_layout.addStretch()  # Добавляем пространство снизу

        # Основной контейнер
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)  # Верхняя часть
        main_layout.addLayout(layout)  # Основная форма
        main_layout.addStretch()

        # Установка контейнера как основного макета
        central_widget.setLayout(main_layout)

    def go_back(self):
        if self.parent:
            self.parent.switch_to_window(self.parent.second_window)  # Возвращаемся на главное меню

class TrainingSaleWindow(QWidget):
    def __init__(self, parent=None):
        super(TrainingSaleWindow, self).__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # Настройка окна
        self.setWindowTitle("Продажа тренировок")

        # Создание кнопки "Назад"
        back_button = QPushButton("\u2190 Назад", self)
        back_button.setStyleSheet("font-size: 18px;")
        back_button.setFixedWidth(150)
        back_button.setFixedHeight(50)
        back_button.clicked.connect(self.go_back)

        # Создание заголовка
        title_label = QLabel("Продажа тренировок", self)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        # Создание виджетов формы
        direction_label = QLabel("Направление:", self)
        direction_label.setStyleSheet("font-size: 24px;")
        self.direction_combo = QComboBox(self)
        self.direction_combo.addItems(["...", "Йога", "Фитнес", "Бокс"])
        self.direction_combo.setFixedWidth(200)
        self.direction_combo.setFixedHeight(50)
        self.direction_combo.setStyleSheet("font-size: 24px;")

        trainer_label = QLabel("ФИО тренера:", self)
        trainer_label.setStyleSheet("font-size: 24px;")
        self.trainer_combo = QComboBox(self)
        self.trainer_combo.addItems(["...", "Иванов И.И.", "Петров П.П.", "Сидоров С.С."])
        self.trainer_combo.setFixedWidth(200)
        self.trainer_combo.setFixedHeight(50)
        self.trainer_combo.setStyleSheet("font-size: 24px;")

        count_label = QLabel("Количество тренировок:", self)
        count_label.setStyleSheet("font-size: 24px;")
        self.count_spin = QSpinBox(self)
        self.count_spin.setRange(1, 100)
        self.count_spin.valueChanged.connect(self.update_total)
        self.count_spin.setFixedWidth(150)
        self.count_spin.setFixedHeight(50)
        self.count_spin.setStyleSheet("font-size: 24px;")

        pass_label = QLabel("Номер пропуска:", self)
        pass_label.setStyleSheet("font-size: 24px;")
        self.pass_input = QLineEdit(self)
        self.pass_input.setFixedWidth(300)
        self.pass_input.setFixedHeight(50)
        self.pass_input.setStyleSheet("font-size: 24px;")

        total_label = QLabel("ИТОГО:", self)
        total_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.total_display = QLineEdit(self)
        self.total_display.setReadOnly(True)
        self.total_display.setFixedWidth(300)
        self.total_display.setFixedHeight(50)
        self.total_display.setStyleSheet("font-size: 24px;")

        sell_button = QPushButton("Продать", self)
        sell_button.setStyleSheet("font-size: 28px;")
        sell_button.setFixedWidth(200)
        sell_button.setFixedHeight(70)

        # Макет для формы
        form_layout = QGridLayout()
        form_layout.addWidget(direction_label, 0, 0, alignment=Qt.AlignRight)
        form_layout.addWidget(self.direction_combo, 0, 1, alignment=Qt.AlignLeft)
        form_layout.addWidget(trainer_label, 0, 2, alignment=Qt.AlignRight)
        form_layout.addWidget(self.trainer_combo, 0, 3, alignment=Qt.AlignLeft)
        form_layout.addWidget(count_label, 0, 4, alignment=Qt.AlignRight)
        form_layout.addWidget(self.count_spin, 0, 5, alignment=Qt.AlignLeft)
        form_layout.addWidget(pass_label, 1, 0, 1, 1, alignment=Qt.AlignRight)
        form_layout.addWidget(self.pass_input, 1, 1, 1, 2, alignment=Qt.AlignLeft)
        form_layout.addWidget(total_label, 1, 3, alignment=Qt.AlignRight)
        form_layout.addWidget(self.total_display, 1, 4, 1, 2, alignment=Qt.AlignLeft)
        form_layout.addWidget(sell_button, 2, 0, 1, 6, alignment=Qt.AlignCenter)

        # Верхний макет с кнопкой "Назад" и заголовком
        top_layout = QVBoxLayout()
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.addStretch()
        top_layout.addLayout(back_button_layout)
        top_layout.addWidget(title_label)
        top_layout.addStretch()

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(form_layout)
        main_layout.addStretch()

        # Установка главного макета
        self.setLayout(main_layout)

    def update_total(self):
        """Обновление итоговой стоимости тренировки."""
        price_per_session = 300
        count = self.count_spin.value()
        total = count * price_per_session
        self.total_display.setText(str(total))

    def go_back(self):
        """Переход к предыдущему окну."""
        if self.parent:
            self.parent.switch_to_window(self.parent.second_window)



class AccessControlWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AccessControlWindow, self).__init__(parent)
        self.parent = parent  # Родительское окно
        self.init_ui()

    def init_ui(self):
        # Заголовок окна
        self.title_label = QLabel("Пропускная система")
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedHeight(120)

        # Кнопка "Назад"
        back_button = QPushButton("Назад", self)
        back_button.setStyleSheet("font-size: 28px;")
        back_button.setFixedSize(150, 50)
        back_button.clicked.connect(self.go_back)

        # Поле "Направление"
        self.direction_label = QLabel("Направление")
        self.direction_label.setStyleSheet("font-size: 28px;")
        self.direction_combo = QComboBox()
        self.direction_combo.addItems(["...", "Фитнес", "Йога", "Бокс"])
        self.direction_combo.setFixedSize(300, 50)

        # Поле "ФИО тренера"
        self.trainer_label = QLabel("ФИО тренера")
        self.trainer_label.setStyleSheet("font-size: 28px;")
        self.trainer_combo = QComboBox()
        self.trainer_combo.addItems(["...", "Иванов И.И.", "Петров П.П.", "Сидоров С.С."])
        self.trainer_combo.setFixedSize(300, 50)

        # Поле "Количество тренировок"
        training_label = QLabel("Количество тренировок")
        training_label.setStyleSheet("font-size: 28px;")
        self.training_spin = QSpinBox()
        self.training_spin.setMinimum(0)
        self.training_spin.setMaximum(100)
        self.training_spin.setValue(1)
        self.training_spin.setFixedSize(100, 50)

        # Поле "Номер пропуска"
        pass_number_label = QLabel("Номер пропуска")
        pass_number_label.setStyleSheet("font-size: 28px;")
        self.pass_number_input = QLineEdit()
        self.pass_number_input.setFixedSize(300, 50)

        # Чекбокс "Тренер"
        self.trainer_checkbox = QCheckBox("Тренер")
        self.trainer_checkbox.setStyleSheet("font-size: 28px;")
        self.trainer_checkbox.setFixedSize(150, 50)
        self.trainer_checkbox.stateChanged.connect(self.toggle_trainer_fields)

        # Кнопка "Продать"
        sell_button = QPushButton("Продать")
        sell_button.setStyleSheet("font-size: 28px;")
        sell_button.setFixedSize(200, 60)

        # Компоновка элементов
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Поля ввода в горизонтальных блоках
        form_layout = QGridLayout()
        form_layout.setAlignment(Qt.AlignCenter)
        form_layout.setHorizontalSpacing(20)
        form_layout.setVerticalSpacing(20)

        form_layout.addWidget(self.direction_label, 0, 0, Qt.AlignCenter)
        form_layout.addWidget(self.direction_combo, 0, 1, Qt.AlignCenter)

        form_layout.addWidget(self.trainer_label, 1, 0, Qt.AlignCenter)
        form_layout.addWidget(self.trainer_combo, 1, 1, Qt.AlignCenter)

        form_layout.addWidget(training_label, 2, 0, Qt.AlignCenter)
        form_layout.addWidget(self.training_spin, 2, 1, Qt.AlignCenter)

        form_layout.addWidget(pass_number_label, 3, 0, Qt.AlignCenter)
        form_layout.addWidget(self.pass_number_input, 3, 1, Qt.AlignCenter)

        form_layout.addWidget(self.trainer_checkbox, 4, 0, 1, 2, Qt.AlignCenter)

        # Добавляем кнопки
        button_layout = QHBoxLayout()
        button_layout.addWidget(sell_button)
        button_layout.setAlignment(Qt.AlignCenter)

        # Основной layout
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()

        top_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        top_layout.addStretch()

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.title_label, alignment=Qt.AlignTop | Qt.AlignCenter)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        # Центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Установка главного окна
        self.setCentralWidget(central_widget)

    def toggle_trainer_fields(self):
        """Скрытие или отображение полей и меток "Направление" и "ФИО тренера"."""
        is_trainer_checked = self.trainer_checkbox.isChecked()
        self.direction_label.setVisible(not is_trainer_checked)
        self.direction_combo.setVisible(not is_trainer_checked)
        self.trainer_label.setVisible(not is_trainer_checked)
        self.trainer_combo.setVisible(not is_trainer_checked)

    def go_back(self):
        """Возврат к предыдущему окну."""
        if self.parent:
            print("Переход на предыдущее окно...")
            self.parent.switch_to_window(self.parent.second_window)
        else:
            print("Родительское окно не задано.")






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
