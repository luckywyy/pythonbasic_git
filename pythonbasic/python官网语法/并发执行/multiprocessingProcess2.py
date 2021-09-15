# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
import time


def run_proc(name):
    print(time.time())

    time.sleep(10)
    print('Run child process %s (%s)...' % (name, os.getpid()))


def hello_world():
    print(time.time())

    # time.sleep(5)
    time.sleep(20)
    print('hello world!')
    print('Run child process (%s)...' % (os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=run_proc, args=('test',))
    p2 = Process(target=hello_world)
    print('Process will start.')
    # p1.start()
    # p2.start()
    # p1.join()
    p_list = (p1, p2)
    map(Process.start, p_list)
    print('Process end.')