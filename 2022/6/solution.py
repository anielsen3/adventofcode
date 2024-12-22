import sys

INPUT = open(sys.argv[1]).readlines()

def solve(s, sz):
    return next(n for n in range(sz, len(s)) if len(set(s[n-sz:n])) == sz)

for line in INPUT:
    print("1:", solve(line, 4))
    print("2:", solve(line, 14))
