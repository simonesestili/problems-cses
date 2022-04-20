n = int(input())

def permutation():
    if n < 4: return '1' if n == 1 else 'NO SOLUTION'
    ans = []
    if n & 1:
        mid = n // 2 + 1
        for i in range(n // 2):
            ans.append(mid + 1 + i)
            ans.append(mid - 1 - i)
        ans.append(mid)
    else:
        mid = n // 2
        for i in range(n // 2):
            ans.append(mid + i + 1)
            ans.append(i + 1)
    return ' '.join(map(str, ans))

print(permutation())
