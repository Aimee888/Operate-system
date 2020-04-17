#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> ReadAndWriteFile.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/14 17:26
@Desc    :
================================================="""


def txt_read():
    # 方法一：
    # 优点：一次性独读出文件放在一个大字符串中，速度最快
    # 缺点：文件过大的时候，占用内存会过大
    # 中文的话，需要添加encoding="utf-8"
    f = open("test1.txt", "r")
    data = f.read()
    print(data)
    f.close()

    # 方法二
    # 优点：占用内存小，逐行读取
    # 缺点：由于是逐行读取，速度比较慢
    # f = open("test1.txt", "r")
    # # 读取一行文本
    # line = f.readline()
    # print(line)
    # f.close()

    # 方法三
    # 优点：一次性读取文本内容，速度比较快
    # 缺点：随着文本的增大，占用内存会越来越多
    # f = open("test1.txt", "r")
    # # 读取文本
    # data = f.readlines()
    # print(data)
    # f.close()


def txt_write():
    lines = ["Good evening! What can I do for you?\n",
             "I'm looking for a pair of black shoes.\n"]
    with open("wtest.txt", 'w') as f:
        # f.write("What a nice day today!")
        f.writelines(lines)


def ini_read():
    import configparser
    conf = configparser.ConfigParser()
    conf.read("test2.ini")
    # 获取section
    sections = conf.sections()
    print(sections)
    # 获取某个section下所有的key
    options = conf.options('ITEMS')
    print(options)
    # 获取某个section下所有的键值对
    items = conf.items('ITEMS')
    print(items)
    # 获取值
    value = conf.get('ITEMS', 'item1')
    print(value)


def ini_write():
    import configparser
    conf = configparser.ConfigParser()
    conf.add_section("Config")
    conf.set("Config", "ip", "10.203.70.170")
    conf.set("Config", "port", "8080")
    conf.write(open("test3.ini", "w"))


if __name__ == '__main__':
    # txt_read()
    # txt_write()
    # ini_read()
    ini_write()
