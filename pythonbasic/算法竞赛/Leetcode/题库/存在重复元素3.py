# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
#
# 如果存在则返回 true，不存在返回 false。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：
#
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：
#
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 思路 题目给了判断条件，先按照条件暴力破解，看是否会超时
# 需要满足两个条件 abs(nums[i] - nums[j]) <= t and abs(i - j) <= k

# # version 1
# nums = [1,5,9,1,5,9]
# k = 2
# t = 3
#
#
# NUMS_LEN = len(nums)
#
# flag = False
# for i in range(NUMS_LEN):
#     for j in range(i, NUMS_LEN):
#         if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k and i != j :
#             flag = True
#             break
#
#     if flag:
#         print("true")
#         break
#
# if flag == False:
#     print("false")


# 根据结果，大概也是刚开始想的那样，条件不难，但是会超时
# 怎么调整超时问题呢，从搜索上入手，上述是冒泡，时间复杂度高


# version 2




