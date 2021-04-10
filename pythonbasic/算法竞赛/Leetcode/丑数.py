# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
#
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 示例 1：
#
# 输入：n = 6
# 输出：true
# 解释：6 = 2 × 3
# 示例 2：
#
# 输入：n = 8
# 输出：true
# 解释：8 = 2 × 2 × 2
# 示例 3：
#
# 输入：n = 14
# 输出：false
# 解释：14 不是丑数，因为它包含了另外一个质因数 7 。
# 示例 4：
#
# 输入：n = 1
# 输出：true
# 解释：1 通常被视为丑数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#     def isUgly(self, n: int) -> bool:

#
# 此题来自每日一题，难度简单
# 根据丑数的定义，首先是只包含质因数是2，3，5的正整数 输出是true false
# 意思就是2 3 5的乘组合能得到 n 每个数数量不限

n = int(input())
if n <= 0:
    print("false")
if n == 1:
    print("true")

for a in [2, 3, 5]:
    while n % a == 0:
        n //= a

if n == 1:
    print("true")
else:
    print("false")

# class Solution:
#     def isUgly(self, n: int) -> bool:
#         # n = int(input())
#         if n <= 0:
#             return False;
#         if n == 1:
#             return True;
#
#         for a in [2, 3, 5]:
#             while n % a == 0:
#                 n //= a
#
#         if n == 1:
#             return True;
#         else:
#             return False;