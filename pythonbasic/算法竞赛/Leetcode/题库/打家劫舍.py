# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2：
#
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 解题：那这题一看就差不多是动态规划了
# dp的话，那就要寻找递归和边界条件

nums = [2,3,2]


# def robRange(start: int, end: int) -> int:
#     first = nums[start]
#     second = max(nums[start], nums[start + 1])
#     for i in range(start + 2, end + 1):
#         first, second = second, max(first + nums[i], second)
#     return second
#
#
# length = len(nums)
# if length == 1:
#     print(nums[0])
#     # return nums[0]
# elif length == 2:
#     print(max(nums[0], nums[1]))
#     # return max(nums[0], nums[1])
# else:
#     print(max(robRange(0, length - 2), robRange(1, length - 1)))
#     # return max(robRange(0, length - 2), robRange(1, length - 1))


# 根据动态规划方程，我们可以得到 ：
def arrayMax(arr):
    ARR_LEN = len(arr) - 1
    # 首先是，根据动态规划方程 这个是arr长度大于2时
    if ARR_LEN >= 2:
        return max(arrayMax(arr[0: ARR_LEN - 1])+arr[ARR_LEN], arr[ARR_LEN - 1])
    # 如果长度等于2
    elif ARR_LEN == 1:
        return max(arr[0], arr[1])
    # 如果长度等于1，那就是本身
    else:
        return arr[0]

# 由于首尾相连，最大值在包括首或尾之间

if len(nums) == 1:
    print(nums[0])
elif len(nums) == 2:
    print(max(nums[0], nums[1]))
else:
    max1 = arrayMax(nums[0: -1])
    max2 = arrayMax(nums[1: len(nums)])
    print(max(max1, max2))







