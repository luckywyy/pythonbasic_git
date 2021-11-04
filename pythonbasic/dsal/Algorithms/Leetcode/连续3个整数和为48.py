


a = 1
while a:

    b = a + 1
    c = a + 2

    if a + b + c == 48:
        print("a={}, b={}, c={}".format(a, b, c))
        break

    a += 1