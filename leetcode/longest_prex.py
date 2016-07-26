#!/usr/bin/env python
# encoding: utf-8

class Solution(object):                        #实现在一个字符串列表中找到最长公共前缀
    def longest_prefix(self,strlist):
        if len(strlist) == 0:
            return ''
        strlist.sort(key=len)                  #把长度最小的排在最前面，然后依次减短该字符串长度来判断是否满足公共前缀
        for i in range(len(strlist[0]),0,-1):
            temp = []
            for strs in strlist:
                if strs[:i] == strlist[0][:i]:
                    temp.append(strs)
            if len(temp) == len(strlist):
                return strlist[0][:i]
        return ''

