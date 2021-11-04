

import queue



# maxsize小于等于0时，创建无限队列
queue_ = queue.Queue(maxsize=5)
queue_.put(1)


print([i for i in queue_.queue])


queue_.put('2')
queue_.put('3')
queue_.put('4')
queue_.put('5')

# 打印队列尺寸
print(queue_.qsize())

# 从队列头部出队列
queue_.get()

# 如果不出队列，会进入阻塞状态
queue_.put('6')
# queue_.put('7')
# queue_.put('11')
# queue_.put('22')

print([i for i in queue_.queue])