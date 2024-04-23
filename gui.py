from PyQt5 import QtCore, QtWidgets
from main import Timetable


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
        self.fill_table_data(timetable)

    def fill_table_data(self, timetable):
        # Данные для таблиц
        timetable_arr = timetable.get_timetable()[0]
        data_week_1 = {
            "8:00": timetable_arr[0],
            "9:40": timetable_arr[1],
            "11:30": timetable_arr[2],
            "13:20": timetable_arr[3],
            "15:00": timetable_arr[4],
            "16:40": timetable_arr[5]
        }

        # Заполнение таблицы 1
        if timetable.get_timetable()[1] == 0:
            self.tableWidget.setHorizontalHeaderLabels(["Первая неделя"])
        else:
            self.tableWidget.setHorizontalHeaderLabels(["Вторая неделя"])

        self.tableWidget.setVerticalHeaderLabels(["8:00", "9:40", "11:30", "13:20", "15:00", "16:40"])

        # Установка таблицы только для чтения
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for row, (time, data) in enumerate(data_week_1.items()):
            text_item = QtWidgets.QTableWidgetItem(data)
            text_item.setTextAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
            self.tableWidget.setItem(row, 0, text_item)

    # Обработчик события изменения размера окна
    def resizeEvent(self, event):
        # Установка высоты строк пропорционально размеру окна
        table_height = self.tableWidget.height()
        row_count = self.tableWidget.rowCount()
        row_height = int(table_height / row_count - 5)
        for row in range(row_count):
            self.tableWidget.setRowHeight(row, row_height)


import sys

timetable = Timetable('test.xlsx', 'Лист1')
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
