n = int(input())
MOD = 10**9+7

def ways():
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for d in range(1, 7):
            if i - d < 0: break
            dp[i] = (dp[i] + dp[i-d]) % MOD

    return dp[n]

print(ways())
