# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
#
#  
#
# 示例 1：
#
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5




# 这题暴力破解时间复杂度会很高 会超时 优化前在10000000超时，优化后（取根号 从小到大 从大到小）会在 1000000000
c = 999999999

import math
c_ = int(math.pow(c, 0.5))

# for i in range(c_+1):
#     for j in range(c_+1)[::-1]:
#         if i**2+j**2 == c:
#             print(True)
#             break
#
# print(False)

# 再优化下

# for i in range(c_+1):
#     for j in range(c_+1)[::-1]:
#         if i**2+j**2 == c:
#             print(True)
#             break
#         # 数值越来越小 所以小于的话结束当前循环
#         elif i**2+j**2 < c:
#             break
# print(False)


# 上面还是会超时 超时在 999999999 时

# 再优化下 从差值出发
for i in range(c_+1):
    b = math.sqrt(c - i**2)
    if b == int(b):
        print(True)

print(False)