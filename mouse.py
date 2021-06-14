# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:20:39 2021

@author: DIAMO
"""
import pyautogui
import time

f = open('./x.txt', 'r')
x=[]
for line in f.readlines():
    x.append(int(line))
    # print(line)
f.close
f = open('./y.txt', 'r')
y=[]
for line in f.readlines():
    y.append(int(line))
    # print(line)
f.close
axis=[]
for i in range(len(x)):
    print(i)
    axis.append([x[i],y[i]])


def manualLeftClick2(x,y):
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    pyautogui.leftClick(x=x, y=y)
    # pyautogui.leftClick(x=x, y=y)


print(pyautogui.position())
# num_seconds = 0.1
# x,y=952,238
# x,y=825,220
x=pyautogui.position().x
y=pyautogui.position().y
region1=(0,0,655,598)
region2=(655,0, 1279, 598)
region3=(653,0, 1279, 598)
# pyautogui.moveTo(x, y, duration=num_seconds)
# icon1=pyautogui.locateCenterOnScreen('./icon.png',region=region1)
# icon2=pyautogui.locateCenterOnScreen('./icon.png',region=region3)
# offset=[icon2.x-icon1.x,icon2.y-icon1.y]
# for aii in axis:
#     manualLeftClick2(aii[0]-offset[0],aii[1]-offset[1])


bubble=pyautogui.locateCenterOnScreen('./shoot.png',region=region1)
manualLeftClick2(bubble.x,bubble.y)
# target1=pyautogui.locateCenterOnScreen('./mantis2.png',region=region1)
# target2=pyautogui.locateCenterOnScreen('./mouse2.png',region=region1)
# while(True):
#     if target1 is not None or target2 is not None:
#         if target1 is not None:    
#             manualLeftClick2(target1.x,target1.y)
#             break
#         if target2 is not None:    
#             manualLeftClick2(target2.x,target2.y)
#             break
#     time.sleep(0.2)
for aii in axis:
    manualLeftClick2(aii[0]-580,aii[1])

bubble=pyautogui.locateCenterOnScreen('./shoot.png',region=region2)
manualLeftClick2(bubble.x,bubble.y)

for aii in axis:
    manualLeftClick2(aii[0],aii[1])



# target1=pyautogui.locateCenterOnScreen('./mantis2.png',region=region2)
# target2=pyautogui.locateCenterOnScreen('./mouse2.png',region=region2)
# while(True):
#     if target1 is not None or target2 is not None:
#         if target1 is not None:    
#             manualLeftClick2(target1.x,target1.y)
#         if target2 is not None:    
#             manualLeftClick2(target2.x,target2.y)
#     time.sleep(0.2)

