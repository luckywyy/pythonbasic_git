# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#  
#
# 示例 1：
#
# 输入：nums = [10,2]
# 输出："210"
# 示例 2：
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 示例 3：
#
# 输入：nums = [1]
# 输出："1"
# 示例 4：
#
# 输入：nums = [10]
# 输出："10"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 首先分析，在相同位中，9越靠前那么数越大 比如第一个示例 10 和 2 2排在10前面
# 比如 3 30 34 5 9 示范，9排在最前面，然后是5 由于3 30 34 开头数字一样，因此比较第2位 接着是34
# 3 和 30，将3放大到30，和30相等，但是330比303大
# 根据上面例子，自己列举下 30 和 300，那么 30300 比 30030大，3 和 300 应该是3300 而不是 3003， 34 和 3 应该是 343 而不是 334 32
# 32 和 3 应该是 332 而不是323， 2 和 30 应该是 302 而不是 230
# 所以 要按照最左边越大优先原则，最左边相等，则看第二位，第二位大于等于第一位，多位大于少位，第二位小于第一位，少位大于多位
# 也就是把数组排个序，排序规则如上

nums = \
    [432,43243]

# 假设使用冒泡方法来排
def ourSort(a, b):

    if len(str(a)) == len(str(b)):
        if a > b :
            return a, b
        else:
            return b, a
    else:
        originA = a
        originB = b
        while len(str(a)) > len(str(b)):
            b *= 10
        while len(str(a)) < len(str(b)):
            a *= 10
        idx = 0
        frontMax = 0
        while idx < len(str(a)):
            front = 0
            if idx >= 1:
                front = int(str(a)[idx-1])
                if front > frontMax:
                    frontMax = front

            if int(str(a)[idx]) > int(str(b)[idx]) and int(str(a)[idx]) >= frontMax:
                return originA, originB
            elif int(str(a)[idx]) < int(str(b)[idx]) and int(str(b)[idx]) >= frontMax:
                return originB, originA
            idx += 1
        if originB > originA:
            return originA, originB
        else:
            return originB, originA


for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a, b = ourSort(nums[i], nums[j])
        nums[i] = a
        nums[j] = b

print("".join(map(str, nums)))

# NUMS_MIN = min(nums)
# NUMS_MAX = max(nums)
# NUMS_MIN_LEN = len(str(NUMS_MIN))
# NUMS_MAX_LEN = len(str(NUMS_MAX))
#
# res = ""
# for numLen in range(NUMS_MIN_LEN, NUMS_MAX_LEN+1):
#     tmpArray = []
#     for num in nums:
#         if len(str(num)) == numLen:
#             tmpArray.append(num)
#             # nums.remove(num)
#
#     print(tmpArray)
#     while len(tmpArray) > 0:
#         tmpArrayMax = max(tmpArray)
#         res += str(tmpArrayMax)
#         tmpArray.remove(tmpArrayMax)
#
#
# print(res)


# s = []
# for i in nums:
#     tmp = (str(i)*10)[:10]
#     heapq.heappush(s, [-int(tmp), str(i)])
# ans = ""
# while s:
#     ans += heapq.heappop(s)[1]
# return str(int(ans))





