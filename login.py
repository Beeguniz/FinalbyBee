from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Signin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("QPushButton#loginbt{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgb(255, 204, 229));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#loginbt:hover{\n"
"background-color:rgb(255,243,255);\n"
"color:black;\n"
"}\n"
"QPushButton#loginbt:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color: rgba(150,123,111,255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.background.setStyleSheet("image: url(:/images/img.jpg);\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 431, 601))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.loginweb = QtWidgets.QLabel(self.widget)
        self.loginweb.setGeometry(QtCore.QRect(290, 230, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.loginweb.setFont(font)
        self.loginweb.setStyleSheet("background-color:white;\n"
"color:rgb(255,204,229);")
        self.loginweb.setObjectName("loginweb")
        self.user_input = QtWidgets.QLineEdit(self.widget)
        self.user_input.setGeometry(QtCore.QRect(230, 400, 331, 31))
        self.user_input.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_input.setObjectName("user_input")
        self.pass_input = QtWidgets.QLineEdit(self.widget)
        self.pass_input.setGeometry(QtCore.QRect(230, 490, 331, 31))
        self.pass_input.setStyleSheet("background-color: white;\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.pass_input.setObjectName("pass_input")
        self.loginbt = QtWidgets.QPushButton(self.widget)
        self.loginbt.setGeometry(QtCore.QRect(280, 560, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.loginbt.setFont(font)
        self.loginbt.setObjectName("loginbt")
        self.asksignup = QtWidgets.QLabel(self.widget)
        self.asksignup.setGeometry(QtCore.QRect(250, 670, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.asksignup.setFont(font)
        self.asksignup.setObjectName("asksignup")
        self.signup_bt = QtWidgets.QPushButton(self.widget)
        self.signup_bt.setGeometry(QtCore.QRect(410, 670, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.signup_bt.setFont(font)
        self.signup_bt.setStyleSheet("background-color: white;\n"
"border:none;\n"
"color:#3399FF;\n"
"padding-bottom:7px;")
        self.signup_bt.setObjectName("signup_bt")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(1120, 1050, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(360, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        '''
        self.loginbt.clicked.connect(self.signin)
        '''
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginweb.setText(_translate("MainWindow", "Dokugaku"))
        self.user_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pass_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.loginbt.setText(_translate("MainWindow", "S i g n  I n"))
        self.asksignup.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.signup_bt.setText(_translate("MainWindow", "Sign up"))
        self.label_3.setText(_translate("MainWindow", "Sign up"))
        self.label.setText(_translate("MainWindow", "Sign in"))
'''  
    def signin(self):
        un = self.user_input.text()
        psw = self.pass_input.text()

        with open('user_data.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(',')
            if len(data) == 2 and data[0] == un and data[1] == psw:
                QMessageBox.information(None, "Dokugaku", "Đăng nhập thành công!")
                return

        QMessageBox.information(None, "Dokugaku", "Đăng nhập thất bại!")
'''
import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_Signin()  
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())