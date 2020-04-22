#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow_TableWidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/22 9:06
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate, pyqtSlot
from PyQt5.QtGui import QFont, QBrush, QIcon
from enum import Enum
from ui_TableWidget import Ui_MainWindow


class CellType(Enum):  # 各单元格的类型
    ctName = 1000
    ctSex = 1001
    ctBirth = 1002
    ctNation = 1003
    ctScore = 1004
    ctPartyM = 1005


class FieldColNum(Enum):  # 各字段在表格中的列号
    colName = 0
    colSex = 1
    colBirth = 2
    colNation = 3
    colScore = 4
    colPartyM = 5


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 添加状态栏和控件
        self.LabCellIndex = QLabel("当前单元格坐标：", self)
        self.LabCellIndex.setMinimumWidth(335)
        self.LabCellType = QLabel("当前单元格类型：", self)
        self.LabCellType.setMinimumWidth(250)
        self.LabStudID = QLabel("学生ID：", self)
        self.LabStudID.setMinimumWidth(200)
        self.ui.statusbar.addWidget(self.LabCellIndex)
        self.ui.statusbar.addWidget(self.LabCellType)
        self.ui.statusbar.addWidget(self.LabStudID)

        self.ui.tableWidget.setAlternatingRowColors(True)  # 交替行颜色
        self.__tableInitialized = False  # 表格数据未初始化

        # ===================================================信号与槽连接
        # 设置表头
        self.ui.btnSetHeader.clicked.connect(self.do_btn_set_header_clicked)
        # 设置行数
        self.ui.btnSetRows.clicked.connect(self.do_btn_set_rows_clicked)
        # 初始化表格数据
        self.ui.btnIniData.clicked.connect(self.do_btn_ini_data_clicked)
        # 当前单元格发生变化
        self.ui.tableWidget.currentCellChanged.connect(self.do_table_widget_current_cell_changed)
        # 插入行
        self.ui.btnInsertRow.clicked.connect(self.do_btn_insert_row_clicked)
        # 添加行
        self.ui.btnAppendRow.clicked.connect(self.do_btn_append_row_clicked)
        # 删除当前行
        self.ui.btnDelCurRow.clicked.connect(self.do_btn_del_currow_clicked)
        # 清空表格内容
        self.ui.btnClearContents.clicked.connect(self.do_btn_clear_content_clicked)
        # 自动调整行高
        self.ui.btnAutoHeight.clicked.connect(self.do_btn_auto_height_clicked)
        # 自动调整列宽
        self.ui.btnAutoWidth.clicked.connect(self.do_btn_auto_width_clicked)

    # 设置表头
    def do_btn_set_header_clicked(self):
        headerText = ["姓 名", "性 别", "出生日期", "民 族", "分 数", "是否党员"]
        self.ui.tableWidget.setColumnCount(len(headerText))  # 设置列数
        for i in range(len(headerText)):
            headerItem = QTableWidgetItem(headerText[i])
            font = headerItem.font()
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setForeground(QBrush(Qt.red))  # 前景色，即文字颜色
            self.ui.tableWidget.setHorizontalHeaderItem(i, headerItem)

    # 设置行数
    def do_btn_set_rows_clicked(self):
        self.ui.tableWidget.setRowCount(self.ui.spinBox.value())  # 设置工作区行数
        self.ui.tableWidget.setAlternatingRowColors(self.ui.chkBoxRowColor.isChecked())

    # 初始化表格数据
    def do_btn_ini_data_clicked(self):
        self.ui.tableWidget.clearContents()  # 清除表格内容
        birth = QDate(1998, 6, 23)
        isParty = True
        nation = "汉族"
        score = 70

        rowCount = self.ui.tableWidget.rowCount()
        for i in range(rowCount):
            strName = "学生%d" % i
            if (i % 2) == 0:
                strSex = "男"
            else:
                strSex = "女"
            self.__createItemsARow(i, strName, strSex, birth, nation, isParty, score)
            birth = birth.addDays(20)
            isParty = not isParty
        self.__tableInitialized = True

    # 设置每一列单元格的样式
    def __createItemsARow(self, rowNo, name, sex, birth, nation, isParty, score):
        studID = 201805000 + rowNo  # 学号

        # 姓名
        item = QTableWidgetItem(name, CellType.ctName.value)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole, studID)  # 关联数据
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colName.value, item)

        # 性别
        if sex == "男":
            icon = QIcon("./Image/Icon/boy.jpg")
        else:
            icon = QIcon("./Image/Icon/girl.jpg")
        item = QTableWidgetItem(sex, CellType.ctSex.value)
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colSex.value, item)

        # 出生日期
        strBirth = birth.toString("yyyy-MM-dd")  # 日期转换为字符串
        item = QTableWidgetItem(strBirth, CellType.ctBirth.value)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colBirth.value, item)

        # 民族
        item = QTableWidgetItem(nation, CellType.ctNation.value)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        if nation != "汉族":
            item.setForeground(QBrush(Qt.blue))
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colNation.value, item)

        # 分数
        strScore = str(score)
        item = QTableWidgetItem(strScore, CellType.ctScore.value)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colScore.value, item)

        # 党员
        item = QTableWidgetItem("党员", CellType.ctPartyM.value)
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        if isParty:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)  # 不允许编辑文字
        item.setBackground(QBrush(Qt.yellow))
        self.ui.tableWidget.setItem(rowNo, FieldColNum.colPartyM.value, item)

    # 当前单元格发生变化时
    @pyqtSlot(int, int, int, int)
    def do_table_widget_current_cell_changed(self, currentRow, currentColumn, previousRow, previousColumn):
        if not self.__tableInitialized:  # 表格数据未初始化
            return
        item = self.ui.tableWidget.item(currentRow, currentColumn)
        if item is None:
            return
        self.LabCellIndex.setText("当前单元格：%d行，%d列" % (currentRow, currentColumn))
        itemCellType = item.type()  # 获取单元格的类型
        self.LabCellType.setText("当前单元格类型：%d" % itemCellType)

        item2 = self.ui.tableWidget.item(currentRow, FieldColNum.colName.value)
        studID = item2.data(Qt.UserRole)  # 读取用户自定义数据
        self.LabStudID.setText("学生ID：%d" % studID)

    # 插入行
    def do_btn_insert_row_clicked(self):
        curRow = self.ui.tableWidget.currentRow()  # 当前行号
        self.ui.tableWidget.insertRow(curRow)
        birth = QDate.fromString("1998-4-5", "yyyy-M-d")
        self.__createItemsARow(curRow, "新学生", "男", birth, "苗族", True, 65)

    # 添加行
    def do_btn_append_row_clicked(self):
        curRow = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(curRow)
        birth = QDate.fromString("1991-1-10", "yyyy-M-d")
        self.__createItemsARow(curRow, "新生", "女", birth, "土家族", False, 86)

    # 删除当前行
    def do_btn_del_currow_clicked(self):
        curRow = self.ui.tableWidget.currentRow()  # 当前行号
        self.ui.tableWidget.removeRow(curRow)

    # 清空表格内容
    def do_btn_clear_content_clicked(self):
        self.ui.tableWidget.clearContents()

    # 自动调整行高
    def do_btn_auto_height_clicked(self):
        self.ui.tableWidget.resizeRowsToContents()

    # 自动调整列宽
    def do_btn_auto_width_clicked(self):
        self.ui.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())