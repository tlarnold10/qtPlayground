# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 194)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 141, 16))
        self.label.setObjectName("label")
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(150, 90, 251, 20))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.namePushButton = QtWidgets.QPushButton(Dialog)
        self.namePushButton.setGeometry(QtCore.QRect(420, 90, 121, 23))
        self.namePushButton.setObjectName("namePushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Your Name"))
        self.namePushButton.setText(_translate("Dialog", "Enter Your Name"))

