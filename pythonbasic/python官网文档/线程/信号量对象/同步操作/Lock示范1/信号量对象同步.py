
# 在这里个例子中，由于启用了多线程，所以是运行Two方法其次是Two方法

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


# 用join方法保证主线程最后运行，用时1秒
threadTargetMethodOne.join()
threadTargetMethodTwo.join()
end = time.time()

print("用时 {} 秒".format(end - start))