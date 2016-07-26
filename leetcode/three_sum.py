#!/usr/bin/env python
# encoding: utf-8

class Solution(object):                     #与以前做过的2个数相加判断列表中有没有和类似
    def two_sum(self,nums,target):          #不过这次是3个数相加判断是不是为0
        sums = set()                        #因此可以借用以前的two_sum函数
        usedlist = []
        for num in nums:
            if num in usedlist:
                sums.add(tuple([num,target-num,-target]))
            usedlist.append(target-num)
        return sums

    def three_sum(self,nums):
        result = set()
        for i,num in enumerate(nums):
            result = result.union(self.two_sum(nums[i+1:],-num))
        return list(result)
