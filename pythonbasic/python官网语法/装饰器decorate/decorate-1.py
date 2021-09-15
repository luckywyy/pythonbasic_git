
# 装饰器是一种语法糖-来自官网

def decorater(func):
    def wrapper():
        print('---1---')
        func()
        print('---2---')


    return wrapper


@decorater
def printa(a = 10):
    print('printa {} '.format(a))

# decorater(printa)()

printa()