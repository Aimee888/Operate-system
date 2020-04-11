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


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
