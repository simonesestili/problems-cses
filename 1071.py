t = int(input())
tests = []
for _ in range(t):
    tests.append(tuple(map(int, input().split())))

def query(row, col):
    layer = max(row, col)
    prev = (layer - 1) * (2 + 2 * (layer - 2)) // 2

    idx = col if row == layer else layer + layer - row
    val = idx if layer & 1 else (layer - 1) * 2 + 2 - idx
    return prev + val

for ans in [query(r, c) for r, c in tests]:
    print(ans)
