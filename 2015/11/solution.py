
def is_legal(p):
    legal = False
    for c1, c2, c3 in zip(p, p[1:], p[2:]):
        if ord(c3) - ord(c2) == ord(c2) - ord(c1) == 1:
            legal = True
    
    if 'i' in p or 'o' in p or 'l' in p:
        return False

    paired = set()
    for c1, c2 in zip(p, p[1:]):
        if c1 == c2:
            paired.add(c1)
    if len(paired) < 2:
        return False

    return legal

def increment(p):
    s = list(p)
    for i, c in reversed(list(enumerate(s))):
        if c == '{':
            s[i-1] = chr(ord(s[i-1]) + 1)
            s[i] = 'a'
        if c == 'z':
            s[i-1] = chr(ord(s[i-1]) + 1)
            s[i] = 'a'
            if s[i-1] != '{':
                break
        else:
            s[i] = chr(ord(s[i]) + 1)
            # print(s)
            break

    return "".join(s)

def next_legal(p):
    p = increment(p)
    while not is_legal(p):
        p = increment(p)
    return p

print("1:", next_legal('cqjxjnds'))
print("2:", next_legal('cqjxxyzz'))
