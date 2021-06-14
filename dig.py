# -*- coding: utf-8 -*-
"""
Created on Fri May  7 02:32:34 2021

@author: DIAMO
"""

import pyautogui
import time
region2=(655,0, 1279, 598)
import time
def manualLeftClick2(x,y):
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
while(True):
    white=pyautogui.locateCenterOnScreen('./white.png')
    
    if white is not None:
        # manualLeftClick2(white.x,white.y)
        print('受傷了')
        skill=pyautogui.locateCenterOnScreen('./skill.png')
        if skill is not None:
            pyautogui.leftClick(skill.x, skill.y)
            cure=pyautogui.locateCenterOnScreen('./cure.png')
            if cure is not None:
                pyautogui.leftClick(cure.x, cure.y)
                time.sleep(1)
                pyautogui.leftClick(cure.x, cure.y)
                # pyautogui.leftClick(cure.x, cure.y)

                while(True):
                    me=pyautogui.locateCenterOnScreen('./me.png')
                    if me is not None:
                        pyautogui.leftClick(me.x, me.y)
                        time.sleep(1)
                        curetarget=pyautogui.locateCenterOnScreen('./curetarget.png')
                        if curetarget is not None:
                            pyautogui.leftClick(curetarget.x, curetarget.y)
                            break
                        
                            
                    time.sleep(1)
                    

        else:
            skill2=pyautogui.locateCenterOnScreen('./skill2.png')
            if skill2 is not None:
                pyautogui.leftClick(skill2.x, skill2.y)
                pyautogui.dragTo(0, 0, button='left')
            # pass
        # break
    
        # if target1 is not None:    
        #     manualLeftClick2(target1.x,target1.y)
        # if target2 is not None:    
        #     manualLeftClick2(target2.x,target2.y)
    time.sleep(1)
