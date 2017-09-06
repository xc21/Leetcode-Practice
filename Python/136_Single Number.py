# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:33:52 2017

@author: Xun Cao
"""
#Given an array of integers, every element appears twice except for one. Find that single one.


class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for num in nums:
            #dict.get, return value for a given key
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key