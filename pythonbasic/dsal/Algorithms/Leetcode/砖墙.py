# # 你的面前有一堵矩形的、由 n 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和应该相等。
# #
# # 你现在要画一条 自顶向下 的、穿过 最少 砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。
# #
# # 给你一个二维数组 wall ，该数组包含这堵墙的相关信息。其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。你需要找出怎样画才能使这条线 穿过的砖块数量最少 ，并且返回 穿过的砖块数量 。
# #
#
# 输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# 输出：2

# 分析：题目初看挺复杂，以示例输入为例 - 表示砖墙
# - -- -- -
# --- - --
# - --- --
# -- ----
# --- - --
# - --- - -
# 那么上面的砖墙，从最后一列下去，是穿越最短的，也就是答案2，那么就可以用数组方式构建砖墙
# 每层总数相等，间隔不同

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# 行数
WALL_LINE = len(wall)

arr = []
# 以 1 代表砖头 0 代表空格 构造出数组
for line in wall:
    tmp = []
    for i in line:
        while i > 0:
            tmp.append(1)
            i -= 1
        tmp.append(0)
    # 最后一个没有间隔 要弹出末尾
    tmp.pop()
    arr.append(tmp)

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print(arr[5])

# 那么现在就是计算这个数组列和最小的值，因为每行长度不同（因为间隔不同），所以简单方法是先补充0

MAX_LINE = -1
for i in arr:
    if len(i) > MAX_LINE:
        MAX_LINE = len(i)

for i in range(WALL_LINE):
    while len(arr[i]) < MAX_LINE:
        arr[i].append(0)

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print(arr[5])

res = 99999999
for i in range(MAX_LINE):
    tmp = 0
    for j in range(WALL_LINE):
        tmp += arr[j][i]

    if tmp < res:
        res = tmp

print(res)

# 结果可能超时
