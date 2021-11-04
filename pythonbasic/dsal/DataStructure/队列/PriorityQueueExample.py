# queue中的类
#
# class queue.PriorityQueue(maxsize=0)
# 优先级队列构造函数。 maxsize 是个整数，用于设置可以放入队列中的项目数的上限。当达到这个大小的时候，插入操作将阻塞至队列中的项目被消费掉。如果 maxsize 小于等于零，队列尺寸为无限大。
#
# 最小值先被取出( 最小值条目是由 sorted(list(entries))[0] 返回的条目)。条目的典型模式是一个以下形式的元组： (priority_number, data) 。
#
# 如果 data 元素没有可比性，数据将被包装在一个类中，忽略数据值，仅仅比较优先级数字 ：



import queue

q = queue.PriorityQueue(maxsize=3)


q.put(3)
q.put(1)
q.put(2)

# 会排序
print([i for i in q.queue])
# out: [1, 3, 2]

# 1会被排出 剩下的会被排序
q.get()

# 会排序
print([i for i in q.queue])
# out: [2, 3]




