# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:32:40 2017

@author: Xun Cao
"""

class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])