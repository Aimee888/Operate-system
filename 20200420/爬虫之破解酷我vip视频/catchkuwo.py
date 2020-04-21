#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> catchkuwo.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/20 20:22
@Desc    :
================================================="""

"""
抓取 酷我vip音乐
基本流程：
    请求网页：requests, selenium
    解析数据：正则, beautifulsoup, pyquery
    存储数据：mysql
    
反爬机制：
    1. Headers
    2. IP代理：免费 付费 安全
    3. UA
    4. cookie
    5. Ajax
"""
import requests  # 请求
import os


def create_folder(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)


# 获取一首歌的url
def get_one_song_url(rid):
    # 点开一首免费歌曲，找到url格式url?format，点开找到头信息
    url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1587429921873&reqId=617f0321-8369-11ea-80b3-bbd056ce88a1".format(rid)
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


def song_downlod(path, song_url, song_name):
    data = requests.get(song_url).content
    with open(path + "/" + song_name + ".mp3", "wb") as f:
        print("正在下载{}".format(song_name))
        f.write(data)
    print(song_name + " 成功下载到" + path)


def get_kuwo_songs(key, page=1):
    # 右键检查-->network-->在Name找到searchMusicBykeyWord?点开，在右侧可以看到请求头和url信息
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        'Referer': "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
        'csrf': "T3X85TXE58",
        'Cookie': "_ga=GA1.2.1300124849.1587384804; _gid=GA1.2.1970714185.1587384804; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1587384804,1587386216,1587427651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1587427651; kw_token=T3X85TXE58"
    }
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}".format(key, page)
    html = requests.get(url, headers=headers).json()
    data = html["data"]["list"]
    for dic_songs_info in data:
        song_rid = dic_songs_info["rid"]
        song_name = dic_songs_info["name"]
        singer_name = dic_songs_info["artist"]
        path_singer = "./酷我音乐/" + singer_name
        create_folder(path_singer)
        song_url = get_one_song_url(song_rid)
        song_downlod(path_singer, song_url, song_name)


if __name__ == '__main__':
    searchinfo = input("请输入搜索内容（歌手/歌曲）：")

    # 不输入整数会报错，可以添加处理机制
    number = int(input("你要获取的页数："))
    # url地址
    for i in range(1, number + 1):
        get_kuwo_songs(searchinfo, i)



