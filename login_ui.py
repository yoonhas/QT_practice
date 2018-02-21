# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#groupBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 40px;\n"
"    background: white;\n"
"}\n"
"#label_1, #label_2{\n"
"    font-size: 20px;\n"
"}\n"
"#password_input, #username_input {\n"
"    font-size: 12;\n"
"}\n"
"#password_input \n"
"{\n"
"  type: password;\n"
"  letter-spacing: 1px;\n"
" }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 330, 371, 211))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.username_input = QtWidgets.QTextEdit(self.groupBox)
        self.username_input.setGeometry(QtCore.QRect(140, 60, 191, 31))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.groupBox)
        self.password_input.setGeometry(QtCore.QRect(140, 110, 191, 31))
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submit = QtWidgets.QPushButton(self.groupBox)
        self.submit.setGeometry(QtCore.QRect(40, 150, 281, 51))
        self.submit.setObjectName("submit")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 230, 401, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(260, 50, 221, 211))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../../work/tipcenter/tiplogo.png"))
        self.Logo.setObjectName("Logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label_1.setText(_translate("MainWindow", "Username :"))
        self.label_2.setText(_translate("MainWindow", "Password : "))
        self.label.setText(_translate("MainWindow", "PSS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

