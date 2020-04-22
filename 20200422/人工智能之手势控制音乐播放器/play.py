#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/22 14:32
@Desc    :手势控制音乐播放
================================================="""

import os
# 混频器
import pygame


def remind():
    print(
        """
        功能设置：
        1. 播放
        2. 暂停
        3. 继续播放
        4. 上一曲
        5. 下一曲
        6. 音量增加
        7. 音量减小
        8. 退出
        """
    )


if __name__ == '__main__':
    # 初始化
    pygame.mixer.init()
    # 搜索文件
    music_names = os.listdir("music")
    # 音乐序号
    music_no = 0
    # 音乐序号的范围
    music_range = range(len(music_names))
    # 音量[0, 1]
    volume = 0.2


    # 提示
    remind()
    while True:
        while True:
            command = input("请输入命令：")

            # 判断指令的合法性
            # alt+鼠标点击可以进行插入操作
            if command in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                print("接受指令", command)
                break

        # 执行任务
        if command == "1":
            # 播放
            pygame.mixer.music.load("./music/" + music_names[music_no])
            pygame.mixer.music.play()
        elif command == "2":
            # 暂停
            pygame.mixer.music.pause()
        elif command == "3":
            # 继续播放
            pygame.mixer.music.unpause()
        elif command == "4":
            # 上一曲
            music_no -= 1
            if music_no not in music_range:
                music_no = music_range[-1]
                pygame.mixer.music.load("music/" + music_names[music_no])
                pygame.mixer.music.play()
        elif command == "5":
            # 下一曲
            music_no += 1
            if music_no not in music_range:
                music_no = 0
            pygame.mixer.music.load("./music/" + music_names[music_no])
            pygame.mixer.music.play()
        elif command == "6":
            # 音量增加
            if volume <= 0.9:
                volume = round(volume + 0.1, 2)
                pygame.mixer.music.set_volume(volume)
            else:
                print("音量已经最大")
        elif command == "7":
            if volume >= 0.1:
                volume = round(volume - 0.1, 2)
                pygame.mixer.music.set_volume(volume)
            else:
                print("音量已经最小")
        elif command == "8":
            print("退出播放器")
            # os.getpid()当前程序的编号
            os.kill(os.getpid(), 9)

        print("正在播放的歌曲：", music_names[music_no])
        print("播放的音量：", volume)

