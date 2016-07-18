#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def max_area(self,height):
        area = 0
        for left in range(len(height)):
            for right in range(len(height)):
                if(right > left):
                    area = max(min(height[left]，height[right]) * (j - i),area)
        return area

#上面是自己的解法，暴力遍历，提交答案的时候提示超时。。。
#以下是网上的解法，在遍历的基础上增加了双指针，原理是当左端线段L小于右端线段R时
#我们把L右移，这时舍弃的是L与右端其他线段（R-1, R-2, ...）组成的木桶
#这些木桶是没必要判断的，因为这些木桶的容积肯定都没有L和R组成的木桶容积大

class Solution(object):
    def max_area(self,height):
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(area,min(height[left],height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area
