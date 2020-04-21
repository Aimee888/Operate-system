#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> catchkuwo_name.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/21 9:24
@Desc    :
================================================="""

import requests


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


if __name__ == '__main__':
    song_name = input("请输入歌曲名：")
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30".format(song_name)
    headers = {
        'Cookie': "_ga=GA1.2.1300124849.1587384804; _gid=GA1.2.1970714185.1587384804; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1587386216,1587427651,1587429757,1587432231; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1587432231; kw_token=R5PHBZIZL1",
        'csrf': "R5PHBZIZL1",
        'Referer': "http://www.kuwo.cn/search/list?key=%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    }
    html = requests.get(url, headers=headers).json()
    data = html["data"]["list"]
    singer_list = data[0]
    print(singer_list)
    # for singer_list in data:
    music_name = singer_list["name"]
    music_rid = singer_list["rid"]
    singer_name = singer_list["artist"]
    song_url = get_one_song_url(music_rid)
    print(song_url)
    # song_downlod("./酷我音乐/周杰伦", song_url, music_name)
