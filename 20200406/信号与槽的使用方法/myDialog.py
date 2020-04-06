# # 与UI窗体类对应的业务逻辑类
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
