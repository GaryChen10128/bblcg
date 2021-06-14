# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:47:54 2021

@author: DIAMO
"""
import subprocess as sp
tmp = sp.call('cls',shell=True)
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# img = Image.open(r"image\1.JPG")
img = Image.open(r"./warningDisconnection.png")
# img = Image.open(r"./20120282OLnL2ubF9j.jpg")
# img.show()
# print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_string(img, lang="eng"))
out=pytesseract.image_to_string(img,lang="chi_tra")
data = pytesseract.image_to_data(img, output_type=Output.DICT)

print(out)
out=out.replace(" ", "")
out=out.replace("\n", "")

# boxes = len(data['level'])
# for i in range(boxes ):
#     (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#     #Draw box        
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

