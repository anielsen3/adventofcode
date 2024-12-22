import sys

INPUT = [l.strip() for l in open(sys.argv[1]).readlines()]

def common_letter(ss):
    return list(set.intersection(*map(set, ss)))[0]

def priority(c):
    return ord(c) - (ord('a') if c.islower() else ord('A') - 26) + 1

def score(ss):
    return priority(common_letter(ss))


print(f"1: {sum(score([s[:len(s)//2], s[len(s)//2:]]) for s in INPUT)}")

i = iter(INPUT)
print(f"2: {sum(score(ss) for ss in zip(i, i, i))}")