#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def reverse(self,x):
        L = list(str(x))
        s = ''
        if x >= 0:
            L = L[::-1]
        else:
            L = L[:1] + L[:0:-1]
        for l in L:
            s += l
        i = int(s)
        if i >= -2147483648 and i <= 2147483648:
            return i
        else:
            return 0
