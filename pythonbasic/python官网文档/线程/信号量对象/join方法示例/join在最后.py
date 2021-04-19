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

# out: 用时 1秒