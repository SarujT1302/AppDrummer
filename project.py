# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time

list1=[]
a=[]
result=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 680)
        MainWindow.setMaximumSize(QtCore.QSize(930, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/รูปfrom internet/15e1448aff067989819887028ebbd2af.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 931, 631))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background:\n"
"url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg)")
        self.stackedWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Enter = QtWidgets.QPushButton(self.page)
        self.Enter.setGeometry(QtCore.QRect(800, 40, 111, 41))
        self.Enter.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Enter.setObjectName("Enter")
        self.Inputsong = QtWidgets.QLineEdit(self.page)
        self.Inputsong.setGeometry(QtCore.QRect(600, 40, 159, 37))
        self.Inputsong.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Rockwell Condensed\";")
        self.Inputsong.setText("")
        self.Inputsong.setObjectName("Inputsong")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(460, 40, 133, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.Inputsong_2 = QtWidgets.QLineEdit(self.page)
        self.Inputsong_2.setGeometry(QtCore.QRect(141, -39, 159, 37))
        self.Inputsong_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Rockwell Condensed\";")
        self.Inputsong_2.setObjectName("Inputsong_2")
        self.Clear = QtWidgets.QPushButton(self.page)
        self.Clear.setGeometry(QtCore.QRect(770, 540, 141, 41))
        self.Clear.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Clear.setObjectName("Clear")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(1, -39, 133, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.Back = QtWidgets.QPushButton(self.page)
        self.Back.setGeometry(QtCore.QRect(70, 540, 141, 41))
        self.Back.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Back.setObjectName("Back")
        self.Source = QtWidgets.QGroupBox(self.page)
        self.Source.setGeometry(QtCore.QRect(70, 90, 801, 441))
        self.Source.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 14pt \"Wide Latin\";\n"
"fo\n"
"font: 81 24pt \"Rockwell Extra Bold\";")
        self.Source.setObjectName("Source")
        self.Output = QtWidgets.QPlainTextEdit(self.Source)
        self.Output.setGeometry(QtCore.QRect(10, 30, 781, 401))
        self.Output.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Output.setObjectName("Output")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Clear_2 = QtWidgets.QPushButton(self.page_3)
        self.Clear_2.setGeometry(QtCore.QRect(740, 500, 141, 41))
        self.Clear_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Clear_2.setObjectName("Clear_2")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 411, 311))
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 36pt \"Poor Richard\";")
        self.label_4.setObjectName("label_4")
        self.CountBotton = QtWidgets.QPushButton(self.page_3)
        self.CountBotton.setGeometry(QtCore.QRect(270, 410, 391, 81))
        self.CountBotton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(199, 0, 0);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/3025528.jpg);")
        self.CountBotton.setObjectName("CountBotton")
        self.Nome = QtWidgets.QLabel(self.page_3)
        self.Nome.setGeometry(QtCore.QRect(480, 70, 401, 311))
        self.Nome.setStyleSheet("color: rgb(255, 255, 127);\n"
"border-color: rgb(200, 14, 42);\n"
"border-color: rgb(212, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);\n"
"font: 72pt \"Poor Richard\";")
        self.Nome.setText("")
        self.Nome.setObjectName("Nome")
        self.Back_2 = QtWidgets.QPushButton(self.page_3)
        self.Back_2.setGeometry(QtCore.QRect(70, 500, 141, 41))
        self.Back_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Back_2.setObjectName("Back_2")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(50, 60, 841, 331))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/รูปfrom internet/3025528.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.page_3)
        self.radioButton.setGeometry(QtCore.QRect(470, 510, 20, 21))
        self.radioButton.setObjectName("radioButton")
        self.label_6.raise_()
        self.Clear_2.raise_()
        self.label_4.raise_()
        self.CountBotton.raise_()
        self.Nome.raise_()
        self.Back_2.raise_()
        self.radioButton.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 263, 177))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.Subdivision = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Subdivision.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Poor Richard\";\n"
"color: rgb(255, 255, 127);")
        self.Subdivision.setObjectName("Subdivision")
        self.verticalLayout_4.addWidget(self.Subdivision)
        self.Timesignature = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Timesignature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Poor Richard\";\n"
"color: rgb(255, 255, 127);")
        self.Timesignature.setObjectName("Timesignature")
        self.verticalLayout_4.addWidget(self.Timesignature)
        self.Tempo = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Tempo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Poor Richard\";\n"
"color: rgb(255, 255, 127);")
        self.Tempo.setObjectName("Tempo")
        self.verticalLayout_4.addWidget(self.Tempo)
        self.Chord = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Chord.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Poor Richard\";\n"
"color: rgb(255, 255, 127);")
        self.Chord.setObjectName("Chord")
        self.verticalLayout_4.addWidget(self.Chord)
        self.Back_5 = QtWidgets.QPushButton(self.page_4)
        self.Back_5.setGeometry(QtCore.QRect(70, 480, 201, 71))
        self.Back_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Poor Richard\";\n"
