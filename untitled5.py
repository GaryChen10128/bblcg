# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:21:42 2021

@author: User
"""

import numpy as np
import cv2
import pyautogui
from PIL import ImageGrab
first_frame = None 
region2=(pyautogui.size().width/2,0, pyautogui.size().width/2, pyautogui.size().height)
region1=(0,0, pyautogui.size().width/2, pyautogui.size().height)

def process(img):

    # convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, bw_copy = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # bilateral filter
    # blur = cv2.bilateralFilter(gray, 5, 75, 75)
    blur=gray
    # cv2.imshow('blur', blur)
    
    # morphological gradient calculation
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # grad = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
    grad=gray
    
    # cv2.imshow('gradient', grad)
    # grad=gray
    # binarization
    # _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # cv2.imshow('otsu', bw)
    
    # closing
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))
    # closed = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('closed', closed)
    
    closed=gray
    
    # finding contours
    contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    
    
    mask = np.zeros(closed.shape, dtype=np.uint8)
    mask1 = np.zeros(bw_copy.shape, dtype=np.uint8)
    wb_copy = cv2.bitwise_not(bw_copy)
    new_bw = np.zeros(bw_copy.shape, dtype=np.uint8)

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

            bw_temp = cv2.bitwise_and(mask1[y:y + h, x:x + w],bw_copy[y:y + h, x:x + w])
            wb_temp = cv2.bitwise_and(mask1[y:y + h, x:x + w],wb_copy[y:y + h, x:x + w])

            bw_count = cv2.countNonZero(bw_temp)
            wb_count = cv2.countNonZero(wb_temp)

            if bw_count > wb_count:
                new_bw[y:y + h, x:x + w]=np.copy(bw_copy[y:y + h, x:x + w])
            else:
                new_bw[y:y + h, x:x + w]=np.copy(wb_copy[y:y + h, x:x + w])

    
    
    
    
    
    
    
    
    # mask = np.zeros(closed.shape, dtype=np.uint8)
    # mask1 = np.zeros(bw_copy.shape, dtype=np.uint8)
    
    # for idx in range(len(contours)):
    #    x, y, w, h = cv2.boundingRect(contours[idx])
    #    mask[y:y + h, x:x + w] = 0
    #    area = cv2.contourArea(contours[idx])
    #    aspect_ratio = float(w) / h
    #    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    #    r = float(cv2.countNonZero(mask[y:y + h, x:x + w])) / (w * h)
    
    #    # identify region of interest
    #    if r > 0.34 and 0.52 < aspect_ratio < 13 and area > 145.0:
    #        cv2.drawContours(mask1, [contours[idx]], -1, (255, 255, 255), -1)
    
    img = cv2.bitwise_and(bw_copy, mask1)
    
    
    
    
    
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    # lower_white = np.array([0,0,0], dtype=np.uint8)
    # upper_white = np.array([0,0,255], dtype=np.uint8)

    # # Threshold the HSV image to get only white colors
    # mask = cv2.inRange(hsv, lower_white, upper_white)
    # # Bitwise-AND mask and original image
    # img = cv2.bitwise_and(img,img, mask= mask)
    
    
    # img = np.where(img == 255, 0, 255)
    
    
    
    
    
    
    img=cv2.subtract(255, img) 
    #--------------------------------------------------
    # threshold the image
    _, bw = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # get horizontal mask of large size since text are horizontal components
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    
    # find all the contours
    # _, contours, hierarchy,=cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy,=cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rec=[]
    #Segment the text lines
    for idx in range(len(contours)):
        
        x, y, w, h = cv2.boundingRect(contours[idx])
        if x<pyautogui.size().width/4:
            cv2.rectangle(img, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
            rec.append([x+w/2,y+h/2])
    #--------------------------------------------------
    
    # cv2.imshow('result', img)
    
    # print(img_no + " Done")
    # cv2.waitKey()
    return img,rec
first=True
firstImg=None
while True:
    img = ImageGrab.grab(bbox=(0, 0, 1000, 1100)) #x, y, w, h
    
    img_np = np.array(img)
    if first:
        firstImg=img_np
        first=False
    if firstImg is not None:
        img=img-firstImg
        
    img,coordinate=process(img)
    # print(len(coordinate))


    cv2.imshow("frame", img)
    
    
    if cv2.waitKey(1) & 0Xff == ord('q'):
    # pass
        break
    
cv2.destroyAllWindows()