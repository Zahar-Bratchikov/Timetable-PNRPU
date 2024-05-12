from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QComboBox, QDialog, QLineEdit, QPushButton
from PyQt5.QtCore import QCoreApplication, QRect
from timetable import Timetable
import requests
import os

# Словари для перевода русских названий в английские эквиваленты
GROUP_TRANSLATIONS = {
    "БМ": "BM",
    "ВМ": "VM",
    "ДПМ": "DPM",
    "ИВК": "IVK",
    "ИСТ": "IST",
    "ИТСИ": "ITSI",
    "МАК": "MAK",
    "МИЭ": "MIEH",
    "ММ": "MM",
    "МТВО": "MTVO",
    "ПМ": "PM",
    "ПМОН": "PMON",
    "ФОП": "FOP",
    "ХЕБИ": "KHEBI",
    "ЦТУ": "CTU"
}

EDUCATION_LEVEL_TRANSLATIONS = {
    "Бакалавриат": "b",
    "Магистратура": "m",
}

SEMESTER_TRANSLATIONS = {
    "Осенний": "osennijj",
    "Весенний": "vesennijj",
}

PERIOD_TRANSLATIONS = {
    "До смены": "do",
    "После смены": "posle",
}

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Расписание ПНИПУ")

        self.timetable = Timetable('timetable.xlsx', 'Лист1')
        self.ui.fill_table_data(self.timetable)


