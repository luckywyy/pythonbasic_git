
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

        while idx < len(str(a)):
            front = 0
            if idx >= 1:
                front = int(str(a)[idx-1])
            if int(str(a)[idx]) > int(str(b)[idx]) and int(str(a)[idx]) > front:
                return originA, originB
            elif int(str(a)[idx]) < int(str(b)[idx]) and int(str(b)[idx]) > front:
                return originB, originA
            idx += 1
        if originB > originA:
            return originA, originB
        else:
            return originB, originA


print(ourSort(3432, 34324))

