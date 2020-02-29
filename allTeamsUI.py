# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allTeamsUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(678, 519)
        self.tableWidgetName = QtWidgets.QTableWidget(Dialog)
        self.tableWidgetName.setGeometry(QtCore.QRect(70, 130, 531, 301))
        self.tableWidgetName.setAlternatingRowColors(True)
        self.tableWidgetName.setRowCount(3)
        self.tableWidgetName.setColumnCount(5)
        self.tableWidgetName.setObjectName("tableWidgetName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "All the Teams"))

