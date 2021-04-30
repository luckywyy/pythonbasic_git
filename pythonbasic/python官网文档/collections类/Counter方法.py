#
#
# class collections.Counter([iterable-or-mapping])
# 一个 Counter 是一个 dict 的子类，用于计数可哈希对象。它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。计数可以是任何整数值，包括0和负数。 Counter 类有点像其他语言中的 bags或multisets。
#

# https://docs.python.org/zh-cn/3.10/library/collections.html#collections.Counter

import collections

arr = [1, 1, 1, 2, 2, 3, 4, "wa", "wa"]

c = collections.Counter(arr)
print(c)

print(c[1])
print(c["wa"])

# out 输出次数


# 删除
del c[1]

print(c)

# 和字典相互转换
dict = dict(c)
print(dict)

# 和字典一样添加元素
c["add"] = 5
print(c)

# 取键做列表
arr = list(c)
print(arr)

# 取每项做列表
arr = list(c.items())
print(arr)

# 取值做列表
arr = list(c.values())
print(arr)