class Ui_MainWindow(object):
    def __init__(self):
        self.current_day = 0

    def setupUi(self, MainWindow):
        screen_resolution = QCoreApplication.instance().desktop().screenGeometry()
        screen_width = screen_resolution.width()
        screen_height = screen_resolution.height()

        # Устанавливаем размер окна в 2/3 от разрешения монитора
        window_width = int(screen_resolution.width() * 2 / 3)
        window_height = int(screen_resolution.height() * 2 / 3)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width, window_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Создаем QGridLayout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Таблица 1
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)  # Политика изменения размеров

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)

        # Кнопки и строка ввода
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)  # Делаем строку ввода только для чтения
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)  # Делаем строку ввода только для чтения
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)  # Делаем строку ввода только для чтения
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.hide()  # Скрываем календарь при инициализации
        self.calendarWidget.selectionChanged.connect(self.on_date_selected)

        self.gridLayout.addWidget(self.calendarWidget, 5, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.showEvent = self.resizeEvent
        # Подключаем событие изменения размера окна
        MainWindow.resizeEvent = self.resizeEvent

        self.pushButton.clicked.connect(self.next_day)
        self.pushButton_2.clicked.connect(self.previous_day)
        self.calendar = False
        self.pushButton_4.clicked.connect(self.show_calendar)
        self.pushButton_3.clicked.connect(self.show_group_dialog)
        self.current_date = QtCore.QDate.currentDate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Следующий день"))
        self.pushButton_2.setText(_translate("MainWindow", "Предыдущий день"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать группу"))
        self.pushButton_4.setText(_translate("MainWindow", "Показать календарь"))

    def fill_table_data(self, timetable):
        self.current_day = timetable.get_timetable()[1]
        self.current_week = self.current_day // 7
        self.lineEdit_2.setText(timetable.get_timetable()[2].replace(" ", ""))
        self.lineEdit_3.setText(timetable.get_timetable()[3])
        if self.current_week == 0:
            self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
        else:
            self.tableWidget.setHorizontalHeaderLabels(["Вторая неделя"])
        # Данные для таблиц
        self.timetable_arr = timetable.get_timetable()[0]

        # Заполнение таблицы 1
        self.tableWidget.setVerticalHeaderLabels(["8:00", "9:40", "11:30", "13:20", "15:00", "16:40"])

        # Установка таблицы только для чтения
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.update_day_label()

    # Обработчик события изменения размера окна
    def resizeEvent(self, event):
        # Установка высоты строк пропорционально размеру окна
        table_height = self.tableWidget.height()
        row_count = self.tableWidget.rowCount()
        row_height = int(table_height / row_count - 5)
        for row in range(row_count):
            self.tableWidget.setRowHeight(row, row_height)

    def next_day(self):
        self.current_day = (self.current_day + 1) % 14
        self.update_day_label()
        self.current_date = self.current_date.addDays(1)

    def previous_day(self):
        self.current_day = self.current_day - 1
        if self.current_day == -1:
            self.current_day = 13
        self.update_day_label()
        self.current_date = self.current_date.addDays(-1)


    def update_day_label(self):
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        self.lineEdit.setText(days_of_week[self.current_day % 7])
        data_week_1 = {
            "8:00": self.timetable_arr[0 + self.current_day * 6],
            "9:40": self.timetable_arr[1 + self.current_day * 6],
            "11:30": self.timetable_arr[2 + self.current_day * 6],
            "13:20": self.timetable_arr[3 + self.current_day * 6],
            "15:00": self.timetable_arr[4 + self.current_day * 6],
            "16:40": self.timetable_arr[5 + self.current_day * 6]
        }
        if self.current_day > 6:
            self.current_week = 1
        else:
            self.current_week = 0
        if self.current_week == 0:
            self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
        else:
            self.tableWidget.setHorizontalHeaderLabels(["Вторая неделя"])

        for row, (time, data) in enumerate(data_week_1.items()):
            text_item = QtWidgets.QTableWidgetItem(data)
            text_item.setTextAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
            self.tableWidget.setItem(row, 0, text_item)

    def show_calendar(self):
        self.calendar = not self.calendar
        self.calendarWidget.setVisible(self.calendar)
        QtCore.QTimer.singleShot(0, lambda: self.resizeEvent(None))
        if self.calendar:
            self.pushButton_4.setText("Скрыть календарь")
        else:
            self.pushButton_4.setText("Показать календарь")

    def show_group_dialog(self):
        dialog = GroupSelectionDialog(self.centralwidget.window())
        if dialog.exec_():
            group_data = dialog.get_group_data()
            if group_data:
                Group, Year, Number_of_group, Level_education, Season, time = group_data
                filename = download_excel_schedule(Group, Year, Number_of_group, Level_education, Season, time)
                if filename:
                    timetable = Timetable(filename, 'Лист1')
                    self.fill_table_data(timetable)
                    self.current_date = QtCore.QDate.currentDate()

    def on_date_selected(self):
        selected_date = self.calendarWidget.selectedDate()
        self.current_day = (self.current_day + self.current_date.daysTo(selected_date))%14
        self.current_date = selected_date
        self.update_day_label()


def download_excel_schedule(Group, Year, Number_of_group, Level_education, Season, time):
    # Сформировать URL на основе предоставленных параметров
    base_url = "https://pstu.ru/files/file/Abitur/timetable/"
    url = f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}%20-{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx"
    url2 = f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}%20%20-{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx"
    url3 = f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}-{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx"
    # Отправить GET-запрос для загрузки файла
    response = requests.get(url)

    if response.status_code == 200:
        # Определить путь для сохранения файла
        filename = f"timetable.xlsx"
        filepath = os.path.join(os.getcwd(), filename)

        # Записать содержимое файла
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath
    else:
        response = requests.get(url2)
        if response.status_code == 200:
            # Определить путь для сохранения файла
            filename = f"timetable.xlsx"
            filepath = os.path.join(os.getcwd(), filename)

            # Записать содержимое файла
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
        else:
            response = requests.get(url3)
            if response.status_code == 200:
                # Определить путь для сохранения файла
                filename = f"timetable.xlsx"
                filepath = os.path.join(os.getcwd(), filename)

                # Записать содержимое файла
                with open(filepath, "wb") as f:
                    f.write(response.content)
                return filepath
            else:
                QMessageBox.critical(None, "Ошибка", "Не удалось загрузить файл.", QMessageBox.Ok)
                return None


class GroupSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super(GroupSelectionDialog, self).__init__(parent)
        self.setWindowTitle("Выбор группы")
        self.layout = QtWidgets.QVBoxLayout(self)

        # Добавление выпадающего списка с группами
        self.group_combo = QComboBox(self)
        self.group_combo.addItems(GROUP_TRANSLATIONS.keys())
        self.layout.addWidget(self.group_combo)

        # Добавление элементов для ввода дополнительной информации
        self.year_line_edit = QLineEdit(self)
        self.year_line_edit.setPlaceholderText("Год поступления")
        self.layout.addWidget(self.year_line_edit)

        self.number_line_edit = QLineEdit(self)
        self.number_line_edit.setPlaceholderText("Номер группы")
        self.layout.addWidget(self.number_line_edit)

        self.level_combo = QComboBox(self)
        self.level_combo.addItems(EDUCATION_LEVEL_TRANSLATIONS.keys())
        self.layout.addWidget(self.level_combo)

        self.semester_combo = QComboBox(self)
        self.semester_combo.addItems(SEMESTER_TRANSLATIONS.keys())
        self.layout.addWidget(self.semester_combo)

        self.period_combo = QComboBox(self)
        self.period_combo.addItems(PERIOD_TRANSLATIONS.keys())
        self.layout.addWidget(self.period_combo)

        self.ok_button = QPushButton("ОК", self)
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)

    def get_group_data(self):
        russian_group = self.group_combo.currentText()
        english_group = GROUP_TRANSLATIONS.get(russian_group)
        year = self.year_line_edit.text()
        number = self.number_line_edit.text()
        russian_level = self.level_combo.currentText()
        english_level = EDUCATION_LEVEL_TRANSLATIONS.get(russian_level)
        russian_semester = self.semester_combo.currentText()
        english_semester = SEMESTER_TRANSLATIONS.get(russian_semester)
        russian_period = self.period_combo.currentText()
        english_period = PERIOD_TRANSLATIONS.get(russian_period)

        if year and number and english_group and english_level and english_semester and english_period:
            return english_group, year, number, english_level, english_semester, english_period
        else:
            return None
