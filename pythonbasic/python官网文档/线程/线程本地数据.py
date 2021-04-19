

import threading


# 创建线程本地数据，在不同线程中，实例对象数值不同

threading_one = threading.local

threading_one.x = 10

# print(threading_one.x)