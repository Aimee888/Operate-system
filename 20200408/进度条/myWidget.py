#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myWidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/8 14:29
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

from ui_proBar import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.horizontalSlider.setMaximum(200)
        self.ui.horizontalScrollBar.setMaximum(200)
        self.ui.progressBar.setMaximum(200)
        self.ui.horizontalSlider.valueChanged.connect(self.do_valueChanged)
        self.ui.horizontalScrollBar.valueChanged.connect(self.do_valueChanged)

    def on_radioButton_clicked(self):  # 显示格式 -- 百分比
        self.ui.progressBar.setFormat("%p%")

    def on_radioButton_2_clicked(self):  # 显示格式 -- 当前值
        self.ui.progressBar.setFormat("%v")

    @pyqtSlot(bool)  # # "textVisible" 复选框
    def on_checkBox_clicked(self, checked):
        self.ui.progressBar.setTextVisible(checked)

    @pyqtSlot(bool)  # # "InvertedAppearance" 复选框
    def on_checkBox_2_clicked(self,checked):
        self.ui.progressBar.setInvertedAppearance(checked)

    # # ========= 自定义槽函数 ==================
    def do_valueChanged(self, value):
        self.ui.progressBar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
