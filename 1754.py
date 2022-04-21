t = int(input())
tests = []
for _ in range(t):
    tests.append(tuple(map(int, input().split())))

def solve(x, y):
    a = (2 * x - y) / 3
    if int(a) != a: return False
    b = x - 2 * a
    return b == int(b) and a >= 0 and b >= 0

for verdict in [solve(a, b) for a, b in tests]:
    print('YES' if verdict else 'NO')
