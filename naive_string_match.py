# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:03:35 2019

@author: 10539
"""

def n_matching(x,y):
    l=len(y)
    for i in range(0,l-len(x)):
        for j in range(len(x)):
            if y[j+i]!=x[j]:break
            if j==len(x)-1:return i
    return("do not exist")
print(n_matching("atax","iamatadorr"))
        