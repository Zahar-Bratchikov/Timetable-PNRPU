from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
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

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)

        # Кнопки и строка ввода
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.hide()  # Скрываем календарь при инициализации

        self.gridLayout.addWidget(self.calendarWidget, 4, 0, 1, 2)

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
        self.calendar = 0
        self.pushButton_4.clicked.connect(self.show_calendar)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Следующий день"))
        self.pushButton_2.setText(_translate("MainWindow", "Предыдущий день"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать группу"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать день"))
        self.lineEdit.setText(_translate("MainWindow", ""))

    def fill_table_data(self, timetable):
        self.current_day = timetable.get_timetable()[2]
        self.current_week = (timetable.get_timetable()[1] + 1) % 2
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
        self.current_day = (self.current_day + 1) % 12
        self.update_day_label()
        if self.current_day % 6 == 0:
            self.current_week = (self.current_week + 1) % 2
            if self.current_week == 0:
                self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
            else:
                self.tableWidget.setHorizontalHeaderLabels(["Вторая неделя"])

    def previous_day(self):
        self.current_day = (self.current_day - 1) % 12
        if self.current_day == -1:
            self.current_day = 11
        self.update_day_label()
        if self.current_day % 6 == 5:
            self.current_week = (self.current_week + 1) % 2
            if self.current_week == 0:
                self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
            else:
                self.tableWidget.setHorizontalHeaderLabels(["Вторая неделя"])

    def update_day_label(self):
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        self.lineEdit.setText(days_of_week[self.current_day % 6])
        data_week_1 = {
            "8:00": self.timetable_arr[0 + self.current_day * 6],
            "9:40": self.timetable_arr[1 + self.current_day * 6],
            "11:30": self.timetable_arr[2 + self.current_day * 6],
            "13:20": self.timetable_arr[3 + self.current_day * 6],
            "15:00": self.timetable_arr[4 + self.current_day * 6],
            "16:40": self.timetable_arr[5 + self.current_day * 6]
        }

        for row, (time, data) in enumerate(data_week_1.items()):
            text_item = QtWidgets.QTableWidgetItem(data)
            text_item.setTextAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
            self.tableWidget.setItem(row, 0, text_item)

    def show_calendar(self):
        self.calendar = (self.calendar + 1) % 2
        if self.calendar == 1:
            self.calendarWidget.show()
        else:
            self.calendarWidget.hide()
