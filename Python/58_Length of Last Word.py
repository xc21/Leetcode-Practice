# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:36:49 2017

@author: Xun Cao
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0