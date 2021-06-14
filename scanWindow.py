# -*- coding: utf-8 -*-
"""
Created on Thu May  6 18:21:27 2021

@author: DIAMO
"""


import pyautogui
import time
def manualLeftClick2(x,y):
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
l=[]

# for 
while(True):
    p=pyautogui.position()
    l.append([p.x,p.y])
    print(pyautogui.position())
    xx=pyautogui.position().x
    yy=pyautogui.position().y
    ans=yy-510/640*(xx)
    if ans>0:
        print(ans,True)
    else:
        print(ans,False)
        

    time.sleep(0.2)
    
    
    

