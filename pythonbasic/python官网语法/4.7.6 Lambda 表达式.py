# Lambda表达式用于创建一个小的匿名函数

# 如下返回一个函数


def returnf():


    return lambda a: print(a)


printa = returnf()


kwargs = { "a": "neirong"}

printa(**kwargs)