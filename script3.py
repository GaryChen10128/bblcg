# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:17:23 2021

@author: DIAMO
"""
import pyautogui
import time
region2=(655,0, 1279, 598)
import time


class Click(object):
    def __init__(self,name,scantime,waitresponsetime,startsign,endsign,region,clicktimes,scandur=0.3):
        self.name=name
        self.waitresponsetime=waitresponsetime
        self.scantime=scantime
        self.startsign=startsign
        self.endsign=endsign
        self.region=region
        self.clicktimes=clicktimes
        self.scandur=scandur
        self.execuetimes=0
        self.isSuccess=False
        pass
    def exevute(self):
        self.executeStartTime=time.time()
        while(True):
            print('scan/execute: ',self.name)
            signobj=pyautogui.locateCenterOnScreen(self.startsign)
            if  signobj is not None:
                for i in range(self.clicktimes):
                    pyautogui.leftClick(x=signobj.x, y=signobj.y)
                self.execuetimes+=1
                print('execute {0} times: '.format(self.execuetimes),self.name)
                self.executeSuccessTime=time.time()
                while(True):
                    endobj=pyautogui.locateCenterOnScreen(self.endsign)
                    if endobj is not None:
                        print('execute success: ',self.name)
                        self.isSuccess=True
                        break
                        
                    time.sleep(self.scandur)
                    if time.time()-self.executeSuccessTime>self.waitresponsetime:
                        print('execute timeout: ',self.name)
                        break
                break
            time.sleep(self.scandur)
            if time.time()-self.executeStartTime>self.scantime:
                print('scan timeout: ',self.name)
                break

clickRuby4=Click(name='click reuby4Server',scantime=3,waitresponsetime=3,startsign='./ruby4.png',endsign='reScanServer.png',region=region2,clicktimes=2)


clickRuby4.exevute()
