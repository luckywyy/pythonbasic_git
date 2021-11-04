# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
#
#  
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/powx-n
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
x = 2.00000
n = -8


# 直接使用内置方法 可以通过
print(pow(x, n))


# 递归求解
# 幂n为自然数，如果是负数，取正数倒数即可；偶数，则是不断相乘 n//2 ，奇数则是不断乘 n//2 向下取整


def multi(x):
    return x * x



res = x

if n == 0:
    print(1)

flag = False
if n < 0:
    n = 0 - n
    flag = True

flag2 = False
if n % 2 == 1:
    n = n - 1
    flag2 = True

while n != 1:
    res = multi(res)
    n = n // 2

if flag:
    res = 1 / res

if flag2:
    res = res * x

print(res)






