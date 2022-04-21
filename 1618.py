n = int(input())

res = 0
while n // 5:
    n //= 5
    res += n

print(res)
