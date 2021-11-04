


# python中lambda表达式用法
# python中sorted函数
# lambda 一般 和 sorted排序函数放一起用


# Lambda 表达式（lambda expression）是一个匿名函数，Lambda表达式基于数学中的λ演算得名，直接对应于其中的lambda抽象（lambda abstraction），是一个匿名函数，即没有函数名的函数。Lambda表达式可以表示闭包（注意和数学传统意义上的不同）。
# 是一种快速定义单行的最小函数，可以简化代码

# 从定义中可以看出 lambda是一个匿名函数 既然是函数 那么就是实现里面的函数体

# 接下来就是语法，lambda的语法是:
# lambda 参数1, 参数2 : 语句

# 例如：

# 使用lambda语法定义了一个函数 total
total = lambda a, b : a + b
# 传入参数1 3 输出total值
print(total(1, 3))
# 实际上上述就是下面这个函数
def total2(a, b):
    return a + b
print(total2(1, 3))

# 比如常用的是给字典排序
dict_ = {'a': 3, 'b': 1, 'd': 10, 'c': 5}

# python 自带了 sorted函数
print(sorted(dict_))
print(sorted(dict_, reverse=True))
print(sorted(dict_.values(), reverse=True))
print(sorted(dict_.keys(), reverse=True))
print(sorted(dict_.items(), reverse=True))
# ['a', 'b', 'c', 'd']
# ['d', 'c', 'b', 'a']
# [10, 5, 3, 1]
# ['d', 'c', 'b', 'a']
# [('d', 10), ('c', 5), ('b', 1), ('a', 3)]

# 上面依次是输出，但是不能按照值的大小进行排序
# sorted 函数有 key 参数
print(sorted(dict_.items(), key= lambda item: item[1]))
print(sorted(dict_.items(), key= lambda item: item[1], reverse=True))


# 不仅是字典 列表也行
scores = [("zhangsan", 90), ("wangsi", 80), ("wubai", 78), ("panda", 100), ("angqi", 69)]



print(sorted(scores, key= lambda x : x[0]))
print(sorted(scores, key= lambda x : x[1]))











