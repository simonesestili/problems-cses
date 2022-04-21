n = int(input())

for k in range(1, n + 1):
    m = k*k
    ans = m * (m - 1) // 2
    ans -= 4 * (k - 1) * (k - 2)
    print(ans)
