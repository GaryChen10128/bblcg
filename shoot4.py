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
region1=(0,0, int(pyautogui.size().width/2), pyautogui.size().height)
region=[region1,region2]
import time
lv=int(input("請輸入lv  ")) # 794
skill=['./bubble.png','./shoot.png']
monsterlist=['./giant.png','./giant2.png','./greendog.png','./greendog2.png','./giant3.png','./giant4.png']

if lv==9:
    lvpath=['./lv{0}.png'.format(lv),'./lv{0}.png'.format(lv-1)]
else:
    lvpath=['./lv{0}.png'.format(lv),'./lv{0}.png'.format(lv+1)]
print('lvpath',lvpath)


scanattack=Click(name='scan attack',scantime=3,
                 waitresponsetime=3,startsign=['./attack.png'],
                 endsign='reScanServer.png',region=region1,
                 clicktimes=0,scandur=0.1)
shootattack=Click(name='shoot attack',scantime=3,
                 waitresponsetime=3,startsign=skill,
                 endsign='lv1.png',region=region1,
                 clicktimes=1,scandur=0.3)

lvattack=Click(name='lv attack',scantime=3,
                 waitresponsetime=3,startsign=lvpath,
                 endsign=None,region=region1,
                 clicktimes=1)

attacktarget=Click(name='attacktarget',scantime=0.5,
                 waitresponsetime=3,startsign=monsterlist,
                 endsign=None,region=region1,
                 clicktimes=4,scandur=0)




# while(True):
# scanattack.exevute()
# shootattack.exevute()
# lvattack.exevute()
# attacktarget.exevute()
for reg in region:
    # scanattack.exevute(region=reg)
    shootattack.exevute(region=reg)
    lvattack.exevute(region=reg)
    attacktarget.exevute(region=reg)


# time.sleep(3)
    