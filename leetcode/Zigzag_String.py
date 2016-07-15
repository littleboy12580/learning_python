#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def convert_str(self,s,numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        L = ['']*numRows
        index = 0
        step = 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(L)
