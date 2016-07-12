#!/usr/bin/env python
# encoding: utf-8

import the_queue
q=the_queue.Queue()
for i in range(10):
    q.enqueue(i)
print("队列为：\n")
q.show()
print("队列的长度为%d" % q.getlength())

