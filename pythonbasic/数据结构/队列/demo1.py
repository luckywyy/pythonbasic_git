
# 队列数据结构为先入先出

# 同样的，也可以用列表模拟


queue = []

# 入队列
queue.append(1)
queue.append(2)
queue.append('a')
queue.append([3.])
print(queue)

# 出队列 pop方法不加参数默认删除最后一个，队列为先入先出数据结构，从首开始删
queue.pop(0)
queue.pop(0)
print(queue)

# 入队
queue.append(10)
print(queue)