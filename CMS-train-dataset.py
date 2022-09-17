import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
import face_recognition 
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

base_path = "C:\\Users\\LENOVO\\source\\repos\\saved_faces_coms\\"

class nameOfUser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("User ID")
        self.setWindowIcon(QtGui.QIcon("../../../OneDrive/Masaüstü/CMS/messageicon.png"))
        self.setMaximumSize(QtCore.QSize(449, 173))
        self.setMinimumSize(QtCore.QSize(449, 173))

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter Your Name:")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setGeometry(QtCore.QRect(30, 20, 221, 31))
        self.label.setFont(QtGui.QFont("Palatino Linotype", 16))

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 321, 31))
        self.lineEdit.setFont(QtGui.QFont("Palatino Linotype", 10))

        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setText("Done")
        self.done_button.setGeometry(QtCore.QRect(170, 130, 93, 28))
        self.done_button.setFont(QtGui.QFont("Palatino Linotype", 11))
        self.done_button.setStyleSheet("background-color: rgb(220, 220, 220); color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.done_button.setFont(font)
        self.done_button.clicked.connect(self.done_clicked)
    
        self.label_2 = QtWidgets.QLabel(self)
        #self.label_2.setGeometry(QtCore.QRect(132,97,201,25))
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setFont(QtGui.QFont("Palatino Linotype", 11))

    def done_clicked(self):
        self.basename = self.lineEdit.text()
        if len(self.basename) > 0:
            try: 
                os.chdir(base_path + self.basename)
                nameofuser.close()
            except FileNotFoundError:
                self.lineEdit.setText("")
                self.label_2.setGeometry(QtCore.QRect(153,97,201,25))
                self.label_2.setText("File Not Found!")
        else:
            self.label_2.setGeometry(QtCore.QRect(132,97,201,25))
            self.label_2.setText("Please Enter a Name")
        
            
app = QtWidgets.QApplication([])
nameofuser = nameOfUser()
nameofuser.show()
sys.exit(app.exec_())
