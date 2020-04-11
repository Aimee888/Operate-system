# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 531, 291))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actFont_Italic = QtWidgets.QAction(MainWindow)
        self.actFont_Italic.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/images/Italic.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_Italic.setIcon(icon)
        self.actFont_Italic.setObjectName("actFont_Italic")
        self.actFont_Bold = QtWidgets.QAction(MainWindow)
        self.actFont_Bold.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/images/Bold.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_Bold.setIcon(icon1)
        self.actFont_Bold.setObjectName("actFont_Bold")
        self.actFont_Underline = QtWidgets.QAction(MainWindow)
        self.actFont_Underline.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/images/underline.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_Underline.setIcon(icon2)
        self.actFont_Underline.setObjectName("actFont_Underline")
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.actFont_Italic)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFont_Bold)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFont_Underline)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑(E)"))
        self.menu_3.setTitle(_translate("MainWindow", "格式(M)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actFont_Italic.setText(_translate("MainWindow", "斜体"))
        self.actFont_Italic.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">斜体</span></p></body></html>"))
        self.actFont_Bold.setText(_translate("MainWindow", "粗体"))
        self.actFont_Bold.setToolTip(_translate("MainWindow", "加粗"))
        self.actFont_Underline.setText(_translate("MainWindow", "下划线"))
        self.actFont_Underline.setToolTip(_translate("MainWindow", "下划线"))
