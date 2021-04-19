
# 目的是让One方法先输出，Two后输出
# Lock锁对象类提供了acquire方法和release方法用于PV操作

import threading
import time

# 创建一个锁
lock = threading.Lock()

# 从线程对象创建线程
start = time.time()
def targetMethodOne():
    # for i in range(100):
    lock.acquire()
    time.sleep(1)
    print(targetMethodOne.__name__)
    lock.release()


def targetMethodTwo():
    # for i in range(100):
    lock.acquire()
    time.sleep(0.5)
    print(targetMethodTwo.__name__)

threadTargetMethodOne = threading.Thread(target=targetMethodOne)
threadTargetMethodTwo = threading.Thread(target=targetMethodTwo)

threadTargetMethodOne.start()
threadTargetMethodTwo.start()

threadTargetMethodOne.join()
threadTargetMethodTwo.join()




end = time.time()

print("用时 {} 秒".format(end - start))

# out: 用时1.51秒
# 使用这种方法会比把One方法start join连用运行时间长，上锁解锁需要时间