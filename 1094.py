length = int(input())
nums = list(map(int, input().split()))

def minMoves(n, arr):
    res, prev = 0, arr[0]
    for i in range(1, n):
        if arr[i] < prev:
            res += prev - arr[i]
        prev = max(arr[i], prev)
    return res

print(minMoves(length, nums))
