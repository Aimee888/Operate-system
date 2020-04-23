#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> main.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/23 9:58
@Desc    :
================================================="""

import cv2
import picture as pic

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体
size = 0.5  # 设置大小

x0, y0 = 300, 100  # 设置选取位置

if __name__ == '__main__':
    while True:
        img = "./image/finger1.jpg"
        imgUMat = cv2.imread(img)
        roi = pic.binaryMask(imgUMat, x0, y0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('i'):
            y0 += 5
        elif key == ord('k'):
            y0 -= 5
        elif key == ord('l'):
            x0 += 5
        elif key == ord('j'):
            x0 -= 5
        # cv2.imshow('imgUMat', imgUMat)
    cv2.destroyAllWindows()
