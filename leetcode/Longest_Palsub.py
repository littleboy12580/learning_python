#!/usr/bin/env python
# encoding: utf-8

class Solution(object):                      #这个是我自己的解法，根据中心点进行迭代
    def longest_pal(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        if len(s) == 1:
            return s
        max_len = 1
        sub = []
        for i in range(2*len(s)-1):                         # 若长度为n，则有2n-1个中心点
            left = i//2
            right = i//2
            if i%2 == 1:
                right+=1
            while(left >= 0 and right <= len(s)):
                if s[left:right] == s[left:right][::-1]:       #判断是否是回文
                    sub.append(s[left:right])                  #是的话存到回文列表里
                left-=1
                right+=1
        for i in range(len(sub)):
            max_len = max(max_len,len(sub[i]))                #计算最大回文长度
        for i in range(len(sub)):
            if(max_len == len(sub[i])):                       #获得最长回文
                return sub[i]



class Solution(object):                                  #这个是网上复杂度很低的解法，思路很有意思
    def longest_palsub(self,s):
        if len(s) == 0:
            return None
        max_len = 1
        start_pos = 0
        for i in range(len(s)):
            if (i-max_len >= 1 and     #针对最开始出现奇数回文的情况
                    s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]):    #回文长度加2的情况
                start_pos = i-max_len-1
                max_len += 2
            if (i-max_len >= 0 and     #针对最开始出现偶数回文的情况
                    s[i-max_len:i+1] == s[i-max_len:i+1][::-1]):        #回文长度加1的情况
                start_pos = i-max_len
                max_len += 1
        return s[start_pos:start_pos+max_len]


