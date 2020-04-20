#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow_QtreeWidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/17 8:50
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QLabel, QFileDialog, QDockWidget
from enum import Enum
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QDir, QFileInfo
from ui_TreeWidget import Ui_MainWindow


# 节点类型的枚举类型
class TreeItemType(Enum):
    itTopItem = 1001  # 顶层节点
    itGroupItem = 1002  # 分组节点
    itImageItem = 1003  # 图片文件节点


class TreeColNum(Enum):  # 目录树的列号的枚举类型
    colItem = 0  # 分组/文件名列
    colItemType = 1  # 节点类型对


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curPixmap = QPixmap()  # 图片
        self.pixRatio = 1  # 显示比例
        #  节点标志
        self.itemFlags = Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate
        self.setCentralWidget(self.ui.scrollArea)

        self.__iniTree()

        # 添加目录节点
        self.ui.actTree_AddFolder.triggered.connect(self.do_act_tree_add_folder_triggered)
        # 添加文件节点
        self.ui.actTree_AddFiles.triggered.connect(self.do_act_tree_add_file_triggered)
        # 删除节点
        self.ui.actTree_DeleteItem.triggered.connect(self.do_act_zoom_delete_item_triggered)
        # 遍历节点
        self.ui.actTree_ScanItems.triggered.connect(self.do_act_tree_scan_item_triggered)
        # 目录树上当前节点变化时
        self.ui.treeWidget.currentItemChanged.connect(self.do_tree_widget_current_item_changed)

        # 适应高度显示图片
        self.ui.actZoomFitH.triggered.connect(self.do_act_zoom_fith_triggerd)
        # 适应宽度显示图片
        self.ui.actZoomFitW.triggered.connect(self.do_act_zoom_fitw_triggered)
        # 放大显示
        self.ui.actZoomIn.triggered.connect(self.do_act_zoom_in_triggered)
        # 缩小显示
        self.ui.actZoomOut.triggered.connect(self.do_act_zoom_out_triggered)
        # 实际大小
        self.ui.actZoomRealSize.triggered.connect(self.do_act_zoom_realsize_triggered)
        # 设置停靠区浮动性
        self.ui.actDockFloat.triggered.connect(self.do_act_dock_float_triggered)
        # 设置停靠区可见性
        self.ui.actDockVisible.triggered.connect(self.do_act_dock_visible_triggered)
        # 停靠区浮动性改变
        self.ui.dockWidget.topLevelChanged.connect(self.do_dock_widget_toplevelchanged)
        # 停靠区可见性改变
        self.ui.dockWidget.visibilityChanged.connect(self.do_dock_widget_visibilitychanged)

    def __iniTree(self):  # 初始化目录树
        self.ui.treeWidget.clear()
        icon = QIcon("./image/icon/pic.jpg")

        # 创建节点
        item = QTreeWidgetItem(TreeItemType.itTopItem.value)
        item.setIcon(TreeColNum.colItem.value, icon)
        item.setText(TreeColNum.colItem.value, "图片文件")
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)
        item.setData(TreeColNum.colItem.value, Qt.UserRole, "")
        self.ui.treeWidget.addTopLevelItem(item)

    # 添加目录节点
    def do_act_tree_add_folder_triggered(self):
        dirStr = QFileDialog.getExistingDirectory()  # 选择目录
        if dirStr == "":
            return
        parItem = self.ui.treeWidget.currentItem()  # 当前节点
        if parItem is None:
            parItem = self.ui.treeWidget.topLevelItem(0)
        icon = QIcon("./image/icon/AddFolder.jpg")
        dirObj = QDir(dirStr)  # QDir对象
        nodeText = dirObj.dirName()  # 最后一级目录的名称

        item = QTreeWidgetItem(TreeItemType.itGroupItem.value)  # 节点类型
        item.setIcon(TreeColNum.colItem.value, icon)
        item.setText(TreeColNum.colItem.value, nodeText)  # 第一列
        item.setText(TreeColNum.colItemType.value, "Group")  # 第二列
        # 设置文字居中
        item.setTextAlignment(TreeColNum.colItemType.value, Qt.AlignCenter)
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)
        item.setData(TreeColNum.colItem.value, Qt.UserRole, dirStr)
        parItem.addChild(item)
        parItem.setExpanded(True)

    # 添加文件节点
    def do_act_tree_add_file_triggered(self):
        fileList, flt = QFileDialog.getOpenFileNames(self, "选择一个或多个文件", "", "Images(*.jpg)")
        if len(fileList) < 1:
            return
        item = self.ui.treeWidget.currentItem()  # 当前节点
        if item.type() == TreeItemType.itImageItem.value:
            parItem = item.parent()  # 当前是图片节点
        else:
            parItem = item

        icon = QIcon("./image/icon/onepic.jpg")
        for i in range(len(fileList)):
            fullFileName = fileList[i]  # 带路径文件名
            fileinfo = QFileInfo(fullFileName)
            nodeText = fileinfo.fileName()  # 不带路径文件名
            item = QTreeWidgetItem(TreeItemType.itImageItem.value)  # 节点类型
            item.setIcon(TreeColNum.colItem.value, icon)  # 第一列的图标
            item.setText(TreeColNum.colItem.value, nodeText)  # 第一列的文字
            item.setText(TreeColNum.colItemType.value, "Image")  # 第二列的文字
            # 设置文字居中
            item.setTextAlignment(TreeColNum.colItemType.value, Qt.AlignCenter)
            item.setFlags(self.itemFlags)
            item.setCheckState(TreeColNum.colItem.value, Qt.Checked)
            item.setData(TreeColNum.colItem.value, Qt.UserRole, fullFileName)
            parItem.addChild(item)

        parItem.setExpanded(True)

    # 删除节点
    def do_act_zoom_delete_item_triggered(self):
        item = self.ui.treeWidget.currentItem()
        parItem = item.parent()
        parItem.removeChild(item)

    # 遍历节点
    def do_act_tree_scan_item_triggered(self):
        cout = self.ui.treeWidget.topLevelItemCount()
        for i in range(cout):
            item = self.ui.treeWidget.topLevelItem(i)
            self.__changeItemCaption(item)

    def __changeItemCaption(self, item):  # 递归调用函数，修改节点标题
        title = "*" + item.text(TreeColNum.colItem.value)
        item.setText(TreeColNum.colItem.value, title)
        if item.childCount() > 0:
            for i in range(item.childCount()):
                self.__changeItemCaption(item.child(i))

    # 当前节点发生变化时
    def do_tree_widget_current_item_changed(self, current, previous):
        if current is None:
            return
        nodeType = current.type()  # 获取节点类型
        if nodeType == TreeItemType.itTopItem.value:
            self.ui.actTree_AddFolder.setEnabled(True)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(False)
        elif nodeType == TreeItemType.itGroupItem.value:
            self.ui.actTree_AddFolder.setEnabled(True)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(True)
        elif nodeType == TreeItemType.itImageItem.value:
            self.ui.actTree_AddFolder.setEnabled(False)
            self.ui.actTree_AddFiles.setEnabled(True)
            self.ui.actTree_DeleteItem.setEnabled(True)
            self.__displayImage(current)  # 显示图片

    def __displayImage(self, item):  # 显示节点item的图片
        filename = item.data(TreeColNum.colItem.value, Qt.UserRole)
        self.ui.statusbar.showMessage(filename)  # 状态栏显示文件名
        self.curPixmap.load(filename)  # 原始图片
        self.do_act_zoom_fith_triggerd()
        self.ui.actZoomFitH.setEnabled(True)
        self.ui.actZoomFitW.setEnabled(True)
        self.ui.actZoomIn.setEnabled(True)
        self.ui.actZoomOut.setEnabled(True)
        self.ui.actZoomRealSize.setEnabled(True)

    # 适应高度显示图片
    def do_act_zoom_fith_triggerd(self):
        H = self.ui.scrollArea.height()  # 得到scrollArea的高度
        realH = self.curPixmap.height()  # 原始图片的实际高度
        self.pixRatio = float(H) / realH  # 当前显示比例，必须转换为浮点数
        pix = self.curPixmap.scaledToHeight(H - 30)  # 图片缩放到指定高度
        self.ui.LabPicture.setPixmap(pix)  # 设置Lable的PixMap

    # 适应宽度显示图片
    def do_act_zoom_fitw_triggered(self):
        W = self.ui.scrollArea.width() - 20
        realW = self.curPixmap.width()
        self.pixRatio = float(W)/realW
        pix = self.curPixmap.scaledToWidth(W-30)
        self.ui.LabPicture.setPixmap(pix)

    # 放大显示
    def do_act_zoom_in_triggered(self):
        self.pixRatio = self.pixRatio * 1.2
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.LabPicture.setPixmap(pix)

    # 缩小显示
    def do_act_zoom_out_triggered(self):
        self.pixRatio = self.pixRatio * 0.8
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.LabPicture.setPixmap(pix)

    # 实际大小
    def do_act_zoom_realsize_triggered(self):
        self.pixRatio = 1
        self.ui.LabPicture.setPixmap(self.curPixmap)

    # 设置停靠区浮动性
    @pyqtSlot(bool)
    def do_act_dock_float_triggered(self, checked):
        self.ui.dockWidget.setFloating(checked)

    # 设置停靠区可见性
    @pyqtSlot(bool)
    def do_act_dock_visible_triggered(self, checked):
        self.ui.dockWidget.setVisible(checked)

    # 停靠区浮动性改变
    @pyqtSlot(bool)
    def do_dock_widget_toplevelchanged(self, topLevel):
        self.ui.actDockFloat.setChecked(topLevel)

    # 停靠区可见性改变
    @pyqtSlot(bool)
    def do_dock_widget_visibilitychanged(self, visible):
        self.ui.actDockVisible.setChecked(visible)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
