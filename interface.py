# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConvertButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConvertButton.setGeometry(QtCore.QRect(320, 90, 141, 51))
        self.ConvertButton.setObjectName("ConvertButton")
        self.ToAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.ToAmount.setGeometry(QtCore.QRect(20, 10, 211, 71))
        self.ToAmount.setObjectName("ToAmount")
        self.Result = QtWidgets.QLineEdit(self.centralwidget)
        self.Result.setEnabled(True)
        self.Result.setGeometry(QtCore.QRect(460, 10, 211, 71))
        self.Result.setReadOnly(True)
        self.Result.setObjectName("Result")
        self.FromCurr = QtWidgets.QComboBox(self.centralwidget)
        self.FromCurr.setGeometry(QtCore.QRect(230, 10, 91, 71))
        self.FromCurr.setObjectName("FromCurr")
        self.ToCurr = QtWidgets.QComboBox(self.centralwidget)
        self.ToCurr.setGeometry(QtCore.QRect(670, 10, 91, 71))
        self.ToCurr.setObjectName("ToCurr")
        self.ReverseCurr = QtWidgets.QPushButton(self.centralwidget)
        self.ReverseCurr.setGeometry(QtCore.QRect(350, 20, 81, 51))
        self.ReverseCurr.setObjectName("ReverseCurr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.ConvertButton.setText(_translate("MainWindow", "КОНВЕРТИРОВАТЬ"))
        self.ReverseCurr.setText(_translate("MainWindow", "↔"))
