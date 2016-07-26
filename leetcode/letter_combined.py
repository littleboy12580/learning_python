#!/usr/bin/env python
# encoding: utf-8

#给定一个手机上的数字对应字母规则，然后根据输入的收集数字输出对应的字母组合
#eg：输入'23'，输出['ad','ae','af','bd','be','bf','cd','ce','cf']
#思路：建一个字典来将数字与字母一一对应，然后循环遍历相加就行
class Solution(object):
    def letter_combined(self,digits):
        if not digits:
            return []
        results = ['']
        letter_dicts = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi',
                '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for digit in digits:
            results = [result+d for result in results for letter in dicts[digit]]
        return results
