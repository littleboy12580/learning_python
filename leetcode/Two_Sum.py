#!/usr/bin/env python
# encoding: utf-8
class Solution(object):
    def Sum(self,nums,target):
        for i in range(len(nums)):
            if(target-nums[i]) in nums[(i+1):]:
                return [i,nums.index(target-nums[i])]

#上面是我自己的解法，复杂度比较高，耗时56ms
#看了一些网上的解法发现使用字典的话可以降低复杂度
#下面是使用字典的解法
def Sum(self,nums,target):
    dictMap={}
    final_list=[]
    for index,value in enumerate(nums):    #python内置的遍历函数，第一个是序号，第二个是值
        if (target - value) in dictMap:           #这种方式只会遍历一遍列表
            final_list.append([dictMap[target - value], index]) #我对网上解法的改进，考虑了多解的情况
        dictMap[value]=index
    return final_list                              #耗时46ms
