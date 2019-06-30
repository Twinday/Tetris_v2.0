# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 481, 691))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setRowCount(22)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(510, 40, 75, 23))
        self.buttonStart.setObjectName("buttonStart")
        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setGeometry(QtCore.QRect(500, 140, 151, 71))
        self.label_score.setText("")
        self.label_score.setObjectName("label_score")
        self.label_level = QtWidgets.QLabel(self.centralwidget)
        self.label_level.setGeometry(QtCore.QRect(500, 420, 131, 51))
        self.label_level.setText("")
        self.label_level.setObjectName("label_level")
        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.btn_info.setObjectName("btn_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
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
        self.buttonStart.setText(_translate("MainWindow", "New Game"))
        self.btn_info.setText(_translate("MainWindow", "Information"))

