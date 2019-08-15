# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:28:05 2019

@author: 10539
"""

class Solution:
    def reverseString(self, s):
        i, j = 0, len(s) - 1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s