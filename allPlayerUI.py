# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allPlayersUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 454)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidgetName = QtWidgets.QTableWidget(Dialog)
        self.tableWidgetName.setGeometry(QtCore.QRect(90, 90, 441, 301))
        self.tableWidgetName.setAlternatingRowColors(True)
        self.tableWidgetName.setRowCount(3)
        self.tableWidgetName.setColumnCount(2)
        self.tableWidgetName.setObjectName("tableWidgetName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "All the Players"))

