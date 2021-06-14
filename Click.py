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
    def __init__(self,name,scantime,waitresponsetime,startsign,endsign,region,clicktimes,scandur=0.3,phase=0,delay=0,isReverse=False,leftshift=0):
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
        self.phase=phase
        self.delay=delay
        self.isScanned=False
        self.isReverse=isReverse
        self.leftshift=leftshift
        pass
    def exevute(self,region=None,coordinate=None):
        self.region=region
        self.executeStartTime=time.time()
        for sign in self.startsign:
            while(True):
                print('scan/execute: ',self.name)
                print ('try to find',sign)
                # print('find region',self.region)
                signobj=pyautogui.locateCenterOnScreen(sign,region=self.region)
                if coordinate is None:
                    if  signobj is not None:
                        
                        self.isScanned=True
                        pyautogui.moveTo(signobj.x+self.leftshift, signobj.y,0)
                        time.sleep(self.delay)
                        for i in range(self.clicktimes):
                            
                            pyautogui.leftClick(x=signobj.x+self.leftshift, y=signobj.y)
                            # print('ppppppppppppppp')
                            # pyautogui.mouseDown(x=signobj.x, y=signobj.y)
                            # time.sleep(0.3)
                            # pyautogui.mouseUp(x=signobj.x, y=signobj.y)
                        self.execuetimes+=1
                        print('execute {0} times: '.format(self.execuetimes),self.name)
                        self.executeSuccessTime=time.time()
                        while(True):
                            if self.endsign is None:
                                break
                            endobj=pyautogui.locateCenterOnScreen(self.endsign,region=self.region)
                            if self.isReverse:
                                if endobj is None:
                                    print('execute success: ',self.name)
                                    self.isSuccess=True
                                    break
                                else:
                                    self.isSuccess=False
                                    
                            else:
                                if endobj is not None:
                                    print('execute success: ',self.name)
                                    self.isSuccess=True
                                    break
                                else:
                                    self.isSuccess=False
                            time.sleep(self.scandur)
                            if time.time()-self.executeSuccessTime>self.waitresponsetime:
                                print('execute timeout: ',self.name)
                                break
                        break
                    else:
                        self.isScanned=False
                    pass
                else:
                    if  True:
                        self.isScanned=True
                        time.sleep(self.delay)
                        for i in range(self.clicktimes):
                            pyautogui.leftClick(x=coordinate[0], y=coordinate[1])
                        self.execuetimes+=1
                        print('execute {0} times: '.format(self.execuetimes),self.name)
                        self.executeSuccessTime=time.time()
                        while(True):
                            if self.endsign is None:
                                break
                            endobj=pyautogui.locateCenterOnScreen(self.endsign,region=self.region)
                            if self.isReverse:
                                if endobj is None:
                                    print('execute success: ',self.name)
                                    self.isSuccess=True
                                    break
                                else:
                                    self.isSuccess=False
                            else:
                                
                                if endobj is not None:
                                    print('execute success: ',self.name)
                                    self.isSuccess=True
                                    break
                                else:
                                    self.isSuccess=False
                                
                            time.sleep(self.scandur)
                            if time.time()-self.executeSuccessTime>self.waitresponsetime:
                                print('execute timeout: ',self.name)
                                break
                        break
                    else:
                        self.isScanned=False
                    pass
                
                time.sleep(self.scandur)

                if time.time()-self.executeStartTime>self.scantime:
                    print('scan timeout: ',self.name)
                    break
            if self.isSuccess:
                break

# clickRuby4=Click(name='click reuby4Server',scantime=3,waitresponsetime=3,startsign='./ruby4.png',endsign='reScanServer.png',region=region2,clicktimes=2)


# clickRuby4.exevute()
