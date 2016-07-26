#!/usr/bin/env python
# encoding: utf-8

class Queue(object):
    def __init__(self，size=10):            #队列初始化
        self.queue = []
        self.size = size

    def enqueue(self,item):            #入队
        if not self.isfull():
            self.queue.append(item)
        else:
            print("the queue is full")

    def dequeue(self):         #出队
        if self.queue!=[]:
            return self.queue.pop(0)
        else:
            return None
            print("the queue is empty")

    def getlength(self):       #获取当前队列内对象数目
        return len(self.queue)

    def isempty(self):         #判断队列是否为空
        return self.queue == []

    def isfull(self):
        return self.getlength() == self.size
    def show(self):            #显示队列
        if self.queue!=[]:
            print(self.queue)
        else:
            return None
