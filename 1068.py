n = int(input())

def weirdAlgorithm(x):
    res = [x]
    while x != 1:
        if x & 1: x = 3 * x + 1
        else: x >>= 1
        res.append(x)
    return res

print(' '.join(map(str, weirdAlgorithm(n))))
