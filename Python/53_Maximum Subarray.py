# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:24:55 2017

@author: Xun Cao
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        
        #initial it
        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum