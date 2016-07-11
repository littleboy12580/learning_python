#!/usr/bin/env python
# encoding: utf-8

#该程序实现的功能是：给定一个名单，让你将名单存储到字典中并按序输出该名单
#名单为：Wan Zeyao,Hu Siqi,Li Xiang,Yu Yue,Wan Jianyi,Li Ping,Li Yuanfang

namemap={}
key='Wan'
value='Zeyao'
namemap.setdefault(key,[]).append(value)
value='Jianyi'
namemap.setdefault(key,[]).append(value)  #将key对应的值用列表表示来实现一键多值
key='Hu'
value='Siqi'
namemap.setdefault(key,[]).append(value)
key='Li'
value='Xiang'
namemap.setdefault(key,[]).append(value)
value='Ping'
namemap.setdefault(key,[]).append(value)
value='Yuanfang'
namemap.setdefault(key,[]).append(value)
print(namemap)
ks=namemap.keys()
ks=list(ks)                              #将字典的键值对转换为列表来实现排序
ks.sort()
for k in ks:
    for i in range(len(namemap[k])):     #获取键值对应列表长度
        print("Name:%s %s" % (k,namemap[k][i]))

