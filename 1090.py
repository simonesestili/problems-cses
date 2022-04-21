n, x = list(map(int, input().split()))
weights = sorted(map(int, input().split()))

def gondolas():
    res = 0
    i, j = 0, n - 1
    while i < j:
        if weights[i] + weights[j] <= x:
            i, j = i + 1, j - 1
        else:
            j -= 1
        res += 1
    return res + int(i == j)

print(gondolas())
