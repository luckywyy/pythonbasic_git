

# 把两个有序数组排序 去除重复值





def sortArray(a, b):

    res = []
    A_LEN = len(a)
    B_LEN = len(b)

    idx_a, idx_b = 0, 0
    while idx_a < A_LEN or idx_b < B_LEN:
        if idx_a == A_LEN:
            if b[idx_b] not in res:
                res.append(b[idx_b])
            idx_b += 1
        elif idx_b == B_LEN:
            if a[idx_a] not in res:
                res.append(a[idx_a])
            idx_a += 1
        elif a[idx_a] < b[idx_b]:
            if a[idx_a] not in res:
                res.append(a[idx_a])
            idx_a += 1
        else:
            if b[idx_b] not in res:
                res.append(b[idx_b])
            idx_b += 1
    return  res


a = [1,1,1,1,1,3,4,7]
b = [1,2,2,3,4,5,5,5,8]


res = sortArray(a, b)


print(res)


