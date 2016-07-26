#!/usr/bin/env python
# encoding: utf-8

import my_stack
s = my_stack.Stack(10)
def stack_log(func):
    def wrapper(*args,**kwargs):
        print("call %s():" % func.__name__)
        s.push(func.__name__)
        print("now the stack is:")
        s.show()
        s.pop()
        print("now the stack is:")
        s.show()
        return func(*args,**kwargs)
    return wrapper

@stack_log
def A():
    print("running function A")

@stack_log
def B():
    print("running function B")

@stack_log
def C():
    print("running function C")
    A()
    B()

C()
