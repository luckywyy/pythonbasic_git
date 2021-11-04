# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。


# bin(1)

# print(bin(4))

x = 1
y = 4

bin_x = str(bin(x))[2:][::-1]
bin_y = str(bin(y))[2:][::-1]
# print(bin_x, bin_y)
total = 0
_len = max(len(bin_x), len(bin_y))

while len(bin_x) < _len:
       bin_x += '0'
while len(bin_y) < _len:
       bin_y += '0'


for i in range(_len):
       if bin_x[i] != bin_y[i]:
              total += 1

print(total)








