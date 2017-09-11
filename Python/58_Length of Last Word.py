# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:36:49 2017

@author: Xun Cao
"""

#36 ms
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0
#42 ms
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length=0
        if s.split()!=[]:
                               #at last digit
            length=len(s.split()[len(s.split())-1])
        return length
