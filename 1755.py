from collections import deque, Counter
s = input()

def reorder():
    count = Counter(s)
    odds, odd = 0, None
    for c in count:
        if count[c] & 1:
            odds += 1
            odd = c
    if odds > 1: return None
    ans = deque([odd] if odd else [])
    for c in count:
        for _ in range(count[c] >> 1):
            ans.appendleft(c)
            ans.append(c)
    return ''.join(ans)


ans = reorder()
print(ans if ans else 'NO SOLUTION')
