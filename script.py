# -*- coding: utf-8 -*-
"""
Created on Thu May  6 18:44:01 2021

@author: DIAMO
"""
import time
import pyautogui
def manualLeftClick2(x,y):
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
phaselist=['./playerPhase.png','./petPhase.png']
monsterlist=['./greenDolf.png','./greenDolf2.png','./redflight.png','./redflight.png']
while(True):
    for p in phaselist:
        if pyautogui.locateCenterOnScreen(p) is not None:
            print('戰鬥中',p)
            for p in monsterlist:
                if pyautogui.locateCenterOnScreen(p) is not None:
                    print('找到目標',p)
                    obj=manualLeftClick2(obj.x,obj.y)
                    break
        
    time.sleep(0.5)
    