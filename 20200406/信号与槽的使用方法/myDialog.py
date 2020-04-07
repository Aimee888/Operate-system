# # 与UI窗体类对应的业务逻辑类
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, pyqtSlot
from Dialog import Ui_Dialog


class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # ///////////// 自行添加的部分 /////////////

        """
        这部分如果是按照槽函数命名规则命名的，可以注释掉，如果是自己命名的，那么需要加上。
        命名规则：on_<object name>_<signal name>(<signal parameters>)
        如清空按钮就是：on_btnClear_clicked
        """
        # ==================================================================
        # # 添加下划线
        # self.ui.chkBoxUnder.clicked.connect(self.on_chkBoxUnder_clicked)
        #
        # # 修改编辑框中字体为斜体
        # self.ui.chkBoxItalic.clicked.connect(self.on_chkBoxItalic_clicked)
        #
        # # # 修改编辑框中字体为斜体
        # # self.ui.chkBoxItalic.toggled.connect(self.on_chkBoxItalic_toggled)
        #
        # # 添加加粗效果
        # self.ui.chkBoxBold.toggled.connect(self.on_chkBoxBold_toggled)
        #
        # # 添加clear效果
        # self.ui.btnClear.clicked.connect(self.on_btnClear_clicked)
        # ==================================================================

        # 设置颜色关联函数
        self.ui.radioBlack.clicked.connect(self.do_setTextColor)
        self.ui.radioRed.clicked.connect(self.do_setTextColor)
        self.ui.radioBlue.clicked.connect(self.do_setTextColor)

    # #//////////////////自定义槽函数////////////////////

    # 设置文本颜色
    def do_setTextColor(self):
        plet = self.ui.plainTextEdit.palette()   # 获取palette
        if(self.ui.radioBlack.isChecked()):
            plet.setColor(QPalette.Text, Qt.black)
        elif(self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text, Qt.red)
        elif(self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)
        self.ui.plainTextEdit.setPalette(plet)

    # 将编辑框里面的文字添加下划线
    def on_chkBoxUnder_clicked(self):
        checked = self.ui.chkBoxUnder.isChecked()  # 读取勾选状态
        font = self.ui.plainTextEdit.font()
        font.setUnderline(checked)
        self.ui.plainTextEdit.setFont(font)

    # @pyqtSlot(bool)
    # # 将编辑框里面的文字变为斜体
    # def on_chkBoxItalic_clicked(self, checked):
    #     # checked = self.ui.chkBoxItalic.isChecked()
    #     font = self.ui.plainTextEdit.font()
    #     font.setItalic(checked)
    #     self.ui.plainTextEdit.setFont(font)

    # 将编辑框里面的文字变为斜体
    def on_chkBoxItalic_clicked(self):
        checked = self.ui.chkBoxItalic.isChecked()
        font = self.ui.plainTextEdit.font()
        font.setItalic(checked)
        self.ui.plainTextEdit.setFont(font)

    # # 将编辑框里面的文字变为斜体
    # def on_chkBoxItalic_toggled(self, checked):
    #     # checked = self.ui.chkBoxItalic.isChecked()
    #     font = self.ui.plainTextEdit.font()
    #     font.setItalic(checked)
    #     self.ui.plainTextEdit.setFont(font)

    # 将编辑框里面的内容加粗
    def on_chkBoxBold_toggled(self, checked):
        font = self.ui.plainTextEdit.font()
        font.setBold(checked)  # 参数checked表示勾选状态
        self.ui.plainTextEdit.setFont(font)

    # 清除编辑框里面的内容函数
    def on_btnClear_clicked(self):
        self.ui.plainTextEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
