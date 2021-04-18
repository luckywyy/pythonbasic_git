# 给你一个整数
# n ，请你找出并返回第
# n
# 个
# 丑数 。
#
# 丑数
# 就是只包含质因数
# 2、3
# 和 / 或
# 5
# 的正整数。
#
#
#
# 示例
# 1：
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# 是由前
# 10
# 个丑数组成的序列。
# 示例
# 2：
#
# 输入：n = 1
# 输出：1
# 解释：1
# 通常被视为丑数。

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:


n = int(input())

if n == 1:
    print(1)
i = 2
count = 1
a = [2, 3, 5]
while i > 0:
    k = i+1
    for j in a:
        while i % j == 0:
            i //= j
    if i == 1:
        count += 1
    if count == n:
        print(k-1)
        break
    i = k


# 上面算法会超时 如果正式比赛 在本地算好也是一个较好的选择










