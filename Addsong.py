# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addsong.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

j={}
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 695)
        MainWindow.setStyleSheet("background-image: url(:/image/รูปfrom internet/ecb60dab3d73704e847e989b04f5521b.jpg);\n"
"background-image: url(:/image/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(460, 260, 111, 41))
        self.Clear.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Clear.setObjectName("Clear")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 590, 141, 41))
        self.Back.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Back.setObjectName("Back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 320, 851, 251))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 382, 70))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 20pt \"Poor Richard\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Addcreate = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Addcreate.setStyleSheet("font: 16pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.Addcreate.setText("")
        self.Addcreate.setObjectName("Addcreate")
        self.horizontalLayout.addWidget(self.Addcreate)
        self.Enter1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Enter1.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 10pt \"Rockwell\";")
        self.Enter1.setObjectName("Enter1")
        self.horizontalLayout.addWidget(self.Enter1)
        self.Enterlistsong = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Enterlistsong.setGeometry(QtCore.QRect(460, 90, 421, 161))
        self.Enterlistsong.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.Enterlistsong.setObjectName("Enterlistsong")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 91, 78))
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 20pt \"Poor Richard\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 0, 211, 81))
        self.label_5.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 36pt \"Poor Richard\";")
        self.label_5.setObjectName("label_5")
        self.Enter2 = QtWidgets.QPushButton(self.centralwidget)
        self.Enter2.setGeometry(QtCore.QRect(330, 240, 93, 29))
        self.Enter2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 10pt \"Rockwell\";")
        self.Enter2.setObjectName("Enter2")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(330, 270, 93, 29))
        self.Delete.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 10pt \"Rockwell\";")
        self.Delete.setObjectName("Delete")
        self.playlistshow = QtWidgets.QLineEdit(self.centralwidget)
        self.playlistshow.setGeometry(QtCore.QRect(130, 240, 191, 51))
        self.playlistshow.setStyleSheet("font: 16pt \"Rockwell\";\n"
"color:rgb(255, 255, 255)")
        self.playlistshow.setObjectName("playlistshow")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 130, 421, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Number = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.Number.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";\n"
"background-image: url(:/image/รูปfrom internet/dark-blue-plain-wall-background_53876-92976.jpg);\n"
"background-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 0);")
        self.Number.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Number.setObjectName("Number")
        self.gridLayout.addWidget(self.Number, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 10pt \"Rockwell\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.Show = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Show.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Rockwell\";")
        self.Show.setText("")
        self.Show.setObjectName("Show")
        self.gridLayout.addWidget(self.Show, 0, 0, 1, 2)
        self.Clear_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_2.setGeometry(QtCore.QRect(770, 260, 111, 41))
        self.Clear_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Clear_2.setObjectName("Clear_2")
        self.Back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Back_2.setGeometry(QtCore.QRect(750, 590, 141, 41))
        self.Back_2.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 16pt \"Rockwell\";")
        self.Back_2.setObjectName("Back_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.Enter1.clicked.connect(self.add)
        self.Enter2.clicked.connect(self.LaLa)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Back.clicked.connect(MainWindow.close)
        self.Back_2.clicked.connect(self.label.clear)
        self.pushButton.clicked.connect(self.Spinbox)
        self.Clear.clicked.connect(self.allclear)
        self.Clear_2.clicked.connect(self.Enter)
        self.Delete.clicked.connect(self.delete)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Addcreate, self.Enter1)
        MainWindow.setTabOrder(self.Enter1, self.Enterlistsong)
        MainWindow.setTabOrder(self.Enterlistsong, self.Clear)
        MainWindow.setTabOrder(self.Clear, self.playlistshow)
        MainWindow.setTabOrder(self.playlistshow, self.Enter2)
        MainWindow.setTabOrder(self.Enter2, self.Delete)
        MainWindow.setTabOrder(self.Delete, self.Back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Addsong"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Back.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><a href=\"https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula\"><span style=\" text-decoration: underline; color:#0000ff;\">sda</span></a></p></body></html>"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Enter the playlist name to add or create.</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Add/Create:"))
        self.Enter1.setText(_translate("MainWindow", "Enter"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Enter the playlist name that you want to see.</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Name :"))
        self.label_5.setText(_translate("MainWindow", "  Playlist"))
        self.Enter2.setText(_translate("MainWindow", "Enter"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.Clear_2.setText(_translate("MainWindow", "Enter"))
        self.Back_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><a href=\"https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula\"><span style=\" text-decoration: underline; color:#0000ff;\">sda</span></a></p></body></html>"))
        self.Back_2.setText(_translate("MainWindow", "Clear"))
    def add(self):
        b=self.Addcreate.text()
        if b in j:
                self.Show.setText("The number of new song you would like to update : ")
                
        else:
                self.Show.setText("The number of song you would like to add in playlist : ")
        print(j)
        print(b)
    def Spinbox(self):
            c=self.Number.value()
            self.Enterlistsong.setPlainText("Song Name : \n"*c)
    def allclear(self):
            self.Addcreate.clear()
            self.Show.clear()
            self.Number.clear()
            self.Enterlistsong.clear()
    def Enter(self):
            e = []
            data=self.Enterlistsong.toPlainText()
            if data=="":
                    self.Enterlistsong.setPlainText("Sorry, please done in process...")
            else:        
                data.replace("Song Name :","")
                data=data.split("\n")
                '''
                if data in j[self.Addcreate]:
                        pass
                else:
                        j[Addcreate].append(data)
                        return j
                '''
                for word in data :
                        v=word.split(":")
                        sad=v.pop(-1)
                        e.append(sad.strip())
                e.pop(-1)
                j[self.Addcreate.text()]=e

                self.Addcreate.clear()
                self.Show.clear()
                self.Number.clear()
                self.Enterlistsong.clear()
                self.Enterlistsong.setPlainText("Adding sucessful!!!")
                print(data)
                print(j)
                print(e)

                return j
    def LaLa(self):
             pry=self.playlistshow.text()
             if pry in j :
                     j[pry]=str(j[pry])
                     self.label.setText(j[pry])
             else:
                     self.label.setText("Please create the playlist!!!")
    def delete(self):
             if self.playlistshow.text()=="":
                     self.label.setText("Clame down dude,input song first!")
             else: 
                pry=self.playlistshow.text()
                del j[pry]
                self.playlistshow.setText("")
                self.label.setText("")

             
import Myimage_rc

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow=QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())