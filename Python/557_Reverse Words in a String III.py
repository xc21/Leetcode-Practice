# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:13:02 2017

@author: caoxun
"""
# x[::-1]: to reverse a whole list in python; when reverse the string, reverse not
# only the word order but also the digit order
class Solution(object):
    def reverseWords(self, s):
        #string to list, reverse it and then join back to the list
        # reverse the list again 
        return ' '.join(s.split()[::-1])[::-1]
    
#another way:
class Solution(object):
    def reverseWords(self, s):
        return " ".join(map(lambda x: x[::-1], s.split()))