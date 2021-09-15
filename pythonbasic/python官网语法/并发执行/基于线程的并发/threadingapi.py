

import threading
from threading import Timer
from threading import Lock

t = 1

lock = Lock()
lock.acquire()

def printa(msg = ''):

    lock.acquire()
    for i in range(0, 33):
        print(msg, i)

def printb():
    # lock2.acquire()
    for i in range(0, 33):
        print('b', i)
    lock.release()

a = threading.Thread(target=printa, args=('msg', ))
b = threading.Thread(target=printb)


a.start()
# a.join()
b.start()

# print('threading count: ', threading.active_count())

# 使用Lock获得锁，需要在建立的时候将锁阻塞