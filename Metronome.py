# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Metronome.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
list1=[]
a=[]
result=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 607)
        MainWindow.setStyleSheet("background:url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 741, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 36pt \"Poor Richard\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 127);\n"
"border-color: rgb(200, 14, 42);\n"
"border-color: rgb(212, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);\n"
"font: 72pt \"Poor Richard\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 400, 391, 81))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(199, 0, 0);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/3025528.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 761, 291))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/รูปfrom internet/3025528.jpg);")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 510, 20, 21))
        self.radioButton.setObjectName("radioButton")
        self.label_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.click)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.radioButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "      Metronome"))
        self.label.setText(_translate("MainWindow", "  "))
        self.pushButton.setText(_translate("MainWindow", "Click To Count !"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
    def click(self):
            result=0
            if len(list1)<2:
                   p=time.time()
                   list1.append(p)
                   BPM=0
        
            if len(list1)==2 :
                    p=time.time()
                    list1.append(p)
                    period=list1[1]-list1[0]
                    BPM= int(60//period)
                    a.append(BPM)
                    list1.clear()
            if len(a)>=2 :
                    for i in a:
                            result +=i
                    BPM=result//len(a)  
            print(list1)
            print(BPM)
            print(result)
            self.label.setText(str(BPM))
            
import Myimage_metronome_rc

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow=QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())