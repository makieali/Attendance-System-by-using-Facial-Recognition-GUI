import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setStyleSheet("background-color:rgb(32, 74, 135)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(10, 0, 381, 281))
        self.camera.setFrameShape(QtWidgets.QFrame.Box)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setLineWidth(4)
        self.camera.setText("")
        self.camera.setPixmap(QtGui.QPixmap("../../Desktop/HAAR/profile.png"))
        self.camera.setObjectName("camera")
        self.TITLE1 = QtWidgets.QLabel(self.centralwidget)
        self.TITLE1.setGeometry(QtCore.QRect(400, 0, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TITLE1.setFont(font)
        self.TITLE1.setStyleSheet("color:rgb(238, 238, 236)")
        self.TITLE1.setObjectName("TITLE1")
        self.TITLE2 = QtWidgets.QLabel(self.centralwidget)
        self.TITLE2.setGeometry(QtCore.QRect(400, 60, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TITLE2.setFont(font)
        self.TITLE2.setStyleSheet("color:rgb(238, 238, 236)")
        self.TITLE2.setObjectName("TITLE2")
        self.TIME = QtWidgets.QLabel(self.centralwidget)
        self.TIME.setGeometry(QtCore.QRect(400, 120, 401, 81))
        self.TIME.setText("")
        self.TIME.setObjectName("TIME")

        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(400, 200, 401, 81))
        self.date.setText("")
        self.date.setObjectName("date")
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(0, 290, 621, 301))
        self.Table.setAutoFillBackground(False)
        self.Table.setStyleSheet("color:rgb(238, 238, 236)")
        self.Table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Table.setLineWidth(2)
        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(4)
        self.Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, item)
        self.Table.setColumnWidth(0,150)
        self.Table.setColumnWidth(1, 150)
        self.Table.setColumnWidth(2, 150)
        self.Table.setColumnWidth(3, 150)
        self.cameraselection = QtWidgets.QComboBox(self.centralwidget)
        self.cameraselection.setGeometry(QtCore.QRect(625, 294, 171, 31))
        self.cameraselection.setStyleSheet("color:rgb(255, 255, 255)")
        self.cameraselection.setEditable(False)
        self.cameraselection.setMaxVisibleItems(2)
        self.cameraselection.setMaxCount(2)
        self.cameraselection.setObjectName("cameraselection")
        self.cameraselection.addItem("")
        self.cameraselection.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 330, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startcamera)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 390, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.outputscreen = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputscreen.setGeometry(QtCore.QRect(620, 450, 171, 111))
        self.outputscreen.setObjectName("outputscreen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 799, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuActions = QtWidgets.QMenu(self.menuBar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionStart_Attendance = QtWidgets.QAction(MainWindow)
        self.actionStart_Attendance.setObjectName("actionStart_Attendance")
        self.actionStop_Attendance = QtWidgets.QAction(MainWindow)
        self.actionStop_Attendance.setObjectName("actionStop_Attendance")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionExport_attendance = QtWidgets.QAction(MainWindow)
        self.actionExport_attendance.setObjectName("actionExport_attendance")
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionHome)
        self.menuActions.addAction(self.actionExport_attendance)
        self.menuBar.addAction(self.menuActions.menuAction())


        self.retranslateUi(MainWindow)
        self.cameraselection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TITLE1.setText(_translate("MainWindow", "              LIVE ATTENDANCE"))
        self.TITLE2.setText(_translate("MainWindow", "            BY USING FACIAL RECOGNITION"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "StudentID"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "StudentName"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ArrivalTime"))
        self.cameraselection.setCurrentText(_translate("MainWindow", "Default Camera"))
        self.cameraselection.setItemText(0, _translate("MainWindow", "Default Camera"))
        self.cameraselection.setItemText(1, _translate("MainWindow", "External Camera"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionStart_Attendance.setText(_translate("MainWindow", "Start Attendance"))
        self.actionStop_Attendance.setText(_translate("MainWindow", "Stop Attendance"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionExport_attendance.setText(_translate("MainWindow", "Export attendance"))

    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)

        self.lbl.setText(displayTxt)

    def startcamera(self):

        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile('trainer/trainer.yml')
        i = 0
        if exists3:
            recognizer.read('trainer/trainer.yml')
            harcascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']

            exists1 = os.path.isfile("Student_Details.csv")
            if exists1:
                df = pd.read_csv("Student_Details.csv")

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
                    serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                    if (conf < 40):
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        name = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                        ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                        ID = str(ID)
                        ID = ID[1:-1]
                        bb = str(name)
                        bb = bb[2:-2]
                        attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                        # print("face match and the serial,ID and name ", serial,bb,ID)
                        cv2.putText(img, bb, (x, y + h), font, 1, (255, 255, 255), 2)
                    else:
                        id = 'Unknown'
                        bb = str(id)
                        cv2.putText(img, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                cv2.imshow('Taking Attendance', img)
                if (cv2.waitKey(1) == ord('q')):
                    cam.release()
                    cv2.destroyAllWindows()
                    break
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")
            if exists:
                with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(attendance)
                csvFile1.close()
            else:
                with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(col_names)
                    writer.writerow(attendance)
                csvFile1.close()
            with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for lines in reader1:
                   #self.Table.setItem(i,0,QtWidgets.QTableWidgetItem(lines["Id"]))
                   #self.Table.setItem(i, 1, QtWidgets.QTableWidgetItem(lines["Name"]))
                   #self.Table.setItem(i, 2, QtWidgets.QTableWidgetItem(lines["Date"]))
                   #self.Table.setItem(i, 2, QtWidgets.QTableWidgetItem(lines["Time"]))
                   i=i+1
            csvFile1.close()