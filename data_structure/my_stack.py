#!/usr/bin/env python
# encoding: utf-8

class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size             #栈的大小
       # self.top = -1                #栈顶对象

    def isempty(self):               #判断栈是否为空
        return len(self.stack) == 0

    def isfull(self):                #判断栈是否已满
        return self.length() == self.size

    def push(self,item):             #入栈
        if not self.isfull():
            self.stack.append(item)
        #    self.top+=1
        else:
            print("栈已满")

    def pop(self):                   #出栈
        if not self.isempty():
            return self.stack.pop()
        else:
            print("栈已空")

    def length(self):                #获取栈内目前对象数量
        return len(self.stack)

    def change_size(self,num):        #修改栈的大小
        self.size=num

    def get_size(self):               #获取栈的大小
        return self.size

    def get_top(self):                #获取栈顶对象
        if not self.isempty():
            return self.stack[self.length()-1]
        else:
            print("栈已空")

    def show(self):                  #显示栈内对象
        print(self.stack)

