#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myWidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/9 15:33
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QDateTime, QDate, QTime
from ui_date_time import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

    # # ============由connectSlotByName() 自动关联的槽函数 ======================
    def on_btnGetTime_clicked(self):  # # 读取当前日期时间按钮
        curDateTime = QDateTime.currentDateTime()
        self.ui.timeEdit.setTime(curDateTime.time())
        self.ui.editTime.setText(curDateTime.toString("hh:mm:ss"))
        self.ui.dateEdit.setDate(curDateTime.date())
        self.ui.editDate.setText(curDateTime.toString("yyyy-MM-dd"))
        self.ui.dateTimeEdit.setDateTime(curDateTime)
        self.ui.editDateTime.setText(curDateTime.toString("yyyy-MM-dd hh:mm:ss"))

    def on_calendarWidget_selectionChanged(self):
        date = self.ui.calendarWidget.selectedDate()
        self.ui.editCalendar.setText(date.toString("yyyy年M月d日"))

    def on_btnSetTime_clicked(self):  # 设置时间按钮
        tmStr = self.ui.editTime.text()
        tm = QTime.fromString(tmStr, "hh:mm:ss")
        self.ui.timeEdit.setTime(tm)

    def on_btnSetDate_clicked(self):  # 设置日期按钮
        dtStr = self.ui.editDate.text()
        dt = QDate.fromString(dtStr, "yyyy-MM-dd")
        self.ui.dateEdit.setDate(dt)

    def on_btnSetDateTime_clicked(self):
        dttmStr = self.ui.editDateTime.text()
        dttm = QDateTime.fromString(dttmStr, "yyyy-MM-dd hh:mm:ss")
        self.ui.dateTimeEdit.setDateTime(dttm)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
