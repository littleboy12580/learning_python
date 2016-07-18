#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def my_atoi(self,str):        #实现将任意字符串转换为整数，如果超出范围取最大/最小范围值
        str = str.strip()         #先去掉各种制表换行空格
        if not str:
            return 0
        MAX_INT = 2147483647      #最大范围值
        MIN_INT = -2147483648     #最小范围值
        overflow = False          #判断是否溢出
        pos = 0
        sign = 1                  #数值正负
        temp = 0
        if str[pos] == '-':
            pos += 1
            sign = -1
        elif str[pos] == '+':
            pos += 1
        for i in range(pos,len(str)):
            if not str[i].isdigit():
                break
            temp = temp * 10 + int(str[i])
            if not MIN_INT <= sign * temp <= MAX_INT:
                overflow = True
                break
        if overflow:
            return MAX_INT if sign == 1 else MIN_INT
        else:
            return sign * temp
