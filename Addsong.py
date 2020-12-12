# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addsong.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 695)
        MainWindow.setStyleSheet("background-image: url(:/image/รูปfrom internet/ecb60dab3d73704e847e989b04f5521b.jpg);\n"
"background-image: url(:/image/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Source = QtWidgets.QGroupBox(self.centralwidget)
        self.Source.setGeometry(QtCore.QRect(70, 80, 831, 491))
        self.Source.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 14pt \"Wide Latin\";\n"
"fo\n"
"font: 81 24pt \"Rockwell Extra Bold\";")
        self.Source.setObjectName("Source")
        self.Output = QtWidgets.QPlainTextEdit(self.Source)
        self.Output.setGeometry(QtCore.QRect(10, 30, 811, 451))
        self.Output.setObjectName("Output")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(470, 30, 301, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Inputsong = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Inputsong.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Rockwell Condensed\";")
        self.Inputsong.setObjectName("Inputsong")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Inputsong)
        self.click = QtWidgets.QPushButton(self.centralwidget)
        self.click.setGeometry(QtCore.QRect(790, 30, 111, 41))
        self.click.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.click.setObjectName("click")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(760, 590, 141, 41))
        self.Clear.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Clear.setObjectName("Clear")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(70, 590, 141, 41))
        self.Back.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Back.setObjectName("Back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.click.clicked.connect(self.Add)
        self.Clear.clicked.connect(self.clear)

        self.retranslateUi(MainWindow)
        self.Back.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Addsong"))
        self.Source.setTitle(_translate("MainWindow", "Songs"))
        self.label.setText(_translate("MainWindow", "Add Name:"))
        self.click.setText(_translate("MainWindow", "Enter"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Back.setText(_translate("MainWindow", "Back"))
    def Add(self):
            lists=self.Inputsong.text()
            self.Output.appendPlainText(lists)
            self.Inputsong.setText("")
    def clear(self):
            self.Output.clear()
import Myimage_rc

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow=QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())