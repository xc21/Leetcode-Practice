# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:32:41 2017

@author: Xun Cao
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        cache, st = {}, []
        for x in nums:
            while st and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
        result = [-1]*len(findNums)
        for idx,x in enumerate(findNums):
            if x in cache:
                result[idx] = cache[x]
        return result