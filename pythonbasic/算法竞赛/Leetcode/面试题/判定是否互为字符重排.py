# 面试题 01.02. 判定是否互为字符重排
# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
#
# 示例 1：
#
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
# 示例 2：
#
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
# 说明：
#
# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100


# 思路：首先条件是两个字符串长度一致，换句话说，字符需要在另外一个字符串当中 在其中的字符串的数量需要一致

s1 = "abc"
s2 = "bca"

if len(s1) != len(s2):
    print(False)

s1_dict = {}

for e in set(s1):
    s1_dict[e] = s1.count(e)

s2_dict = {}

for e in set(s2):
    s2_dict[e] = s2.count(e)

if len(s1_dict) != len(s2_dict):
    print(False)

for e in s1_dict:
    if e not in s2_dict or s1_dict[e] != s2_dict[e]:
        print(False)

print(True)









