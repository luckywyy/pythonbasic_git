from multiprocessing import Process


def p1():
    for i in range(1, 2000):
        print('p1, ', i)


def p2():
    for i in range(3000, 5000):
        print('p2, ', i)


if __name__ == '__main__':

    print('main process start...')

    p1 = Process(target=p1)
    p2 = Process(target=p2)

    p1.start()
    p2.start()

    p1.join()
    print('main process end...')

# 从执行结果可以看出，join方法会阻塞主进程，执到p1子进程结束才会开始主进程