"color: rgb(255, 255, 127);")
        self.Back_5.setObjectName("Back_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 30, 471, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setStyleSheet("background-image: url(:/Help/รูปfrom internet/Chord.jpg);\n"
"background-image: url(:/Help/รูปfrom internet/divisions and subdivisions.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setStyleSheet("background-image: url(:/Help/รูปfrom internet/Major-Key-Chord-Progressions.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setStyleSheet("background:\n"
"url(:/Help/รูปfrom internet/Tempo-Markings-BPM-Summary-Chart.jpg)")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setStyleSheet("background-image: url(:/Help/รูปfrom internet/TimeSig.jpg);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(0, -20, 921, 601))
        self.label.setMaximumSize(QtCore.QSize(1011, 16777215))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Desktop/รูปfrom internet/Template Metronome.jpg"))
        self.label.setObjectName("label")
        self.SongList = QtWidgets.QPushButton(self.page_2)
        self.SongList.setGeometry(QtCore.QRect(50, 130, 311, 71))
        self.SongList.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.SongList.setObjectName("SongList")
        self.Metronome = QtWidgets.QPushButton(self.page_2)
        self.Metronome.setGeometry(QtCore.QRect(530, 130, 311, 71))
        self.Metronome.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.Metronome.setObjectName("Metronome")
        self.MusicTool = QtWidgets.QLabel(self.page_2)
        self.MusicTool.setGeometry(QtCore.QRect(280, 260, 311, 61))
        self.MusicTool.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 36pt \"Poor Richard\";")
        self.MusicTool.setObjectName("MusicTool")
        self.Theory = QtWidgets.QPushButton(self.page_2)
        self.Theory.setGeometry(QtCore.QRect(280, 390, 311, 71))
        self.Theory.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.Theory.setObjectName("Theory")
        self.Exit = QtWidgets.QPushButton(self.page_2)
        self.Exit.setGeometry(QtCore.QRect(810, 560, 91, 41))
        self.Exit.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";\n"
"background-image: url(:/newPrefix/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.Exit.setObjectName("Exit")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 751, 471))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/รูปfrom internet/Retrospect.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_5.raise_()
        self.SongList.raise_()
        self.Metronome.raise_()
        self.MusicTool.raise_()
        self.Theory.raise_()
        self.Exit.raise_()
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.Clear.clicked.connect(self.Output.clear)
        self.Subdivision.clicked.connect(self.label_8.show)
        self.Timesignature.clicked.connect(self.label_13.show)
        self.Tempo.clicked.connect(self.label_11.show)
        self.Chord.clicked.connect(self.label_9.show)
        self.Subdivision.clicked.connect(self.label_9.hide)
        self.Subdivision.clicked.connect(self.label_11.hide)
        self.Subdivision.clicked.connect(self.label_13.hide)
        self.Timesignature.clicked.connect(self.label_8.hide)
        self.Timesignature.clicked.connect(self.label_9.hide)
        self.Timesignature.clicked.connect(self.label_11.hide)
        self.Tempo.clicked.connect(self.label_8.hide)
        self.Tempo.clicked.connect(self.label_9.hide)
        self.Tempo.clicked.connect(self.label_13.hide)
        self.Chord.clicked.connect(self.label_8.hide)
        self.Chord.clicked.connect(self.label_11.hide)
        self.Chord.clicked.connect(self.label_13.hide)
        self.SongList.clicked.connect(self.gopage2)
        self.Metronome.clicked.connect(self.gopage3)
        self.Theory.clicked.connect(self.gopage4)
        self.Back.clicked.connect(self.gopage1)
        self.Back_2.clicked.connect(self.gopage1)
        self.Back_5.clicked.connect(self.gopage1)
        self.Enter.clicked.connect(self.Add)
        self.CountBotton.clicked.connect(self.click)
        self.Clear_2.clicked.connect(self.clear)
        self.CountBotton.clicked.connect(self.radioButton.animateClick)
        self.Exit.clicked.connect(self.show_popup)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.label_2.setText(_translate("MainWindow", "Add Name:"))
        self.Inputsong_2.setText(_translate("MainWindow", "fsdfasdffdsaf"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Add Name:"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.Source.setTitle(_translate("MainWindow", "Songs"))
        self.Clear_2.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "        Metronome"))
        self.CountBotton.setText(_translate("MainWindow", "Click To Count !"))
        self.Nome.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Back_2.setText(_translate("MainWindow", "Back"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Theory</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "           Theory"))
        self.Subdivision.setText(_translate("MainWindow", "Sub Division"))
        self.Timesignature.setText(_translate("MainWindow", "Time-Signature"))
        self.Tempo.setText(_translate("MainWindow", "Tempo"))
        self.Chord.setText(_translate("MainWindow", "Chord progression"))
        self.Back_5.setText(_translate("MainWindow", "Back"))
        self.SongList.setText(_translate("MainWindow", "SongList"))
        self.Metronome.setText(_translate("MainWindow", "Metronome"))
        self.MusicTool.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Music-Tool</p></body></html>"))
        self.MusicTool.setText(_translate("MainWindow", "   Music-Tool"))
        self.Theory.setText(_translate("MainWindow", "Theory"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
    def gopage2(self):
            self.stackedWidget.setCurrentIndex(0)
    def gopage3(self):
            self.stackedWidget.setCurrentIndex(1)
    def gopage4(self):
            self.stackedWidget.setCurrentIndex(2)
    def gopage1(self):
            self.stackedWidget.setCurrentIndex(3)
    def Add(self):
            lists=self.Inputsong.text()
            self.Output.appendPlainText(lists)
            self.Inputsong.setText("")
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
            print(a)
            print(result)
            self.Nome.setText(str(BPM))
    def clear(self):
            a.clear()
            result=0
            BPM=""
            self.Nome.setText(str(BPM))
    def show_popup(self):
            msg = QMessageBox()
            msg.setWindowTitle("Exit")
            msg.setText("Are you sure ?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.buttonClicked.connect(self.popup_button)
            
            x = msg.exec_()
    def popup_button(self,i):
            q=i.text()
            print(q)
            if q == "OK":
                    MainWindow.close()
            
            


import Myimage_project_rc

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow=QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())