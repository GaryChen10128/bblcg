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

class Coordinator(object):
    def __init__(self,region):
        # self.firstImage=img
        self.region=region
        pass
    def imputBaseline(self,img):
        self.firstImage=img
    def process(self,img):
        img=img-self.firstImage
        # convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw_copy = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        blur=gray
        grad=gray
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
    
    
        img = cv2.bitwise_and(bw_copy, mask1)
        
        
        img=cv2.subtract(255, img) 
        #--------------------------------------------------
        # threshold the image
        _, bw = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
        
        contours, hierarchy,=cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        rec=[]
        #Segment the text lines
        for idx in range(len(contours)):
        
            xx, yy, ww, hh = cv2.boundingRect(contours[idx])
            # if self.refion==1:    
            #     y=510/640*x
            # else:
            #     y=510/640*(x-640)
            ans=False
            if self.region==1:
                if yy-510/640*x<0:
                    ans=True
                else:
                    ans=False
            else:
                if yy-510/640*(x-640)<0:
                    ans=True
                else:
                    ans=False
            if xx<620:
            #     print(xx,yy)
            # if ans:
                cv2.rectangle(img, (xx, yy), (xx+ww-1, yy+hh-1), (0, 255, 0), 2)
                rec.append([xx+ww/2,yy+hh/2])
        #--------------------------------------------------
    
        # cv2.waitKey()
        return img,rec

# first=True
# cor=Coordinator(1)
# while True:
#     img = ImageGrab.grab(bbox=(0, 0, 1000, 1100)) #x, y, w, h
#     img_np = np.array(img)
#     if first:
#         first=False
#         cor.imputBaseline(img_np)
#     else:
#         img,coordinate=cor.process(img_np)
#         print(len(coordinate))
#         cv2.imshow("frame", img)
#         if cv2.waitKey(1) & 0Xff == ord('q'):
#         # pass
#             break
    
# cv2.destroyAllWindows()