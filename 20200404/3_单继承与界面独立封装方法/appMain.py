# # appMain.py 单继承方法，能更好地进行界面与逻辑的分离
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Form import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗体
        self.__ui = Ui_Form()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI
        self.Lab = "单继承的QmyWidget"
        self.__ui.label.setText(self.Lab)

    def set_btn_text(self, a_text):
        self.__ui.btnClose.setText(a_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.set_btn_text("间接设置")
    sys.exit(app.exec_())
