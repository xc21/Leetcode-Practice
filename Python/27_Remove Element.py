# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:53:43 2017

@author: Xun Cao
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    # clrs qsort
    def removeElement(self, A, elem):
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1