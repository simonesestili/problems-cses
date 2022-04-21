n, m, k = list(map(int, input().split()))
applicants = sorted(map(int, input().split()))
apartments = sorted(map(int, input().split()))

def claims():
    res = 0
    i = j = 0
    while i < n and j < m:
        if apartments[j] - k <= applicants[i] <= apartments[j] + k:
            res, i, j = res + 1, i + 1, j + 1
        elif applicants[i] > apartments[j] + k: j += 1
        else: i += 1
    return res

print(claims())
