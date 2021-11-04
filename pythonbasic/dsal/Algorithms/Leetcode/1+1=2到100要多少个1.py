
total = 0
for i in range(1, 101):
    # r = i + i
    # s = str(i) + "+" + str(i) + "=" + str(r)
    s = "{}+{}={}".format(i, i, i + 1)
    total += s.count("1")
    # print(s)

print(total)
# out 102