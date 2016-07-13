#!/usr/bin/env python
# encoding: utf-8

import my_stack
s=my_stack.Stack(10)
for i in range(9):
    s.push(i)
s.show()
s.push(9)
s.show()
s.push(10)
s.pop()
s.show()
print(s.length())
print(s.gettop())
for i in range(9):
    s.pop()
s.pop()
print(s.gettop())
