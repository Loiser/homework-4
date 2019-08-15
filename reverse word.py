# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:30:35 2019

@author: 10539
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        strr=s.split(' ')
        s=[]
        for i in strr:
            s.append(i[::-1])
        return ' '.join(s)
ll=Solution()
print(ll.reverseWords("i am"))
