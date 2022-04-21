n = int(input())

total = n * (n + 1) // 2

if total & 1: print('NO')
else:
    total >>= 1
    arr1, arr2 = [], []
    for i in range(n, 0, -1):
        if i <= total:
            total -= i
            arr1.append(i)
        else:
            arr2.append(i)
    print('YES')
    print(len(arr1))
    print(' '.join(map(str, arr1)))
    print(len(arr2))
    print(' '.join(map(str, arr2)))
