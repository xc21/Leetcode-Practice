# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:24:55 2017

@author: Xun Cao
"""

class Solution:
    def removeDuplicates(self,nums):
        if (len(nums)==0):
            return 0
        i=0
        j=1
        for j in range(len(nums)):
                if nums[j] != nums[i]:
                    i=i+1
                    nums[i] = nums[j]
                j=j+1
        return i+1    