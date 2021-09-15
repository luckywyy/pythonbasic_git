


# 使用items从字典中取出对应的键值


dicts = { "name": "wy", "age": 1111, "likes": "kkkk"}


for item in dicts.items():

    print(item)


# zip()函数可以一一对应
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))