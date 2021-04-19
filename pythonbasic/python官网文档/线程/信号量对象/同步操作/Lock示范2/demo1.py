
# 填充target参数，实际上是重写run方法，同样的也可以继承threading.Thread类，重写run方法
# 下面这个例子是存钱取钱操作

# 账户初始1000元
balance = 500

def drawMoney(n = -1000):
    global balance
    if abs(balance) < abs(n):
        print("余额不足")
        return
    balance += n
    print("drawMoney 余额 {}".format(balance))

def saveMoney(n = 1500):
    global balance
    balance += n
    print("saveMoney 余额 {}".format(balance))

import threading
t1 = threading.Thread(target=drawMoney)
t2 = threading.Thread(target=saveMoney)

t1.start()
t2.start()

t1.join()
t2.join()
print("剩下余额 {}".format(balance))

#