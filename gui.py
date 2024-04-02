from PyQt5 import QtCore, QtWidgets


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


        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        # Таблица 2
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)  # Растягиваем последний столбец
        self.tableWidget_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                         QtWidgets.QSizePolicy.Expanding)  # Политика изменения размеров

        self.gridLayout.addWidget(self.tableWidget_2, 2, 1, 1, 1)

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
        self.lineEdit.setReadOnly(True)  # Делаем строку ввода только для чтения
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "След. день"))
        self.pushButton_2.setText(_translate("MainWindow", "Пред. день"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать Группу"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать День"))
        self.lineEdit.setText(_translate("MainWindow", "День Недели"))

        # заполнение таблиц
        self.fill_table_data()

    def fill_table_data(self):
        # Данные для таблиц
        data_week_1 = {
            "8:00": "Данные 1\nДанные 2\nДанные 3",
            "9:40": "Данные 4\nДанные 5\nДанные 6",
            "11:30": "Данные 7\nДанные 8\nДанные 9",
            "13:20": "Данные 10\nДанные 11\nДанные 12",
            "15:00": "Данные 13\nДанные 14\nДанные 15",
            "16:40": "Данные 16\nДанные 17\nДанные 18"
        }

        data_week_2 = {
            "8:00": "Данные 19\nДанные 20\nДанные 21",
            "9:40": "Данные 22\nДанные 23\nДанные 24",
            "11:30": "Данные 25\nДанные 26\nДанные 27",
            "13:20": "Данные 28\nДанные 29\nДанные 30",
            "15:00": "Данные 31\nДанные 32\nДанные 33",
            "16:40": "Данные 34\nДанные 35\nДанные 36"
        }

        # Заполнение таблицы 1
        self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
        self.tableWidget.setVerticalHeaderLabels(["8:00", "9:40", "11:30", "13:20", "15:00", "16:40"])
        for row, (time, data) in enumerate(data_week_1.items()):
            text_edit = QtWidgets.QTextEdit()
            text_edit.setPlainText(data)
            self.tableWidget.setCellWidget(row, 0, text_edit)

        # Заполнение таблицы 2
        self.tableWidget_2.setHorizontalHeaderLabels(["Вторая неделя"])
        self.tableWidget_2.setVerticalHeaderLabels(["8:00", "9:40", "11:30", "13:20", "15:00", "16:40"])
        for row, (time, data) in enumerate(data_week_2.items()):
            text_edit = QtWidgets.QTextEdit()
            text_edit.setPlainText(data)
            self.tableWidget_2.setCellWidget(row, 0, text_edit)

    # Обработчик события изменения размера окна
    def resizeEvent(self, event):
        # Установка высоты строк пропорционально размеру окна
        table_height = self.tableWidget.height()
        row_count = self.tableWidget.rowCount()
        row_height = int(table_height / row_count * 0.96)
        for row in range(row_count):
            self.tableWidget.setRowHeight(row, row_height)

        table_height = self.tableWidget_2.height()
        row_count = self.tableWidget_2.rowCount()
        row_height = int(table_height / row_count * 0.96)
        for row in range(row_count):
            self.tableWidget_2.setRowHeight(row, row_height)


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
