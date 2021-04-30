

# 输入一个整数n（0<n<10），显示n行如下规律图形。
# 例如输入3 ，显示
#           1
#        2 3
#     4 5 6
# 例如输入5，显示
#                                         1
#                                 2      3
#                         4      5      6
#                  7     8      9     10
#          11  12   13    14     15



# n = int(input())
n = 5

numbers = n * n
count = 1
for i in range(n+1):

    for j in range(n):

        if n - j  > i:
            print(" ", end=" ")
        else:
            print(count, end=" ")
            count += 1

    print('')



