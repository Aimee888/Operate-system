# # appMain1.py
# # 使用ui_Form.py文件中的类Ui_Form创建app
import sys
from PyQt5 import QtWidgets
import Form

app = QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()   # 创建窗体的基类QWidget的实例

ui = Form.Ui_Form()
ui.setupUi(baseWidget)  # 以baseWidget作为传递参数，创建完整窗体

baseWidget.show()
ui.label.setText("Hello, 被程序修改")  # 可以修改窗体上标签的文字
sys.exit(app.exec_())
