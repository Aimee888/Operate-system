# 1_test.py
# 使用PyQt5，纯代码创建一个简单的GUI程序
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)      # 创建app，用QApplication类
widgetHello = QtWidgets.QWidget()           # 创建窗体，用QWidget类
widgetHello.resize(280, 150)                # 设置窗体的宽度和高度
widgetHello.setWindowTitle("Hello World")   # 设置窗体的标题文字

LabHello = QtWidgets.QLabel(widgetHello)    # 创建标签，父容器为widgetHello
LabHello.setText("Hello World, PyQt5")      # 设置标签文字
font = QtGui.QFont()                        # 创建字体对象font，用QFont类
font.setPointSize(12)                       # 设置字体大小
font.setBold(True)                          # 设置为粗体
LabHello.setFont(font)                      # 设置为标签LableHello的字体
size = LabHello.sizeHint()                  # 获取LabelHello的合适大小，返回值是Qsize类对象
LabHello.setGeometry(70, 60, size.width(), size.height())

widgetHello.show()                          # 显示对话框
sys.exit(app.exec_())                       # 应用程序运行
