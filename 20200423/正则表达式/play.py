#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/23 14:45
@Desc    :
================================================="""

import re


def notes():
    print(
        """
        匹配单个字符：
        .   匹配任意字符(除了\n) 备注：如果想要匹配到.的话，那么用\.可以匹配
        []  匹配[]中列举的数据
        \d  匹配数字0-9
        \D  匹配非数字
        \s  匹配空白：空格 tab
        \S  非空白
        \w  匹配单词字符 a-z A-Z 0-9 _
        \W  匹配非单词字符
        
        匹配多个字符：
        *       匹配前面字符出现0次或者无数次
        +       匹配前面字符出现1次或者无数次 至少有一次
        ?       匹配前面字符出现1次或者0次 至多有一次
        {n}     匹配前面出现的字符n次
        {m, n}  匹配前面出现的字符m次到n次，尽可能多匹配
        
        匹配开头 结尾
        ^   匹配字符串开头
        $   匹配字符串结尾
        """
          )


# 展示匹配结果，打印的是匹配到的字符或者None
def show_result_match(res, order):
    if res is None:
        print(str(order) + ". " + "匹配失败哦。。。")
    else:
        result = res.group()
        print(str(order) + ". ", end="")
        print(result)


# 匹配单个字符，从第一个字符开始匹配
def one_test_match():
    # 匹配第一个字符
    str1 = "3123452236712389"
    res = re.match(".", str1)
    show_result_match(res, 1)
    res = re.match("[1,2,3]", str1)
    show_result_match(res, 2)
    res = re.match("\d", str1)
    show_result_match(res, 3)
    res = re.match("\D", str1)
    show_result_match(res, 4)
    res = re.match("\s", str1)
    show_result_match(res, 5)
    res = re.match("\S", str1)
    show_result_match(res, 6)
    res = re.match("\w", str1)
    show_result_match(res, 7)
    res = re.match("\W", str1)
    show_result_match(res, 8)


# 匹配多个字符，从第一个字符开始匹配
def more_test_match():
    """
    cmp = re.compile(str1)
    res = cmp.match(str2)
    等价于
    res = re.match(str1, str2)

    """
    str2 = "1234567890m"
    res = re.match("\d*", str2)
    show_result_match(res, 1)
    res = re.match("\d+", str2)
    show_result_match(res, 2)
    res = re.match("\d?", str2)
    show_result_match(res, 3)
    res = re.match("\d{10}", str2)
    show_result_match(res, 4)
    res = re.match("\d{6,11}", str2)
    show_result_match(res, 5)

    # 开头 结尾
    res = re.match("^s\d", str2)
    show_result_match(res, 6)
    res = re.match("^[a-z, A-Z]\d+", str2)
    show_result_match(res, 7)
    res = re.match("^[a-z, A-Z]\d+m$", str2)
    show_result_match(res, 8)


# 找出所有符合匹配条件的值，返回的是一个列表
def more_test_findall():
    str2 = "a123b456c123d345"
    res = re.findall("\d+", str2)
    print(res)


# 扫描整个string并返回第一个匹配对象，如果没有匹配对象，返回None
def more_test_search():
    str2 = "a123b456c123d345"
    res = re.search("\d+", str2)
    cmp = re.compile("\d+")
    # 第二个参数给出了字符串开始搜索的位置索引，默认是0，5代表从第5个字符开始搜索
    # 第三个参数限定了字符串搜索的结束，7表示搜索到第7个字符结束
    res1 = cmp.search(str2, 5, 7)
    print(res[0])
    print(res1[0])


def more_test_finditer():
    text = "He was carefully disguised but captured quickly by police."
    for m in re.finditer(r"\w+ly", text):
        print("%02d-%02d: %s" % (m.start(), m.end(), m.group(0)))


def main():
    more_test_finditer()
    # more_test_search()
    # more_test_findall()
    # more_test_match()
    # one_test()


if __name__ == '__main__':
    main()
