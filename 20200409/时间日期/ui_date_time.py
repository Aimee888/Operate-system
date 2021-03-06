# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_date_time.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(683, 391)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 331, 361))
        self.groupBox.setObjectName("groupBox")
        self.btnGetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnGetTime.setGeometry(QtCore.QRect(70, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnGetTime.setFont(font)
        self.btnGetTime.setObjectName("btnGetTime")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 90, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setGeometry(QtCore.QRect(70, 90, 121, 22))
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(70, 180, 121, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.editTime = QtWidgets.QLineEdit(self.groupBox)
        self.editTime.setGeometry(QtCore.QRect(210, 90, 111, 20))
        self.editTime.setObjectName("editTime")
        self.btnSetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetTime.setGeometry(QtCore.QRect(210, 130, 111, 23))
        self.btnSetTime.setObjectName("btnSetTime")
        self.editDate = QtWidgets.QLineEdit(self.groupBox)
        self.editDate.setGeometry(QtCore.QRect(210, 180, 111, 20))
        self.editDate.setObjectName("editDate")
        self.btnSetDate = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDate.setGeometry(QtCore.QRect(210, 220, 111, 23))
        self.btnSetDate.setObjectName("btnSetDate")
        self.editDateTime = QtWidgets.QLineEdit(self.groupBox)
        self.editDateTime.setGeometry(QtCore.QRect(210, 270, 111, 20))
        self.editDateTime.setObjectName("editDateTime")
        self.btnSetDateTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDateTime.setGeometry(QtCore.QRect(210, 310, 111, 23))
        self.btnSetDateTime.setObjectName("btnSetDateTime")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(70, 270, 121, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 20, 331, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 80, 312, 261))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.editCalendar = QtWidgets.QLineEdit(self.groupBox_2)
        self.editCalendar.setGeometry(QtCore.QRect(140, 40, 171, 20))
        self.editCalendar.setObjectName("editCalendar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "日期时间"))
        self.btnGetTime.setText(_translate("Form", "读取当前日期时间"))
        self.label.setText(_translate("Form", "时 间"))
        self.timeEdit.setDisplayFormat(_translate("Form", "H:mm:ss"))
        self.label_2.setText(_translate("Form", "日 期"))
        self.label_3.setText(_translate("Form", "日期时间"))
        self.editTime.setInputMask(_translate("Form", "99:99:99;_"))
        self.btnSetTime.setText(_translate("Form", "设置时间"))
        self.editDate.setInputMask(_translate("Form", "9999-99-99"))
        self.btnSetDate.setText(_translate("Form", "设置日期"))
        self.editDateTime.setInputMask(_translate("Form", "9999-99-99 99:99:99"))
        self.btnSetDateTime.setText(_translate("Form", "设置时间日期"))
        self.dateTimeEdit.setDisplayFormat(_translate("Form", "yyyy/M/d H:mm:ss"))
        self.groupBox_2.setTitle(_translate("Form", "日历选择"))
        self.label_4.setText(_translate("Form", "选择的日期："))
