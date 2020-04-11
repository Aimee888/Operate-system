#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myWidget_ComboBox.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/11 9:48
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

from ui_ComboBox import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.btnIni2.clicked.connect(self.on_btn_ini2_clicked)
        self.ui.comboBox_2.currentIndexChanged[str].connect(self.combo_box_current_index_change)

    def on_btnIniItems_clicked(self):  # 初始化列表按钮
        icon = QIcon("./icons/images/aim.ico")
        self.ui.comboBox.clear()  # 清除列表
        provinces = ["山东", "河北", "河南", "湖北", "湖南", "广东"]  # 列表数据
        # self.ui.comboBox.addItems(provinces)  # 直接添加列表，但无法加图标
        for i in range(len(provinces)):
            self.ui.comboBox.addItem(icon, provinces[i])

    @pyqtSlot(bool)  # 可编辑CheckBox
    def on_chkBoxEditable_clicked(self, checked):
        self.ui.comboBox.setEditable(checked)

    @pyqtSlot(str)  # 简单的ComboBox的当前项变化
    def on_comboBox_currentIndexChanged(self, curText):
        self.ui.lineEdit.setText(curText)

    def on_btn_ini2_clicked(self):  # 有用户数据的comboBox2的初始化
        icon = QIcon("./icons/images/unit.ico")
        self.ui.comboBox_2.clear()
        cities = {"北京": 10, "上海": 21, "天津": 22, "徐州": 516, "福州": 591, "青岛": 532}  # 字典数据
        for k in cities:
            # print(k)
            self.ui.comboBox_2.addItem(icon, k, cities[k])

    def combo_box_current_index_change(self, curText):
        self.ui.lineEdit.setText(curText)
        zone = self.ui.comboBox_2.currentData()  # 读取关联数据
        if zone is not None:
            self.ui.lineEdit.setText(curText + ":区号=%d" % zone)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
