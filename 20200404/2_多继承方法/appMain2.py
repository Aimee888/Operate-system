# # appMain2.py  多继承方法
"""
多继承方式优缺点：
1. 界面上的组件都成为窗体业务逻辑类QmyWidget的公共属性，外界可以直接访问。优点是访问方便，缺点是过于开放，
    不符合面向对象严格封装的设计思想
2. 界面上的组件与QmyWidget类里新定义的属性混合在一起了，不便于区分。当窗体上的界面组件较多，
    且窗体业务逻辑类里定义的属性也很多时，就难以区分哪个属性是界面上的组件，哪个属性是在业务逻辑类里新定义的，
    这样不利于界面与业务逻辑分离。
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Form import Ui_Form


class QmyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)   # 调用父类构造函数，创建QWidget窗体
        
        self.Lab = "多重继承的QmyWidget"   # 新定义的一个变量
        self.setupUi(self)  # self是QWidget窗体，可作为参数传给setupui()
        self.label.setText(self.Lab)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.btnClose.setText("不关闭了")
    sys.exit(app.exec_())
