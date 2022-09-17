import cv2 
import numpy as np
import os
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

face_cascade = cv2.CascadeClassifier("C:\\Users\\LENOVO\\source\\repos\\PY\\frontalface.xml")
base_path = "C:\\Users\\LENOVO\\source\\repos\\saved_faces_coms\\"

class DatasetName(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dataset Name")
        self.setMaximumSize(QtCore.QSize(449, 150))
        self.setMinimumSize(QtCore.QSize(449, 150))
        self.setWindowIcon(QtGui.QIcon("../../../OneDrive/Masaüstü/CMS/foldericon.png"))

        # enter your name to create dataset folder
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("Enter Your Name:")
        font_3 = QtGui.QFont()
        font_3.setBold(True)
        font_3.setUnderline(True)
        self.label_3.setFont(font_3)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 221, 31))
        self.label_3.setFont(QtGui.QFont("Palatino Linotype", 16))

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 90, 321, 31))
        self.lineEdit.setFont(QtGui.QFont("Palatino Linotype", 10))
        self.lineEdit.returnPressed.connect(self.exit_n_save_folder_name)
        self.lineEdit.returnPressed.connect(self.path_exists)

    def exit_n_save_folder_name(self):
        self.folder_name = self.lineEdit.text()
        global base_path
        self.new_dir = os.path.join(base_path, self.folder_name)
        os.mkdir(self.new_dir)
        self.close()
    
    def get_new_path(self):
        return self.new_dir

    def f_name(self):
        return self.folder_name
    
    # check if folder was saved correctly
    def path_exists(self):
        if os.path.exists(self.new_dir):
            messagewin.show()
        else:
            errorwin.show()
            
class MessageWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message")
        self.setWindowIcon(QtGui.QIcon("../../../OneDrive/Masaüstü/CMS/messageicon.png"))
        self.setMaximumSize(QtCore.QSize(500, 150))
        self.setMinimumSize(QtCore.QSize(500, 150))
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Your dataset directory has been created!")
        self.label.setGeometry(QtCore.QRect(20, 40, 456, 41))
        self.label.setFont(QtGui.QFont("Palatino Linotype", 16))

        self.ok_button = QtWidgets.QPushButton(self)
        self.ok_button.setText("Ok")
        self.ok_button.setGeometry(QtCore.QRect(200, 90, 93, 28))
        self.ok_button.setFont(QtGui.QFont("Palatino Linotype", 11))
        self.ok_button.setStyleSheet("background-color: rgb(220, 220, 220); color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok_button.setFont(font)
        self.ok_button.clicked.connect(self.ok_button_clicked)
        self.ok_button.clicked.connect(self.facelock_window)

    def ok_button_clicked(self):
        messagewin.close()

    # this function will save your face label to entered folder
    def facelock_window(self):  
        cap = cv2.VideoCapture(0)
        
        skip = 0
        faces_data = []
        
        while True:
            ret, frame = cap.read()
            
            if ret == False:
                continue
            
            frame = cv2.flip(frame, 1)
            # convert space color to gray for detecting better
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)

            if len(faces) == 0:
                continue

            text = "Please move your face."
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, text, (0, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
                roi = frame[y:y+h, x:x+w]
                skip += 1
                
                # it saves your face fastly. So skipping frames will be better to save different pictures
                if skip % 3 == 0:
                    i=0
                    maxFrames = 45
                    while maxFrames >= i:
                        faces_data.append(roi)
                        name = "{}".format(str(i))
                        for face in faces_data:
                            # convert pictures to numpy array
                            face = np.asarray(face, dtype=object)
                            face = face.reshape((face.shape[0], -1))
                            np.save(os.path.join(base_path+datasetname.f_name(),name) ,face)

                        for face_ in faces_data:
                            if w>=150 and h>=150:
                                # to save your label
                                cv2.imwrite(os.path.join(base_path+datasetname.f_name(),name+".jpg"), face_)
                                #print(len(faces_data))
                                i+=1
                            else:
                                pass     

            if skip == 135:
                break        
            
            cv2.imshow("Frame", frame)
            cv2.imshow("Roi", roi)
            if cv2.waitKey(1) == 27:
                break
    
        #print("Your data succesfully saved!")

        cap.release()
        cv2.destroyAllWindows()
 
class ErrorWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!")
        self.setWindowIcon(QtGui.QIcon("../../../OneDrive/Masaüstü/CMS/erroricon.png"))
        self.setMaximumSize(QtCore.QSize(449, 150))
        self.setMinimumSize(QtCore.QSize(449, 150))

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 421, 41))
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setFont(QtGui.QFont("Palatino Linotype", 16))
        self.label_2.setText("ERROR: Directory has not been created!")

        self.cancel_button = QtWidgets.QPushButton(self)
        self.cancel_button.setText("Cancel")
        self.cancel_button.setGeometry(QtCore.QRect(180, 90, 93, 28))
        self.cancel_button.setFont(QtGui.QFont("Palatino Linotype", 11))
        self.cancel_button.setStyleSheet("background-color: rgb(220, 220, 220); color: rgb(0, 0, 0);")
        font_2 = QtGui.QFont()
        font_2.setBold(True)
        font_2.setWeight(75)
        self.cancel_button.setFont(font_2)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

    def cancel_button_clicked(self):
        sys.exit()

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
app2 = QtWidgets.QApplication([])
app3 = QtWidgets.QApplication([])
messagewin = MessageWindow()
errorwin = ErrorWindow()
datasetname = DatasetName()
nameofuser = nameOfUser()
datasetname.show()
sys.exit(app.exec_()) 

# sonra knn ile train edilecek***
# ekran kendiliğinden kapanacak
# kayıt işleminden sonra login ekranına geçecek
# yuz tanıma butonu tıklandıktan sonra directory skanlanacek
# eger train edilen yüz varsa giriş yapılacak

# Error ve message pencerelerini wizard içine al

#------------------------------------
# bi face saver , face train ve facelock kodu olacak
# face saver tamamlandı
# *******
# face train kodunda resimler knn ile train edilecek ve model .clf dosyası olarak kişisin adını taşıyan klasöre kaydedilecek
# train edilirken ekrana lütfen bekleyiniz tarzı bir mesaj çıksın
# *******
# facelock kodunda ilk önce ismini soracak ona göre kaydettiğin dataset'e erişecek 
# sonra seni tanımaya çalışacak
