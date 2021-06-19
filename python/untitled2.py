# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:21:42 2021

@author: User
"""

import numpy as np
import cv2
from PIL import ImageGrab
first_frame = None 

while True:
    img = ImageGrab.grab(bbox=(0, 0, 1000, 1100)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    

    # getting the range of blue color in frame
    # frame = cv2.inRange(frame, lower_white, higher_white)
    # cv2.imshow("White", white_range);cv2.waitKey(0);
        
    
    cv2.imshow("frame", frame)
    
    
    if cv2.waitKey(1) & 0Xff == ord('q'):
    # pass
        break
    
cv2.destroyAllWindows()