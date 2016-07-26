#!/usr/bin/env python
# encoding: utf-8

#实现给定一个整数列表和一个目标值，找出列表中三个数相加的结果和目标值最近的数，返回该结果
#思路：先排序，然后遍历一次列表，对于列表的每个值，取它右边列表的最小值和最大值
#然后计算三者和，与target作比较，小的话左边右移，大的话右边左移
class Solution(object):
    def three_sum_closet(self,nums,target):
        if len(numns) < 3:
            return 0
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if nums[i] > target/3.0:     #如果大于后面的值相加肯定大于target
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if abs(temp - target) < abs(result - target):
                    result = temp
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
                else:
                    break
        return result

