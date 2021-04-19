#
# 信号量对象是同步原语一种，也就是PV操作
# 在python中，使用acquire()和release（）维护一个计数器
# 当acquire()方法小于0时，会进入阻塞状态


# 在这里个例子中，由于启用了多线程，所以是运行Two方法其次是Two方法
# 由于未定义先后顺序，所以在子线程进入阻塞状态后，主线程会抢先运行
# join方法表示需要等待被调用线程完成执行

import threading
import time

# 从线程对象创建线程
start = time.time()
def targetMethodOne():
    # for i in range(100):
    time.sleep(1)
    print(targetMethodOne.__name__)


def targetMethodTwo():
    # for i in range(100):
    time.sleep(0.5)
    print(targetMethodTwo.__name__)

threadTargetMethodOne = threading.Thread(target=targetMethodOne)
threadTargetMethodTwo = threading.Thread(target=targetMethodTwo)

threadTargetMethodOne.start()
threadTargetMethodTwo.start()

# 在这里调用join方法，保证主线程最后执行
# 需要注意的是，这行代码需要放在start之后，例如One方法的start和join连用，表示需等待One执行完再执行Two方法
threadTargetMethodOne.join()
threadTargetMethodTwo.join()

end = time.time()

print("用时 {} 秒".format(end - start))