# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grammar11.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(255, 248, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.w1 = QtWidgets.QWidget(self.centralwidget)
        self.w1.setGeometry(QtCore.QRect(0, 0, 1019, 1101))
        font = QtGui.QFont()
        font.setKerning(False)
        self.w1.setFont(font)
        self.w1.setStyleSheet("border-image:url(:/hobby/cach-viet-doan-van-tieng-anh-ve-gioi-thieu-so-thich-1-1.jpeg);\n"
"border-top-right-radius: 70px;\n"
"border-bottom-right-radius: 70px;")
        self.w1.setObjectName("w1")
        self.w2 = QtWidgets.QWidget(self.centralwidget)
        self.w2.setGeometry(QtCore.QRect(929, 0, 1981, 1101))
        self.w2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(144, 221, 205, 255), stop:1 rgba(255, 255, 255, 255));")
        self.w2.setObjectName("w2")
        self.ex11 = QtWidgets.QPushButton(self.w2)
        self.ex11.setGeometry(QtCore.QRect(300, 660, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ex11.setFont(font)
        self.ex11.setStyleSheet("QPushButton {\n"
"    border: 5px solid black;\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-radius: 50px;\n"
"    padding: 10px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(0, 170, 0); \n"
"}")
        self.ex11.setFlat(True)
        self.ex11.setObjectName("ex11")
        self.gra11 = QtWidgets.QPushButton(self.w2)
        self.gra11.setEnabled(True)
        self.gra11.setGeometry(QtCore.QRect(300, 340, 321, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gra11.setFont(font)
        self.gra11.setStyleSheet("QPushButton {\n"
"    border: 5px solid black;\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-radius: 50px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(0, 170, 0); \n"
"}")
        self.gra11.setAutoDefault(False)
        self.gra11.setDefault(False)
        self.gra11.setFlat(True)
        self.gra11.setObjectName("gra11")
        self.label = QtWidgets.QLabel(self.w2)
        self.label.setGeometry(QtCore.QRect(740, 0, 201, 91))
        self.label.setStyleSheet("image: url(:/logo/62264bc2694c9812c15d.jpg);\n"
"border: 5px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.back_home11 = QtWidgets.QPushButton(self.w2)
        self.back_home11.setGeometry(QtCore.QRect(100, 920, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_home11.setFont(font)
        self.back_home11.setStyleSheet("QPushButton {\n"
"    border: 5px solid black;\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-radius: 25px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(0, 170, 0); \n"
"}")
        self.back_home11.setObjectName("back_home11")
        self.w2.raise_()
        self.w1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.ex11.setText(_translate("MainWindow", "EXERCISES"))
        self.gra11.setText(_translate("MainWindow", "GRAMMAR"))
        self.back_home11.setText(_translate("MainWindow", "Back"))
import anhnen_rc
import hobby_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
