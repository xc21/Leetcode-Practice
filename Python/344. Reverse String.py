# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 01:01:15 2018

@author: Xun Cao
"""

#1 with python string method
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
#2. method 2: 2 pointers
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp

        return ''.join(s)
    

#3. recursion
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        left_s = s[:len(s)/2]
        right_s = s[len(s)/2:]
        return self.reverseString(right_s) + self.reverseString(left_s)        