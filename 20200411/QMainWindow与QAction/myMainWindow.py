#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/11 14:44
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QActionGroup, QLabel, QProgressBar, QSpinBox, QFontComboBox)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QTextCharFormat, QFont

from ui_mainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置斜体
        self.ui.actFont_Italic.triggered.connect(self.do_act_font_italic_triggered)
        # 设置粗体
        self.ui.actFont_Bold.triggered.connect(self.do_act_font_bold_triggered)
        # 设置下划线
        self.ui.actFont_Underline.triggered.connect(self.do_act_underline_triggered)

    @pyqtSlot(bool)
    def do_act_font_italic_triggered(self, checked):  # 斜体
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontItalic(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def do_act_font_bold_triggered(self, checked):  # 粗体
        fmt = self.ui.plainTextEdit.currentCharFormat()
        if checked:
            fmt.setFontWeight(QFont.Bold)
        else:
            fmt.setFontWeight(QFont.Normal)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)

    @pyqtSlot(bool)
    def do_act_underline_triggered(self, checked):  # 下划线
        fmt = self.ui.plainTextEdit.currentCharFormat()
        fmt.setFontUnderline(checked)
        self.ui.plainTextEdit.mergeCurrentCharFormat(fmt)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
