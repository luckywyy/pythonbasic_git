

# 使用*操作符从列表或者元组中解包参数，使用**从字典中解包关键字参数


list_a = [1, 2, 3, 4]

def list_star(*args):
    print(args)
    print(type(args))


list_star(*list_a)

# output:
# (1, 2, 3, 4)
# <class 'tuple'>


kw_a = { "name": "wy", "age": "23"}

def kw_star(**kwargs):
    print(kwargs)
    print(type(kwargs))
    pass

kw_star(**kw_a)

# output:
# {'name': 'wy', 'age': '23'}
# <class 'dict'>