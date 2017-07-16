# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:12:14 2017

@author: caoxun
"""

import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            #np.reshape syntax: (a, newshape, order='c')
            #order: different index order
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums