#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myWidget_tiner.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/10 9:25
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QTimer

from ui_timer import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timer = QTimer()  # 创建定时器
        self.timer.stop()  # 停止
        self.timer.setInterval(1000)  # 定时周期1000ms
        self.timer.timeout.connect(self.do_timer_timeout)
        self.counter = QTime()  # 创建计时器

    def on_btnStart_clicked(self):
        self.timer.start()  # 开始定时
        self.counter.start()
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.btnSetIntv.setEnabled(False)

    def on_btnSetIntv_clicked(self):  # #设置定时器的周期
        self.timer.setInterval(self.ui.spinBoxIntv.value())

    def on_btnStop_clicked(self):
        self.timer.stop()  # 定时器停止
        tmMs = self.counter.elapsed()  # 计时器经过的毫秒数
        ms = tmMs % 1000  # 取余数，毫秒
        sec = tmMs/1000  # 整秒
        timeStr = "经过的时间：%d 秒，%d 毫秒" % (sec, ms)
        self.ui.LabElapsedTime.setText(timeStr)
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnSetIntv.setEnabled(True)

    def do_timer_timeout(self):  # 定时中断响应
        curTime = QTime.currentTime()  # 获取当前时间
        self.ui.LCDHour.display(curTime.hour())
        self.ui.LCDMin.display(curTime.minute())
        self.ui.LCDSec.display(curTime.second())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
