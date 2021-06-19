# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:13:55 2021

@author: DIAMO
"""

import cv2
import numpy as np


def process(img):
    # read image
    img_no = str(img)
    rgb = cv2.imread(img_no + '.jpg')
    # cv2.imshow('original', rgb)
    
    # convert image to grayscale
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    
    _, bw_copy = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # bilateral filter
    blur = cv2.bilateralFilter(gray, 5, 75, 75)
    # cv2.imshow('blur', blur)
    
    # morphological gradient calculation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
    # cv2.imshow('gradient', grad)
    
    # binarization
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # cv2.imshow('otsu', bw)
    
    # closing
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))
    closed = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('closed', closed)
    
    # finding contours
    contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    mask = np.zeros(closed.shape, dtype=np.uint8)
    mask1 = np.zeros(bw_copy.shape, dtype=np.uint8)
    
    for idx in range(len(contours)):
       x, y, w, h = cv2.boundingRect(contours[idx])
       mask[y:y + h, x:x + w] = 0
       area = cv2.contourArea(contours[idx])
       aspect_ratio = float(w) / h
       cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
       r = float(cv2.countNonZero(mask[y:y + h, x:x + w])) / (w * h)
    
       # identify region of interest
       if r > 0.34 and 0.52 < aspect_ratio < 13 and area > 145.0:
           cv2.drawContours(mask1, [contours[idx]], -1, (255, 255, 255), -1)
    
    result = cv2.bitwise_and(bw_copy, mask1)
    cv2.imshow('result', result)
    
    print(img_no + " Done")
    cv2.waitKey()
