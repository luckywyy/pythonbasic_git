# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 示例 2：
#
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# nums 中的所有整数 互不相同
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-divisible-subset
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 意思是返回一个子集，这个子集长度最大，并且其中两两组合均能满足题目条件


nums = [1,2,3]


# 暴力法：查看所有子集，依次判断子集中是否每个数都能和其他数取余

NUMS_LEN = len(nums)
res = []
# def judgeNums(nums):
#
#     for idx in range(NUMS_LEN):
#         tmp_nums = nums[idx: ]
#         # 暴力判断
#         flag = False
#         for i in range(len(tmp_nums)):
#             for j in range(len(tmp_nums)):
#                 if i != j:
#                     if tmp_nums[i] % tmp_nums[j] != 0 and tmp_nums[j] % tmp_nums[i] != 0:
#                         flag = True
#                         break
#             if flag:
#                 break
#
#
#         if flag == False:
#             print(tmp_nums)
#             return tmp_nums
#             break


for i in range(NUMS_LEN):
    flag = False
    for j in range(NUMS_LEN):
        if i != j:
            print(nums[i], nums[j])
            if nums[i] % nums[j] == 0 and nums[j] % nums[i] == 0:
                continue
            else:
                flag = True
                break

    if flag == False:
        res.append(nums[i])

print(nums)
#
# res_1 = judgeNums(nums)
# nums = nums[::-1]
# res_2 = judgeNums(nums)
#
# if len(res_1) >= len(res_2):
#     print(res_1)
# else:
#     print(res_2[::-1])


