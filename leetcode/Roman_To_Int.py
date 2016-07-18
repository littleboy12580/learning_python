#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def roman_to_int(self,s):    #将罗马数字转换为数字
        roman_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        temp = 0
        for i in range(len(s)):
            if i > 0 and roman_int[s[i]] > roman_int[s[i-1]]:
                temp += roman_int[s[i]] - 2 * roman_int[s[i-1]]
            else:
                temp += roman_int[s[i]]
        return temp

