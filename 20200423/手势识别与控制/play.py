#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/23 8:34
@Desc    :
================================================="""

import cv2
import numpy as np


# 肤色检测
def skinMask(img_finger):
    YCrCb = cv2.cvtColor(img_finger, cv2.COLOR_BGR2YCR_CB)  # 转换至YCrCb空间
    (y, cr, cb) = cv2.split(YCrCb)  # 拆分出Y，Cr, Cb值
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    res = cv2.bitwise_and(img_finger, img_finger, mask=skin)
    return res


def get_outline(img_outline, dst):
    # 寻找轮廓
    h = cv2.findContours(img_outline, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    coutour = h[0]
    # 已轮廓区域面积进行排序
    coutour = sorted(coutour, key=cv2.contourArea, reverse=True)
    # # 创建白色幕布
    # bg = np.ones(dst.shape, np.uint8)*255
    # 创建黑色幕布
    bg = np.ones(dst.shape, np.uint8)
    # 绘制黑色轮廓
    ret = cv2.drawContours(bg, coutour[0], -1, (255, 255, 255), 3)
    return ret


def main():
    while True:
        img = "./image/finger1.jpg"
        imgUMat = cv2.imread(img)
        res = skinMask(imgUMat)  # 进行肤色检测
        cv2.imshow("0", imgUMat)

        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        dst = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
        Laplacian = cv2.convertScaleAbs(dst)

        # 轮廓处理
        coutour = get_outline(Laplacian, dst)
        cv2.imshow("2", coutour)

        key = cv2.waitKey(50) & 0xFF
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
