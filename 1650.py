n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
queries = []
for _ in range(q):
    queries.append(tuple(map(int, input().split())))

prefix = [0]
for x in arr: prefix.append(prefix[-1] ^ x)

for a, b in queries:
    print(prefix[b] ^ prefix[a-1])

