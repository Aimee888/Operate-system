#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> myMainWindow_kuwo_download.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/21 10:26
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QLineEdit, QFileDialog
from enum import Enum
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from ui_kuwo import Ui_MainWindow
import requests


# 节点类型的枚举类型
class TreeItemType(Enum):
    itTopItem = 1001  # 顶层节点
    itGroupItem = 1002  # 分组节点
    itImageItem = 1003  # 图片文件节点


class TreeColNum(Enum):  # 目录树的列号的枚举类型
    col_order = 0  # 序号列
    col_song_name = 1   # 歌曲名列
    col_singer_name = 2  # 歌手列
    col_singer_album = 3  # 专辑列
    col_song_time = 4  # 时长列
    col_song_rid = 5  # rid


class SongDownload(QThread):
    label_str = pyqtSignal(str)

    def __init__(self, path, song_url, song_name):
        super(SongDownload, self).__init__()
        self.__path = path
        self.__url = song_url
        self.__songname = song_name

    def run(self):
        self.label_str.emit("正在请求响应...请耐心等待")
        # self.label_str.emit("正在下载{}".format(self.__songname))
        # print("正在下载{}".format(self.__songname))
        data = requests.get(self.__url).content

        with open(self.__path + "/" + self.__songname + ".mp3", "wb") as f:
            f.write(data)
        self.label_str.emit(self.__songname + " 成功下载到" + self.__path)
        print(self.__songname + " 成功下载到" + self.__path)


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread = None

        self.itemFlags = Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate

        self.ui.lineEdit.addAction(self.ui.actSong_Search, QLineEdit.TrailingPosition)

        self.ui.treeWidget.hideColumn(5)

        # 当点击搜索时
        self.ui.actSong_Search.triggered.connect(self.do_act_song_search_triggered)
        # 全选
        self.ui.btnSel_ALL.clicked.connect(self.do_btn_sel_all_clicked)
        # 全不选
        self.ui.btnSel_None.clicked.connect(self.do_btn_sel_none_clicked)
        # 反选
        self.ui.btnSel_Invs.clicked.connect(self.do_btn_sel_invs_clicked)
        # 当点击下载歌曲时
        self.ui.actSong_Download.triggered.connect(self.do_act_song_download_triggered)

    # 全选
    def do_btn_sel_all_clicked(self):
        for i in range(self.ui.treeWidget.topLevelItemCount()):
            aItem = self.ui.treeWidget.topLevelItem(i)
            aItem.setCheckState(TreeColNum.col_order.value, Qt.Checked)

    # 全不选
    def do_btn_sel_none_clicked(self):
        for i in range(self.ui.treeWidget.topLevelItemCount()):
            aItem = self.ui.treeWidget.topLevelItem(i)
            aItem.setCheckState(TreeColNum.col_order.value, Qt.Unchecked)

    # 反选
    def do_btn_sel_invs_clicked(self):
        for i in range(self.ui.treeWidget.topLevelItemCount()):
            aItem = self.ui.treeWidget.topLevelItem(i)
            if aItem.checkState(TreeColNum.col_order.value) != Qt.Checked:
                aItem.setCheckState(TreeColNum.col_order.value, Qt.Checked)
            else:
                aItem.setCheckState(TreeColNum.col_order.value, Qt.Unchecked)

    # 当点击搜索按钮时
    def do_act_song_search_triggered(self):
        # 获取歌手名或者歌曲名
        search_text = self.ui.lineEdit.text()
        self.ui.treeWidget.clear()
        self.get_kuwo_songs(search_text)

    # 搜索之后列出歌单
    def show_songs_tree(self, order, song_name, singer_name, singer_album, song_time, song_rid):
        # 创建节点
        item = QTreeWidgetItem(TreeItemType.itTopItem.value)
        item.setText(TreeColNum.col_order.value, str(order+1))
        item.setText(TreeColNum.col_song_name.value, song_name)
        item.setText(TreeColNum.col_singer_name.value, singer_name)
        item.setText(TreeColNum.col_singer_album.value, singer_album)
        item.setText(TreeColNum.col_song_time.value, song_time)
        item.setText(TreeColNum.col_song_rid.value, str(song_rid))

        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.col_order.value, Qt.Checked)
        item.setData(TreeColNum.col_order.value, Qt.UserRole, "")

        # 设置文字居中
        item.setTextAlignment(TreeColNum.col_order.value, Qt.AlignCenter)
        item.setTextAlignment(TreeColNum.col_song_name.value, Qt.AlignCenter)
        item.setTextAlignment(TreeColNum.col_singer_name.value, Qt.AlignCenter)
        item.setTextAlignment(TreeColNum.col_singer_album.value, Qt.AlignCenter)
        item.setTextAlignment(TreeColNum.col_song_time.value, Qt.AlignCenter)
        item.setTextAlignment(TreeColNum.col_song_rid.value, Qt.AlignCenter)
        self.ui.treeWidget.addTopLevelItem(item)

    # 获取歌曲，默认5页
    def get_kuwo_songs(self, key, page=1):
        # 右键检查-->network-->在Name找到searchMusicBykeyWord?点开，在右侧可以看到请求头和url信息
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            'Referer': "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
            'csrf': "T3X85TXE58",
            'Cookie': "_ga=GA1.2.1300124849.1587384804; _gid=GA1.2.1970714185.1587384804; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1587384804,1587386216,1587427651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1587427651; kw_token=T3X85TXE58"
        }
        order = 0
        for i in range(1, page + 1):
            url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}".format(key, i)
            html = requests.get(url, headers=headers).json()
            data = html["data"]["list"]
            for dic_songs_info in data:
                song_rid = dic_songs_info["rid"]
                song_name = dic_songs_info["name"]
                singer_name = dic_songs_info["artist"]
                song_time = dic_songs_info["songTimeMinutes"]
                singer_album = dic_songs_info["album"]
                self.show_songs_tree(order, song_name, singer_name, singer_album, song_time, song_rid)  # 显示到窗口
                order = order + 1

    def start_thread(self, path_singer, song_url, song_name):
        # 创建线程
        self.thread = SongDownload(path_singer, song_url, song_name)
        # 连接信号
        self.thread.label_str[str].connect(self.do_label_change)
        # 开启线程
        self.thread.start()

    # 当点击下载
    def do_act_song_download_triggered(self):
        for i in range(self.ui.treeWidget.topLevelItemCount()):
            aItem = self.ui.treeWidget.topLevelItem(i)
            if aItem.checkState(TreeColNum.col_order.value) != Qt.Checked:
                pass
            else:
                song_name = aItem.text(1)
                song_rid = int(aItem.text(5))
                song_url = self.get_one_song_url(song_rid)
                dirStr = QFileDialog.getExistingDirectory()  # 选择目录
                self.start_thread(dirStr, song_url, song_name)

    # 获取一首歌的url
    def get_one_song_url(self, rid):
        # 点开一首免费歌曲，找到url格式url?format，点开找到头信息
        url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1587429921873&reqId=617f0321-8369-11ea-80b3-bbd056ce88a1".format(
            rid)
        headers = {
            'Cookie': "_ga=GA1.2.1300124849.1587384804; _gid=GA1.2.1970714185.1587384804; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1587384804,1587386216,1587427651,1587429757; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1587429793; _gat=1; kw_token=PRLZKVXE32C",
            'Referer': "http://www.kuwo.cn/search/list?key=%E5%8D%8E%E6%99%A8%E5%AE%87",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            'csrf': "PRLZKVXE32C"
        }
        data = requests.get(url, headers=headers).json()
        # {'code': 200, 'msg': 'success', 'url': 'https://win-web-ra01-sycdn.kuwo.cn/e9cbd04a0602f9f82c40e0f1800fa696/5e9e44a1/resource/n3/128/43/28/1310690697.mp3'}
        song_url = data["url"]
        return song_url

    def do_label_change(self, str_label):
        self.ui.label.setText(str_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app，用QApplication类
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
