

lists = ['apple', 'banana', 'lizi']

lists_upper = [i.upper() for i in lists]

print(lists_upper)

lists_enum = list(enumerate(lists))

print(lists_enum)

print(type(lists_enum))

name = input("print your name: ")

print("name: %s" % name)

