# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:23:17 2021

@author: DIAMO
"""

from Click import Click
import pyautogui
import time
pyautogui.size().width
# region2=(pyautogui.size().width/2,0, pyautogui.size().width/2, pyautogui.size().height)
# region1=(0,0, pyautogui.size().width/2, pyautogui.size().height)
region1=(0,0,pyautogui.size().width,pyautogui.size().height)

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
skillclick=Click(name='skill click',scantime=3,
                  waitresponsetime=3,startsign=['./skill.png'],
                  endsign='dig.png',region=region1,
                  clicktimes=1)

dig=Click(name='dig',scantime=3,
                  waitresponsetime=3,startsign=['./dig.png'],
                  endsign='diglv.png',region=region1,
                  clicktimes=1)
diglv=Click(name='diglv',scantime=9,
                  waitresponsetime=9,startsign=['./diglv.png'],
                  endsign='working.png',region=region1,
                  clicktimes=4)
movemouse=Click(name='movemouse',scantime=3,
                  waitresponsetime=3,startsign=['./working.png'],
                  endsign='working.png',region=region1,
                  clicktimes=3)
skillcancel=Click(name='skill cancel',scantime=3,
                  waitresponsetime=3,startsign=['./skill2.png'],
                  endsign='skill.png',region=region1,
                  clicktimes=1)
checkhealth=Click(name='checkhealth',scantime=3,
                  waitresponsetime=3,startsign=['./white.png'],
                  endsign='skill.png',region=region1,
                  clicktimes=0)

cureskill=Click(name='cureskill click',scantime=3,
                  waitresponsetime=3,startsign=['./cure.png'],
                  endsign='me2.png',region=region1,
                  clicktimes=3)

curesme=Click(name='cure me',scantime=3,
                  waitresponsetime=3,startsign=['./me3.png'],
                  endsign='curetarget.png',region=region1,
                  clicktimes=1,delay=0)

curetarget=Click(name='cure target',scantime=3,
                  waitresponsetime=3,startsign=['./cureTarget.png'],
                  endsign='curesuccess.png',region=region1,
                  clicktimes=3)

iscuresuccess=Click(name='cure success',scantime=3,
                  waitresponsetime=3,startsign=['./curesuccess.png'],
                  endsign=None,region=region1,
                  clicktimes=3)
# eeennd='./selectTarget.png'
eeennd=None
sh=90
dd=2.5
retry=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./retry.png'],
                  endsign=eeennd,region=region1,
                  clicktimes=1,delay=dd)
t1=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t1.png'],
                  endsign=None,region=region1,
                  clicktimes=1,leftshift=sh,delay=dd)
t2=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t2.png'],
                  endsign=None,region=region1,
                  clicktimes=1,leftshift=sh,delay=dd)
t3=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t3.png'],
                  endsign=None,region=region1,
                  clicktimes=1,leftshift=sh,delay=dd)
t4=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t4.png'],
                  endsign=None,region=region1,
                  clicktimes=1,leftshift=sh,delay=dd)

t1x=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t1.png'],
                  endsign=None,region=region1,
                  clicktimes=1,delay=dd,leftshift=sh)
t2x=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t2.png'],
                  endsign=None,region=region1,
                  clicktimes=1,delay=dd,leftshift=sh)
t3x=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t32.png'],
                  endsign=None,region=region1,
                  clicktimes=1,delay=dd,leftshift=sh)
t4x=Click(name='retry',scantime=3,
                  waitresponsetime=3,startsign=['./t4.png'],
                  endsign=None,region=region1,
                  clicktimes=1,delay=dd,leftshift=sh)
time.sleep(2)
# delayy=3
while(True):
    retry.exevute()
    # pyautogui.moveRel(100,100,1)
    t1.exevute()
    t1x.exevute()
    
    # time.sleep(0.3)
    # x,y=pyautogui.position().x+50,pyautogui.position().y+50
    # pyautogui.moveTo(x,y,0)
    # time.sleep(0.3)
    
    retry.exevute()
    # pyautogui.moveRel(100,100,1)
    t2.exevute()
    t2x.exevute()
    
    # time.sleep(0.3)
    # x,y=pyautogui.position().x+50,pyautogui.position().y+50
    # pyautogui.moveTo(x,y,0)
    # time.sleep(0.3)
    
    retry.exevute()
    # pyautogui.moveRel(100,100,1)
    t3.exevute()
    t3x.exevute()
    t3x.exevute()
    # time.sleep(0.3)
    # x,y=pyautogui.position().x+50,pyautogui.position().y+50
    # pyautogui.moveTo(x,y,0)
    # time.sleep(0.3)
    
    
    retry.exevute()
    # pyautogui.moveRel(100,100,1)
    t4.exevute()
    t4x.exevute()
    
    time.sleep(0.3)
    x,y=pyautogui.position().x+50,pyautogui.position().y+50
    pyautogui.moveTo(x,y,0)
    time.sleep(0.3)
    x,y=pyautogui.position().x+60,pyautogui.position().y
    pyautogui.moveTo(x,y,0)
    # checkhealth.exevute()
    # if checkhealth.isScanned:
    #     #unhealth
    #     skillclick.exevute()
    #     cureskill.exevute()
    #     # time.sleep(2)
    #     # me=pyautogui.locateCenterOnScreen('./me2.png')
    #     # pyautogui.moveTo(me.x,me.y,2)
    #     # pyautogui.moveRel(100,100,2)
    #     curesme.exevute()
    #     curetarget.exevute()
    #     skillcancel.exevute()


    #     # movemouse.exevute()
    # else:
    #     # continue
    #     iscuresuccess.exevute()
    #     if iscuresuccess.isScanned:
    #         pyautogui.moveRel(100,100,1)
    #         skillcancel.exevute()
    #         pyautogui.moveRel(100,100,1)
    #         skillclick.exevute()
    #         dig.exevute()
    #         pyautogui.moveRel(100,100,1)
    #         diglv.exevute()
    #         pyautogui.moveRel(100,100,1)
    #         movemouse.exevute()
    #         pyautogui.moveRel(100,100,1)
    #         skillcancel.exevute()
    #         pyautogui.moveRel(100,100,1)
    #         movemouse.exevute()
    #         pyautogui.moveRel(100,100,2)
    #     pass
        

    # break
    # time.sleep(2)
    