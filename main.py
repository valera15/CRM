# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_vhod.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(1100, 800)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_nazv = QtWidgets.QLabel(self.centralwidget)
        self.label_nazv.setGeometry(QtCore.QRect(350, 10, 450, 71))
        self.label_nazv.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_nazv.setFont(font)
        self.label_nazv.setObjectName("label_nazv")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(350, 200, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.label_parol = QtWidgets.QLabel(self.centralwidget)
        self.label_parol.setGeometry(QtCore.QRect(350, 280, 135, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_parol.setFont(font)
        self.label_parol.setObjectName("label_parol")
        self.pushButton_Voete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voete.setGeometry(QtCore.QRect(510, 700, 130, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Voete.setFont(font)
        self.pushButton_Voete.setObjectName("pushButton_Voete")
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(510, 200, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setText("")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_parol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_parol.setGeometry(QtCore.QRect(510, 290, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_parol.setFont(font)
        self.lineEdit_parol.setObjectName("lineEdit_parol")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Шаги к счастью"))
        self.label_nazv.setText(_translate("MainWindow1", "Войти в систему"))
        self.label_login.setText(_translate("MainWindow1", "Логин"))
        self.label_parol.setText(_translate("MainWindow1", "Пароль"))
        self.pushButton_Voete.setText(_translate("MainWindow1", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())