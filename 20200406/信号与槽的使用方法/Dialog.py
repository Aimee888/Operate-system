# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chkBoxUnder = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxUnder.setObjectName("chkBoxUnder")
        self.horizontalLayout_3.addWidget(self.chkBoxUnder)
        self.chkBoxItalic = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxItalic.setObjectName("chkBoxItalic")
        self.horizontalLayout_3.addWidget(self.chkBoxItalic)
        self.chkBoxBold = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxBold.setObjectName("chkBoxBold")
        self.horizontalLayout_3.addWidget(self.chkBoxBold)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioBlack = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBlack.setObjectName("radioBlack")
        self.horizontalLayout_4.addWidget(self.radioBlack)
        self.radioRed = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioRed.setObjectName("radioRed")
        self.horizontalLayout_4.addWidget(self.radioRed)
        self.radioBlue = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBlue.setObjectName("radioBlue")
        self.horizontalLayout_4.addWidget(self.radioBlue)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_2.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_2.addWidget(self.btnOK)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.btnOK.clicked.connect(Dialog.accept)
        self.btnClose.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Demo2-3信号与槽"))
        self.chkBoxUnder.setText(_translate("Dialog", "Underline"))
        self.chkBoxItalic.setText(_translate("Dialog", "Italic"))
        self.chkBoxBold.setText(_translate("Dialog", "Bold"))
        self.radioBlack.setText(_translate("Dialog", "Black"))
        self.radioRed.setText(_translate("Dialog", "Red"))
        self.radioBlue.setText(_translate("Dialog", "Blue"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "PyQt5 编程指南\n"
"Python 和 Qt."))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.btnOK.setText(_translate("Dialog", "确定"))
        self.btnClose.setText(_translate("Dialog", "退出"))
