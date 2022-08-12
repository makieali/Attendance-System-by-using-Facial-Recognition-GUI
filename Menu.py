from PyQt5 import QtCore, QtGui, QtWidgets
import take_attendace as ta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("UCPFINAL.png"))
        self.logo.setObjectName("logo")
        self.takeattendance = QtWidgets.QPushButton(self.centralwidget)
        self.takeattendance.setGeometry(QtCore.QRect(40, 160, 181, 25))
        self.takeattendance.setObjectName("takeattendance")
        self.takeattendance.clicked.connect(self.attendance)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.loginmenu = QtWidgets.QMenu(self.menubar)
        self.loginmenu.setObjectName("loginmenu")
        self.helpmenu = QtWidgets.QMenu(self.menubar)
        self.helpmenu.setObjectName("helpmenu")
        MainWindow.setMenuBar(self.menubar)
        self.adminlogin = QtWidgets.QAction(MainWindow)
        self.adminlogin.setObjectName("adminlogin")
        self.adminlogin.triggered.connect(self.adminlog)
        self.teacherlogin = QtWidgets.QAction(MainWindow)
        self.teacherlogin.setObjectName("teacherlogin")
        self.teacherlogin.triggered.connect(self.teacherlog)
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.actionEXIT.triggered.connect(self.exit)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionContact_Us = QtWidgets.QAction(MainWindow)
        self.actionContact_Us.setObjectName("actionContact_Us")
        self.loginmenu.addAction(self.adminlogin)
        self.loginmenu.addAction(self.teacherlogin)
        self.loginmenu.addAction(self.actionEXIT)
        self.helpmenu.addAction(self.actionManual)
        self.helpmenu.addAction(self.actionContact_Us)
        self.menubar.addAction(self.loginmenu.menuAction())
        self.menubar.addAction(self.helpmenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.takeattendance.setText(_translate("MainWindow", "TAKE ATTENDANCE"))
        self.loginmenu.setTitle(_translate("MainWindow", "Login"))
        self.helpmenu.setTitle(_translate("MainWindow", "Help"))
        self.adminlogin.setText(_translate("MainWindow", "Admin Login"))
        self.teacherlogin.setText(_translate("MainWindow", "Teacher Login"))
        self.actionEXIT.setText(_translate("MainWindow", "Exit"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionContact_Us.setText(_translate("MainWindow", "Contact Us"))

    def attendance(self):
        print("Take attendance")
    def adminlog(self):
        print("Admin loginscreen")

    def teacherlog(self):
        print("TeacherLogin")



    def exit(self):
        print("Exit")
