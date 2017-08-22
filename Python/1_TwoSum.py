# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:51:04 2017

@author: Xun Cao
"""

class Solution(object):
    #nums is a list 
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                #look up the dictionary by key
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i