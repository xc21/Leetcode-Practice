# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:17:40 2017

@author: Xun Cao
"""
# binary search
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = ( left + right ) / 2
            if A[mid] < target:
                left = mid + 1 # keep going to the right
            elif A[mid] > target:
                right = mid - 1 # keep going to the left
            else:
                return mid
        return left
