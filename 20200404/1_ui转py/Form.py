# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Demo2_2"))
        self.label.setText(_translate("Form", "Hello, by UI Designer"))
        self.btnClose.setText(_translate("Form", "关闭"))
