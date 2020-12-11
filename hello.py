from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,QtGui
import sys

def window():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setGeometry(0,0,1000,700)
    window.setWindowTitle("Metronome")
    window.setMinimumSize(346,223)
    window.setWindowIcon(QtGui.QIcon("C:\\Users\\ACER\\Desktop\\รูปfrom internet\\Main.jpg"))
    window.show()
    sys.exit(app.exec_())

window()