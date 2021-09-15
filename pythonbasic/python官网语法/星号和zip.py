

a = [1, 2]
b = ['a', 'b']

c = zip(a, b)

print(a, b)
print(*a)


print(zip(a,b))

for e in zip(a, b):
    print('e-> ', e)

print(*zip(a,b))

print(list(zip(*zip(a,b))))

a, b = zip(a,b)

print(a, b)

def printt(t1, t2):

    print('t: ', t1, t2)

printt(*a)



# *解包一般用来传参


