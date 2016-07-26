#!/usr/bin/env python
# encoding: utf-8

#给定一个整数列表和一个目标值，找到列表中的4个数相加的结果等于目标值的数，返回这四个数
#思路：和three_sum_closet的思路相似，只不过多了一个参数外层多了一层遍历循环
class Solution(object):
    def four_sum(self,nums,target):
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if nums[i] > target/4.0:             #如果值比平均值大的话，值绝对大于目标值
                break
            if i > 0 and nums[i] == nums[i-1]:   #相等的话会出现重复状况，因此需要跳过
                continue
            temp_target = target - nums[i]
            for j in range(i+1,len(nums)-2):
                if nums[j] > temp_target/3.0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    temp_sum = nums[j] + nums[left] + nums[right]
                    if temp_sum == temp_target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left_value = nums[left]
                        left += 1
                        while left < right and nums[left] == left_value:
                            left += 1
                        right_value = nums[right]
                        right -= 1
                        while left < right and nums[right] == right_value:
                            right -= 1
                    elif temp_sum < temp_target:
                        left += 1
                    else:
                        right -= 1

        return result
