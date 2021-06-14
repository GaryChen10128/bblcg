# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:58:41 2021

@author: DIAMO
"""

f = open('./x.txt', 'r')
x=[]
for line in f.readlines():
    x.append(line)
    # print(line)
f.close
f = open('./y.txt', 'r')
y=[]
for line in f.readlines():
    y.append(line)
    # print(line)
f.close
axis=[]
for i in range(len(x)):
    print(i)
    axis.append([x[i],y[i]])
    