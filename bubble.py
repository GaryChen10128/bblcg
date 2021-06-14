# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:23:17 2021

@author: DIAMO
"""

from Click import Click
import pyautogui
import time
pyautogui.size().width
region2=(pyautogui.size().width/2,0, pyautogui.size().width/2, pyautogui.size().height)
region1=(0,0, pyautogui.size().width/2, pyautogui.size().height)

import time
lv=1 # 794
skill='./bubble.png'
monster=['chicken']
# monster=['chicken']
if lv==1:
    lvpath='./lv1.png'
if lv==7:
    lvpath='./lv7.png'
if lv==9:
    lvpath='./lv9.png'
if lv==4:
    lvpath='./lv4.png'
scanattack=Click(name='scan attack',scantime=3,
                  waitresponsetime=3,startsign='./attack.png',
                  endsign='reScanServer.png',region=region2,
                  clicktimes=0)
shootattack=Click(name='shoot attack',scantime=3,
                  waitresponsetime=3,startsign=skill,
                  endsign='lv1.png',region=region2,
                  clicktimes=1)

lvattack=Click(name='lv attack',scantime=3,
                  waitresponsetime=3,startsign=lvpath,
                  endsign=None,region=region2,
                  clicktimes=1)

attacktarget=Click(name='attacktarget',scantime=3,
                  waitresponsetime=3,startsign='./giant.png',
                  endsign=None,region=region2,
                  clicktimes=4,scandur=0.1)



scanattack2=Click(name='scan attack',scantime=3,
                 waitresponsetime=3,startsign='./attack.png',
                 endsign='reScanServer.png',region=region1,
                 clicktimes=0)
shootattack2=Click(name='shoot attack',scantime=3,
                 waitresponsetime=3,startsign=skill,
                 endsign='lv1.png',region=region1,
                 clicktimes=1)

lvattack2=Click(name='lv attack',scantime=3,
                 waitresponsetime=3,startsign=lvpath,
                 endsign=None,region=region1,
                 clicktimes=1)

attacktarget2=Click(name='attacktarget',scantime=3,
                 waitresponsetime=3,startsign='./greendolf4.png',
                 endsign=None,region=region1,
                 clicktimes=4,scandur=0.1)



# while(True):
# scanattack.exevute()
# shootattack.exevute()
# lvattack.exevute()
# attacktarget.exevute()

scanattack2.exevute()
shootattack2.exevute()
lvattack2.exevute()
attacktarget2.exevute()


# time.sleep(3)
    