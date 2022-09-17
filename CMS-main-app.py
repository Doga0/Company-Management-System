from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(741, 721)
        Wizard.setMinimumSize(QtCore.QSize(741, 721))
        Wizard.setMaximumSize(QtCore.QSize(741, 721))
        Wizard.setStyleSheet("")
        Wizard.setSizeGripEnabled(False)
        Wizard.setModal(False)
        Wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        Wizard.setOptions(QtWidgets.QWizard.DisabledBackButtonOnLastPage|QtWidgets.QWizard.NoBackButtonOnStartPage|QtWidgets.QWizard.NoCancelButton)
        Wizard.setSubTitleFormat(QtCore.Qt.AutoText)
        
        # To block the next button
        QtWidgets.QWizard.button(Wizard, QtWidgets.QWizard.NextButton).blockSignals(True)
        
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")

        # Background label
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 681))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/cms3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Title label
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.171, x2:1, y2:0.818, stop:0.147368 rgba(84, 84, 84, 133), stop:0.789474 rgba(241, 241, 241, 84));\n"
"color: rgb(0, 48, 86);")
        self.label_2.setObjectName("label_2")

        # Icon label
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        self.label_3.setGeometry(QtCore.QRect(240, 130, 241, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/comsicon3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        # Switch screesn to login screen
        self.pushButton = QtWidgets.QPushButton(self.wizardPage1)
        self.pushButton.setGeometry(QtCore.QRect(240, 400, 105, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 70, 125);\n"
"color: rgb(204, 204, 204);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login_clicked)

        # Switch screesn to register screen
        self.pushButton_2 = QtWidgets.QPushButton(self.wizardPage1)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 400, 105, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 70, 125);\n"
"color: rgb(204, 204, 204);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.register_page)
        Wizard.addPage(self.wizardPage1)

        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")

        # Background label
        self.label_4 = QtWidgets.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 741, 671))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/cms3.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # Login icon label
        self.label_5 = QtWidgets.QLabel(self.wizardPage2)
        self.label_5.setGeometry(QtCore.QRect(240, 100, 241, 231))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/login5.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        # "Email:" label
        self.label_6 = QtWidgets.QLabel(self.wizardPage2)
        self.label_6.setGeometry(QtCore.QRect(240, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(96, 226, 244);")
        self.label_6.setObjectName("label_6")

        # "Email: lineedit"
        self.lineEdit = QtWidgets.QLineEdit(self.wizardPage2)
        self.lineEdit.setGeometry(QtCore.QRect(280, 410, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        # "Password:" label
        self.label_7 = QtWidgets.QLabel(self.wizardPage2)
        self.label_7.setGeometry(QtCore.QRect(240, 460, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(41, 197, 236);")
        self.label_7.setObjectName("label_7")

        # "Password:" lineedit
        self.lineEdit_2 = QtWidgets.QLineEdit(self.wizardPage2)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 490, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Switch screen to facelock screen
        self.pushButton_3 = QtWidgets.QPushButton(self.wizardPage2)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 177, 158);")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.face_id)
        Wizard.addPage(self.wizardPage2)

        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")

        # Background label
        self.label_8 = QtWidgets.QLabel(self.wizardPage)
        self.label_8.setGeometry(QtCore.QRect(-10, 0, 761, 681))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/cms3.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        # Tablewidget for database
        self.tableWidget = QtWidgets.QTableWidget(self.wizardPage)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 601))
        self.tableWidget.setStyleSheet("background-color: rgb(120, 139, 154);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        # Add button to add items to tablewidget
        self.pushButton_4 = QtWidgets.QPushButton(self.wizardPage)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 50, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 70, 125);\n"
"color: rgb(204, 204, 204);")
        self.pushButton_4.setObjectName("pushButton_4")

        # Delete button to delete tablewidget items
        self.pushButton_5 = QtWidgets.QPushButton(self.wizardPage)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 90, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 70, 125);\n"
"color: rgb(204, 204, 204);")
        self.pushButton_5.setObjectName("pushButton_5")

        # Delete All button to delete all tablewidget items
        self.pushButton_6 = QtWidgets.QPushButton(self.wizardPage)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 562, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(60, 74, 131);\n"
