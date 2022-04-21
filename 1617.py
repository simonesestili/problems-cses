n = int(input())

MOD = 10**9 + 7

def power(a, b):
    if b == 1: return a
    res = power(a, b >> 1) ** 2 % MOD
    if b & 1: res = res * a % MOD
    return res

print(power(2, n))
