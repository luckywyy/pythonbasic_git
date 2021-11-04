
# 0-9 十个数字，按 n 个数进行组合 有多少种
#  9 8 7 和 7 8 9算一样 这样有多少种
# 9 8 7 和 9 7 8 算不一样 这样有多少种




# 假设有个函数qp(m, n) 可以求出m 到 n之间的全排列


#
# def qp(m, n):
#     res = []
#
#     return res
#
#
# # 假设求1-3之间的全排列
# for i in range(1, 4):
#     qp(i,)


n = 4

# for i1 in range(n):
#     for i2 in range(n):
#         for i3 in range(n):
#             for i4 in range(n):
#                 if i1 !=i2 !=i3 != i4:
#                     print(i1, i2, i3, i4)


def qp(i, nums):

    qp(i+1, nums)