"color: rgb(204, 204, 204);")
        self.pushButton_6.setObjectName("pushButton_6")

        Wizard.addPage(self.wizardPage)
        self.wizardPage.setFinalPage(True)

        self.wizardPage3 = QtWidgets.QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        
        # Background label
        self.label_11 = QtWidgets.QLabel(self.wizardPage3)
        self.label_11.setGeometry(QtCore.QRect(0, -5, 741, 731))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/registerbg.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")

        # Register icon label
        self.label_12 = QtWidgets.QLabel(self.wizardPage3)
        self.label_12.setGeometry(QtCore.QRect(30, 130, 241, 231))
        self.label_12.setStyleSheet("")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../../../OneDrive/Masaüstü/CMS/reg3.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.wizardPage3)
        self.label_13.setGeometry(QtCore.QRect(290, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_13.setObjectName("label_13")

        # Lineedit to enter name and surname
        self.lineEdit_7 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_7.setGeometry(QtCore.QRect(290, 180, 161, 31))
        self.lineEdit_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.label_14 = QtWidgets.QLabel(self.wizardPage3)
        self.label_14.setGeometry(QtCore.QRect(490, 140, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_14.setObjectName("label_14")

        # Lineedit to enter email
        self.lineEdit_8 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_8.setGeometry(QtCore.QRect(490, 180, 161, 31))
        self.lineEdit_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.label_15 = QtWidgets.QLabel(self.wizardPage3)
        self.label_15.setGeometry(QtCore.QRect(290, 250, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_15.setObjectName("label_15")

        # Lineedit to enter job
        self.lineEdit_9 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 290, 161, 31))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.label_16 = QtWidgets.QLabel(self.wizardPage3)
        self.label_16.setGeometry(QtCore.QRect(490, 250, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_16.setObjectName("label_16")

        # Lineedit to enter phone number
        self.lineEdit_10 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_10.setGeometry(QtCore.QRect(490, 290, 161, 31))
        self.lineEdit_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        # For entering only numbers
        self.enter_int = QtGui.QIntValidator()
        self.lineEdit_10.setValidator(self.enter_int) 

        self.label_17 = QtWidgets.QLabel(self.wizardPage3)
        self.label_17.setGeometry(QtCore.QRect(290, 360, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_17.setObjectName("label_17")
        
        # Lineedit to enter salary
        self.lineEdit_11 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_11.setGeometry(QtCore.QRect(290, 400, 161, 31))
        self.lineEdit_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_11.setCursorPosition(0)
        self.lineEdit_11.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_11.setClearButtonEnabled(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        # For entering only numbers
        self.lineEdit_11.setValidator(self.enter_int)

        self.label_18 = QtWidgets.QLabel(self.wizardPage3)
        self.label_18.setGeometry(QtCore.QRect(490, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_18.setObjectName("label_18")

        # Lineedit to enter password
        self.lineEdit_12 = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_12.setGeometry(QtCore.QRect(490, 400, 161, 31))
        self.lineEdit_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setFrame(True)
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_12.setDragEnabled(False)
        self.lineEdit_12.setReadOnly(False)
        self.lineEdit_12.setClearButtonEnabled(True)
        self.lineEdit_12.setObjectName("lineEdit_12")

        # Switch register screen to entrance
        self.pushButton_7 = QtWidgets.QPushButton(self.wizardPage3)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 500, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(115, 115, 115);\n"
"color: rgb(0, 82, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.done_clicked)

        # To save your face id
        self.pushButton_8 = QtWidgets.QPushButton(self.wizardPage3)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 500, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setUnderline(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(196, 217, 244);")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.face_id)

        self.label_19 = QtWidgets.QLabel(self.wizardPage3)
        self.label_19.setGeometry(QtCore.QRect(90, 360, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 111, 172);")
        self.label_19.setObjectName("label_19")

        # Choose your gender
        combo_box = QtWidgets.QComboBox(self.wizardPage3)
        combo_box.setGeometry(QtCore.QRect(90, 400, 161, 31))
        combo_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(199, 199, 199, 0), stop:1 rgba(163, 163, 163, 64));\n"
"color: rgb(255, 255, 255);")
        combo_box.addItem("Male")
        combo_box.addItem("Female")
        
        # Title label
        self.label_20 = QtWidgets.QLabel(self.wizardPage3)
        self.label_20.setGeometry(QtCore.QRect(330, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.171, x2:1, y2:0.818, stop:0.142105 rgba(0, 46, 163, 37), stop:0.784211 rgba(0, 6, 130, 79));\n"
"color: rgb(0, 0, 0);")
        self.label_20.setObjectName("label_20")
        Wizard.addPage(self.wizardPage3)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Company Management System"))
        self.label_2.setText(_translate("Wizard", "Welcome To The Company Management System"))
        self.pushButton.setText(_translate("Wizard", "Login"))
        self.pushButton_2.setText(_translate("Wizard", "Register"))
        self.label_6.setText(_translate("Wizard", "Email:"))
        self.label_7.setText(_translate("Wizard", "Password:"))
        self.pushButton_3.setText(_translate("Wizard", "Or Login With Face ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Wizard", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Wizard", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Wizard", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Wizard", "Job"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Wizard", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Wizard", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Wizard", "Gender"))
        self.pushButton_4.setText(_translate("Wizard", "Add"))
        self.pushButton_5.setText(_translate("Wizard", "Delete"))
        self.pushButton_6.setText(_translate("Wizard", "Delete All"))

        self.label_13.setText(_translate("Wizard", "Name and Surname:"))
        self.label_14.setText(_translate("Wizard", "Email:"))
        self.label_15.setText(_translate("Wizard", "Job:"))
        self.label_16.setText(_translate("Wizard", "Phone:"))
        self.label_17.setText(_translate("Wizard", "Salary:"))
        self.label_18.setText(_translate("Wizard", "Password:"))
        self.pushButton_7.setText(_translate("Wizard", "Done"))
        self.pushButton_8.setText(_translate("Wizard", "Face ID [Optional]"))
        self.label_19.setText(_translate("Wizard", "Gender:"))
        self.label_20.setText(_translate("Wizard", " Register"))
    
    def login_clicked(self):
        QtWidgets.QWizard.next(Wizard)
        
    def register_page(self):
        QtWidgets.QWizard.next(Wizard)
        QtWidgets.QWizard.next(Wizard)
        QtWidgets.QWizard.next(Wizard)
        
    def done_clicked(self):
        QtWidgets.QWizard.back(Wizard)
        QtWidgets.QWizard.back(Wizard)
        QtWidgets.QWizard.back(Wizard)

    def face_id(self):
        pass
        # yüz tanıma ekranı açılacak
        # tanınan kişi eğer datası varsa ismi labelin üstünde görünecek yoksa "kişi tanınanamdı"
        # kişi tanındıktan sonra db ekranı açılacak (wizardpage)
                                                                             
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

# register ekranındaki isimlerin labellarını kaldırıp .setPlaceholderText() kullan.
