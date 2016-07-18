#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def int_to_roman(self,num):              #将一个取值范围在1到3999的数转换为罗马数字
        roman_list = [                       #列出所有特殊的情况，与相应的罗马值一一对应
                "M","CM","D","CD",
                "C","XC","L","XL",
                "X","IX","V","IV",
                "I"
                ]
        int_list = [
                1000,900,500,400,
                100,90,50,40,
                10,9,5,4,
                1
                ]
        roman = ''
        index = 0
        while num > 0:
            for _ in range(num // int_list[index]):
                roman += roman_list[i]
                num -= int_list[index]
            index += 1
        return roman
