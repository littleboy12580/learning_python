#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def is_pal(self,x):                   #判断一个整数是否是回文数，要求不能使用字符串操作
        if x < 0:                         #负数不存在回文
            return False
        p = x
        temp = 0
        while p:
            temp = temp * 10 + p % 10     #实现整数的倒序
            p = p // 10
        return temp == x
