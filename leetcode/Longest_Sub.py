#!/usr/bin/env python
# encoding: utf-8

class Solution(object):                                    #解法一：使用列表
    def len_longestsub(self,s):
        maxlength=0
        usedlist=[]
        for i in s:
            if i in usedlist:                              #判断该字符串是否已经出现过
                usedlist = usedlist[usedlist.index(i)+1:]  #采用分片构建新字符串
            usedlist.append(i)
            maxlength = max(len(usedlist),maxlength)       #计算最大长度
        return maxlength

class Solution(object):                                    #解法二：使用字典
    def len_longestsub(self,s):
        start = maxlength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:   #根据字典键对应值会覆盖前面值的特点
                start = usedChar[s[i]] + 1
            else:
                maxlength = max(maxlength,i-start+1)
            usedChar[s[i]] = i
        return maxlength
