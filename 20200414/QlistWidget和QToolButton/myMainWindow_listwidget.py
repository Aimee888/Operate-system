#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow_listwidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/14 9:24
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMenu, QToolButton
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import pyqtSlot, Qt
from ui_listwidget import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.splitter)  # 使splitter充满整个工作区
        self.__set_actions_for_button()  # ToolButton关联Action
        self.__create_selection_pop_menu()
        self.__FlagEditable = Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        self.__FlagNotEditable = Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled

        self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        # 初始化列表
        self.ui.actList_Ini.triggered.connect(self.do_act_list_ini_triggered)
        # 插入一项
        self.ui.actList_Insert.triggered.connect(self.do_act_list_insert_triggered)
        # 添加一项
        self.ui.actList_Append.triggered.connect(self.do_act_list_append_triggered)
        # 删除当前项
        self.ui.actList_Delete.triggered.connect(self.do_act_list_delete_triggered)
        # 清空列表
        self.ui.actList_Clear.triggered.connect(self.do_act_list_clear_triggered)

        # 全选
        self.ui.actSel_ALL.triggered.connect(self.do_act_sel_all_triggered)
        # 全不选
        self.ui.actSel_None.triggered.connect(self.do_act_sel_none_triggered)
        # 反选
        self.ui.actSel_Invs.triggered.connect(self.do_act_sel_invs_triggered)
        # 当选择项发生变化时
        self.ui.listWidget.currentItemChanged.connect(self.do_list_widget_current_item_changed)
        # 右键快捷菜单
        self.ui.listWidget.customContextMenuRequested.connect(self.do_list_widget_custom_context_menu_requested)

    # ToolButton关联Action
    def __set_actions_for_button(self):
        self.ui.btnList_Ini.setDefaultAction(self.ui.actList_Ini)
        self.ui.btnList_Clear.setDefaultAction(self.ui.actList_Clear)

        self.ui.btnList_Insert.setDefaultAction(self.ui.actList_Insert)
        self.ui.btnList_Append.setDefaultAction(self.ui.actList_Append)
        self.ui.btnList_Delete.setDefaultAction(self.ui.actList_Delete)

        self.ui.btnSel_ALL.setDefaultAction(self.ui.actSel_ALL)
        self.ui.btnSel_None.setDefaultAction(self.ui.actSel_None)
        self.ui.btnSel_Invs.setDefaultAction(self.ui.actSel_Invs)

        self.ui.btnList_Ini.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnList_Clear.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnList_Insert.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnList_Append.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnList_Delete.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

    # 创建ToolButton按钮的下拉菜单
    def __create_selection_pop_menu(self):
        menuSelection = QMenu(self)  # 下拉菜单
        menuSelection.addAction(self.ui.actSel_ALL)
        menuSelection.addAction(self.ui.actSel_None)
        menuSelection.addAction(self.ui.actSel_Invs)

        # listWidget上方的btnSelectItem按钮
        self.ui.btnSelectItem.setPopupMode(QToolButton.MenuButtonPopup)
        self.ui.btnSelectItem.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnSelectItem.setDefaultAction(self.ui.actSelPopMenu)
        self.ui.btnSelectItem.setMenu(menuSelection)  # 设置下拉菜单

        # 工具栏上的下拉式菜单按钮
        toolBtn = QToolButton(self)
        toolBtn.setPopupMode(QToolButton.InstantPopup)
        toolBtn.setDefaultAction(self.ui.actSelPopMenu)
        toolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBtn.setMenu(menuSelection)  # 设置下拉菜单
        self.ui.toolBar.addWidget(toolBtn)

        # 工具栏添加分隔条和"退出"按钮
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.ui.actQuit)

    # 初始化列表
    def do_act_list_ini_triggered(self):
        editable = self.ui.checkBox.isChecked()
        if editable:
            Flag = self.__FlagEditable  # 可编辑
        else:
            Flag = self.__FlagNotEditable  # 不可编辑
        self.ui.listWidget.clear()  # 清除列表
        for i in range(10):
            itemStr = "Item %d" % i
            aItem = QListWidgetItem()
            aItem.setText(itemStr)
            aItem.setCheckState(Qt.Checked)
            aItem.setFlags(Flag)  # 项的Flag
            self.ui.listWidget.addItem(aItem)

    # 插入一项
    def do_act_list_insert_triggered(self):
        editable = self.ui.checkBox.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        aItem = QListWidgetItem()
        aItem.setText("Insert Item")
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        curRow = self.ui.listWidget.currentRow()  # 当前行
        self.ui.listWidget.insertItem(curRow, aItem)

    # 添加一项
    def do_act_list_append_triggered(self):
        editable = self.ui.checkBox.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        aItem = QListWidgetItem()
        aItem.setText("Append Item")
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        self.ui.listWidget.addItem(aItem)

    # 删除当前项
    def do_act_list_delete_triggered(self):
        row = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(row)  # 移出当前项，Python自动删除

    # 清空列表
    def do_act_list_clear_triggered(self):
        self.ui.listWidget.clear()

    # 全选
    def do_act_sel_all_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Checked)

    # 全不选
    def do_act_sel_none_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Unchecked)

    # 反选
    def do_act_sel_invs_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            if aItem.checkState() != Qt.Checked:
                aItem.setCheckState(Qt.Checked)
            else:
                aItem.setCheckState(Qt.Unchecked)

    # 当选择项发生变化时
    def do_list_widget_current_item_changed(self, current, previous):
        strInfo = ""
        if current is not None:
            if previous is None:
                strInfo = "当前：" + current.text()
            else:
                strInfo = "前一项：" + previous.text() + "；当前项：" + current.text()
        self.ui.lineEdit.setText(strInfo)

    # 右键快捷菜单
    def do_list_widget_custom_context_menu_requested(self, pos):
        print("aaa")
        menuList = QMenu(self)  # 创建菜单
        menuList.addAction(self.ui.actList_Ini)
        menuList.addAction(self.ui.actList_Clear)
        menuList.addAction(self.ui.actList_Insert)
        menuList.addAction(self.ui.actList_Append)
        menuList.addAction(self.ui.actList_Delete)
        menuList.addSeparator()
        menuList.addAction(self.ui.actSel_ALL)
        menuList.addAction(self.ui.actSel_None)
        menuList.addAction(self.ui.actSel_Invs)
        menuList.exec(QCursor.pos())  # 显示菜单


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
