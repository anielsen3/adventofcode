def solve(sz):
    s = open("input1.txt").read()
    return next(n+sz for n in range(len(s)) if len(set(s[n:n+sz])) == sz)
#   return next(n for n in range(sz, len(s)) if len(set(s[n-sz:n])) == sz)

print("1:", solve(4))
print("2:", solve(14))
