import os
import sys
import threading
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit



from PyQt5 import QtCore, QtGui, QtWidgets

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)
    def flush(self):
        self.textWritten.emit('')
    def write(self, text):
        self.textWritten.emit(str(text))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(330, 90, 75, 23))
        self.download_btn.setObjectName("download")
        self.download_btn.clicked.connect(self.dnld)

        self.url_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.url_txt.setGeometry(QtCore.QRect(130, 20, 481, 20))
        self.url_txt.setObjectName("url")

        self.out_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.out_txt.setGeometry(QtCore.QRect(130, 180, 481, 251))
        self.out_txt.setObjectName("out")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(456, 160, 151, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        sys.stdout = EmittingStream(textWritten=self.output_terminal_written)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.download_btn.setText(_translate("MainWindow", "حمل"))
        self.label.setText(_translate("MainWindow", "الرابط"))
        self.label_2.setText(_translate("MainWindow", "النسبة و بقية الحبشكلات"))

    def output_terminal_written(self, text):
        self.out_txt.append(text)

    def onUpdateText(self, text):
        cursor = self.process.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def dnld(self):
        from youtubeDownloader import Downloader
        # threading.Thread.start(main.download(self.url_txt.text()))
        downloader = Downloader(self.url_txt.text())
        threading.Thread(target=downloader.download).start()

    def __del__(self):
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
