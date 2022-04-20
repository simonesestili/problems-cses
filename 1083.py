n = int(input())
nums = list(map(int, input().split()))

def missingNumber(l, arr):
    ans = 0
    for i in range(l + 1): ans ^= i
    for x in arr: ans ^= x
    return ans

print(missingNumber(n, nums))
