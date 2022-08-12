from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids


class Ui_AddStudentWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("color:rgb(52, 101, 164)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 6, 791, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/bg2.png"))
        self.label.setObjectName("label")
        self.Nameinput = QtWidgets.QLineEdit(self.centralwidget)
        self.Nameinput.setGeometry(QtCore.QRect(120, 50, 191, 31))
        self.Nameinput.setText("")
        self.Nameinput.setObjectName("Nameinput")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(50, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setStyleSheet("color:rgb(255, 255, 255)")
        self.Name.setObjectName("Name")
        self.ID = QtWidgets.QLabel(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(80, 90, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ID.setFont(font)
        self.ID.setStyleSheet("color:rgb(255, 255, 255)")
        self.ID.setObjectName("ID")
        self.Gender = QtWidgets.QLabel(self.centralwidget)
        self.Gender.setGeometry(QtCore.QRect(40, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Gender.setFont(font)
        self.Gender.setStyleSheet("color:rgb(255, 255, 255)")
        self.Gender.setObjectName("Gender")
        self.ismale = QtWidgets.QRadioButton(self.centralwidget)
        self.ismale.setGeometry(QtCore.QRect(140, 130, 112, 41))
        self.ismale.setStyleSheet("color:rgb(255, 255, 255)")
        self.ismale.setObjectName("ismale")
        self.isFemale = QtWidgets.QRadioButton(self.centralwidget)
        self.isFemale.setGeometry(QtCore.QRect(210, 130, 112, 41))
        self.isFemale.setStyleSheet("color:rgb(255, 255, 255)")
        self.isFemale.setObjectName("isFemale")
        self.idinput = QtWidgets.QLineEdit(self.centralwidget)
        self.idinput.setGeometry(QtCore.QRect(120, 90, 191, 31))
        self.idinput.setText("")
        self.idinput.setObjectName("idinput")
        self.Email = QtWidgets.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(40, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setStyleSheet("color:rgb(255, 255, 255)")
        self.Email.setObjectName("Email")
        self.Contact = QtWidgets.QLabel(self.centralwidget)
        self.Contact.setGeometry(QtCore.QRect(30, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Contact.setFont(font)
        self.Contact.setStyleSheet("color:rgb(255, 255, 255)")
        self.Contact.setObjectName("Contact")
        self.Emailinput = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailinput.setGeometry(QtCore.QRect(120, 180, 191, 31))
        self.Emailinput.setText("")
        self.Emailinput.setObjectName("Emailinput")
        self.ContactInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ContactInput.setGeometry(QtCore.QRect(120, 220, 191, 31))
        self.ContactInput.setText("")
        self.ContactInput.setObjectName("ContactInput")
        self.TakeImages = QtWidgets.QPushButton(self.centralwidget)
        self.TakeImages.setGeometry(QtCore.QRect(120, 310, 141, 41))
        self.TakeImages.setObjectName("TakeImages")
        self.TakeImages.clicked.connect(self.TakeImagessample)
        self.Saveprofile = QtWidgets.QPushButton(self.centralwidget)
        self.Saveprofile.setGeometry(QtCore.QRect(120, 380, 141, 41))
        self.Saveprofile.setStatusTip("")
        self.Saveprofile.setObjectName("Saveprofile")
        self.Saveprofile.clicked.connect(self.saveandtrain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setText(_translate("MainWindow", "Name:"))
        self.ID.setText(_translate("MainWindow", "ID:"))
        self.Gender.setText(_translate("MainWindow", "Gender:"))
        self.ismale.setText(_translate("MainWindow", "male"))
        self.isFemale.setText(_translate("MainWindow", "Female"))
        self.Email.setText(_translate("MainWindow", "Email:"))
        self.Contact.setText(_translate("MainWindow", "Contact :"))
        self.TakeImages.setText(_translate("MainWindow", "Take Images"))
        self.Saveprofile.setText(_translate("MainWindow", "Save Profile"))


    def TakeImagessample(self):
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME','' , 'Gender', '', 'Email', '', 'CONTACT']
        serial = 0
        exists = os.path.isfile('Student_Details.csv')
        if exists:
            with open('Student_Details.csv', 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            # serial = (serial // 2)
            csvFile1.close()
        else:
            with open('Student_Details.csv', 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()

        Id = self.idinput.text()
        name = self.Nameinput.text()
        if self.ismale.isChecked():
            gender = 'Male'
        if self.isFemale.isChecked():
            gender = 'Female'

        Email = self.Emailinput.text()
        Contact = self.ContactInput.text()

        cam = cv2.VideoCapture(0)

        cam.set(3, 640)  # set video width
        cam.set(4, 480)  # set video height
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count
        count = 0

        # start detect your face and take 100 pictures
        while (True):

            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/ " + name + "." + str(serial) + "." + Id + '.' + str(count) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 50:  # Take 30 face sample and stop video
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        #res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name,'',gender,'',Email,'',Contact,'']
        with open('Student_Details.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    def saveandtrain(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath);

        print("\n [INFO] Training faces. It will take a few seconds. Wait ...")

        faces, ids = getImagesAndLabels("dataset")
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.save('trainer/trainer.yml')

        #res = "Profile Saved Successfully"
