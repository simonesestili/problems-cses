seq = input()

def repetitions(s):
    prev, res, curr = '!', 1, 1
    for c in s:
        if c != prev:
            prev, curr = c, 0
        curr += 1
        res = max(res, curr)
    return res

print(repetitions(seq))
