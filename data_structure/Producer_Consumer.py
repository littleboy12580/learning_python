#!/usr/bin/env python
# encoding: utf-8

import threading
import my_queue
import random
import time

class Producer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name = t_name)
        self.buf = queue

    def run(self):
        for i in range(10):
            print("Producer %s is producing %d to the buffer" % (self.getName(),i))
            self.buf.enqueue(i)
            time.sleep(random.randint(1,5))

class Consumer(threading.Thread):
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name = t_name)
        self.buf = queue

    def run(self):
        for _ in range(10):
            print("Consumer %s is consuming %d from the buffer" % (self.getName(),self.buf.dequeue()))
            time.sleep(random.randint(1,5))

def main():
    queue = my_queue.Queue()
    producer = Producer('1',queue)
    consumer = [Consumer(x,queue) for x in '123']
    producer.start()
    for i in range(3):
        consumer[i].start()
    producer.join()
    for i in range(3):
        consumer[i].join()

if __name__ == "__main__":
    main()

