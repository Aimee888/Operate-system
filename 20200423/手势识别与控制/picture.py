#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate-system -> picture.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/23 10:01
@Desc    :
================================================="""
import cv2
import numpy as np
import fourierDescriptor as fd


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


def binaryMask(img_finger, x0, y0):
    cv2.imshow("img_finger", img_finger)  # 显示手势框图
    res = skinMask(img_finger)  # 进行肤色检测
    # cv2.imshow("res", res)  # 显示肤色检测后的图像

    # 形态学处理
    kernel = np.ones((3, 3), np.uint8)  # 设置卷积核
    erosion = cv2.erode(res, kernel)  # 腐蚀操作
    # cv2.imshow("erosion", erosion)
    res = cv2.dilate(erosion, kernel)  # 膨胀操作
    # cv2.imshow("dilation", res)

    # 轮廓提取
    # gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # dst = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
    # Laplacian = cv2.convertScaleAbs(dst)
    # ret = get_outline(Laplacian, dst)
    # cv2.imshow("ret", ret)
    ret, fourier_result = fd.fourierDesciptor(res)
    cv2.imshow("ret", ret)
    return res


# 肤色检测
def skinMask(img_finger):
    YCrCb = cv2.cvtColor(img_finger, cv2.COLOR_BGR2YCR_CB)  # 转换至YCrCb空间
    (y, cr, cb) = cv2.split(YCrCb)  # 拆分出Y，Cr, Cb值
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    res = cv2.bitwise_and(img_finger, img_finger, mask=skin)
    return res