#!/usr/bin/env python
# encoding: utf-8

class Queue(object):
    def __init__(self):            #队列初始化
        self.queue = []

    def enqueue(self,item):    #入队
        self.queue.append(item)

    def dequeue(self):         #出队
        if self.queue!=[]:
            return self.queue.pop(0)
        else:
            return None

    def getlength(self):       #获取队列长度
        return len(self.queue)

    def isempty(self):         #判断队列是否为空
        return self.queue == []

    def show(self):            #显示队列
        if self.queue!=[]:
            print(self.queue)
        else:
            return None
