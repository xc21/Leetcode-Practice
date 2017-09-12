# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:48:49 2017

@author: Xun Cao
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0
        
        if flag == 1:
            digits.insert(0, 1)
        return digits