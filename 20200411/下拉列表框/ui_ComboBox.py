# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(433, 193)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 391, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 89, 231, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnIniItems = QtWidgets.QPushButton(self.groupBox_2)
        self.btnIniItems.setGeometry(QtCore.QRect(10, 30, 75, 21))
        self.btnIniItems.setObjectName("btnIniItems")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.chkBoxEditable = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBoxEditable.setGeometry(QtCore.QRect(170, 30, 70, 17))
        self.chkBoxEditable.setObjectName("chkBoxEditable")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 89, 171, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnIni2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btnIni2.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.btnIni2.setObjectName("btnIni2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 60, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "选择的内容"))
        self.groupBox_2.setTitle(_translate("Form", "简单的ComboBox"))
        self.btnIniItems.setText(_translate("Form", "初始化列表"))
        self.pushButton_2.setText(_translate("Form", "清除列表"))
        self.chkBoxEditable.setText(_translate("Form", "可编辑"))
        self.groupBox_3.setTitle(_translate("Form", "有用户数据的ComboBox"))
        self.btnIni2.setText(_translate("Form", "初始化城市+区号"))
