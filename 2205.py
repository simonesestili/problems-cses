n = int(input())

for i in range(1 << n):
    val = i ^ (i >> 1)
    ans = [val >> j & 1 for j in range(n - 1, -1, -1)]
    print(''.join(map(str, ans)))
