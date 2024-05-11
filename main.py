from PyQt5 import QtWidgets
from timetable import Timetable
from gui import Ui_MainWindow, MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
