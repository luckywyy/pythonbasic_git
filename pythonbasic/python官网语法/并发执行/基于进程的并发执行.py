from multiprocessing import Pool
import time
import os


print(os.cpu_count())
def f(x):
    return x*x

# processes 要工作的进程数，默认cpu核心数
if __name__ == '__main__':
    with Pool(processes=5) as p:
        print(p.map(f, [1, 2, 3]))
        time.sleep(100)