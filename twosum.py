# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:02:12 2019

@author: 10539
"""

class Solution:
    def twoSum(self, nums, target):
        for i,val in enumerate(nums):
            if target-val in nums:
                j=nums.index(target-val)
                if(i!=j):
                    ans=[i,j]
                    break
        return ans
'''hash map:  
   class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None 
'''
l=Solution()
a=l.twoSum([1,2,3,4,5],9)
print(a)