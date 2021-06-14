# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:23:17 2021

@author: DIAMO
"""
from PIL import ImageGrab
from Click import Click
import cv2
import numpy as np
import pyautogui
from Coordinator import Coordinator
import time
pyautogui.size().width
region2=(pyautogui.size().width/2,0, pyautogui.size().width/2, pyautogui.size().height)
region1=(0,0, int(pyautogui.size().width/2), pyautogui.size().height)
region=[region1,region2]
import time
# lv=int(input("請輸入lv  ")) # 794
lv=5
# skill=['./shoot.png','./bubble.png']
skill=['./bubble.png']
monsterlist=['./giant.png','./giant2.png','./greendog.png','./greendog2.png','./giant3.png','./giant4.png']

if lv==9:
    lvpath=['./lv{0}.png'.format(lv),'./lv{0}.png'.format(lv-1)]
else:
    lvpath=['./lv{0}.png'.format(lv),'./lv{0}.png'.format(lv+1)]
print('lvpath',lvpath)


scanattack=Click(name='scan attack',scantime=0,
                 waitresponsetime=3,startsign=['./attack.png'],
                 endsign='reScanServer.png',region=region1,
                 clicktimes=0,scandur=0.1)
shootattack=Click(name='shoot attack',scantime=3,
                 waitresponsetime=3,startsign=skill,
                 endsign='lv1.png',region=region1,
                 clicktimes=1,scandur=0)
                 # clicktimes=1,scandur=0.3)
                 
lvattack=Click(name='lv attack',scantime=3,
                 waitresponsetime=3,startsign=lvpath,
                 endsign=None,region=region1,
                 clicktimes=1)


attacktarget=Click(name='attacktarget',scantime=0.5,
                 waitresponsetime=3,startsign=monsterlist,
                 endsign=None,region=region1,
                 clicktimes=4,scandur=0)


isPlayerPhase=Click(name='playerphase',scantime=3,
                  waitresponsetime=1,startsign=['./playerPhase.png'],
                  endsign=None,region=region1,
                  clicktimes=0,scandur=0)
# isPlayerPhase=Click(name='playerphase',scantime=2,
#                  waitresponsetime=3,startsign=['./battlepet.png'],
#                  endsign=None,region=region1,
#                  clicktimes=0,scandur=0)
isPetPhase=Click(name='playerphase',scantime=2,
                 waitresponsetime=3,startsign=['./petPhase.png'],
                 endsign=None,region=region1,
                 clicktimes=0,scandur=0)


first=True
cor=Coordinator(1)
shootattack=Click(name='shoot attack',scantime=3,
                  waitresponsetime=3,startsign=skill,
                  endsign='lv1.png',region=region1,
                  clicktimes=1,scandur=0.3)




useAlgorithm=False
while True:
    # img = ImageGrab.grab(bbox=(0, 0, 640, 510)) #x, y, w, h
    img = pyautogui.screenshot()
    img_np = np.array(img)
    if useAlgorithm:
        isPlayerPhase.exevute(region=region1)
    # if False:
        if isPlayerPhase.isScanned:
            print('success')
            # cor.imputBaseline(img_np)
            if first:
                first=False
                cor.imputBaseline(img_np)
        
            else:
                # pyautogui.moveTo(x=5,y=5)
                img_np,coordinate=cor.process(img_np)
                # cv2.imshow("frame", img_np)
                print('update')
                continue
                if len(coordinate)>0:
                    print('monster count', len(coordinate))
                    
                    # pyautogui.moveTo(x=coordinate[0][0],y=coordinate[0][1])
                    lv=len(coordinate)-3
                    if lv<1:
                        lv=1
                    if lv>9:
                        lv=5
    
                    lvpath=['./lv{0}.png'.format(lv)]
                    
                    lvpath.append(lvpath[0].replace('.png','2.png'))
                    
                    
    
                    shootattack.exevute(region=region1)
                    print('####lvpath is ',lvpath)
                    lvattack=Click(name='lv attack',scantime=3,
                       waitresponsetime=3,startsign=lvpath,
                       endsign='./choseeTarget.png',region=region1,
                       clicktimes=1)
                    lvattack.exevute(region=region1)
                    targetAttack=Click(name='target attack',scantime=0,
                       waitresponsetime=3,startsign=lvpath,
                       endsign='./petPhase.png',region=region1,
                       clicktimes=1)
                    targetAttack2=Click(name='target attack',scantime=0,
                       waitresponsetime=3,startsign=lvpath,
                       endsign='./petPhase.png',region=region1,
                       clicktimes=1,isReverse=True)
                    targetAttack.exevute(coordinate=coordinate[0])
                    targetAttack2.exevute(coordinate=coordinate[0])
                    
                    
                    # pyautogui.leftClick(x=coordinate[0][0],y=coordinate[0][1])
                    # time.sleep(0.8)
                    # pyautogui.leftClick(x=coordinate[0][0],y=coordinate[0][1])
                    # pyautogui.leftClick(x=coordinate[0][0],y=coordinate[0][1])
                else:
                    pass
                # print(len(coordinate))
                # cv2.imshow("frame", img)
                # if cv2.waitKey(1) & 0Xff == ord('q'):
                #     break
                first=True
    cv2.imshow("frame", img_np)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

# for reg in region:
#     # scanattack.exevute(region=reg)
#     shootattack.exevute(region=reg)
#     lvattack.exevute(region=reg)
#     attacktarget.exevute(region=reg)


# time.sleep(3)
    