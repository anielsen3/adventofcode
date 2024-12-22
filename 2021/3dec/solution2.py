import sys

from string import maketrans 

lines = map(str.strip, sys.stdin.readlines())

def filter_by_bit(bit, pos, lines):
    return filter(lambda l: l[pos] == bit, lines)

def invert(s):
    return s.translate(maketrans("01", "10"))

# Part 1 
res = ""
for i in range(len(lines[0])):
    lines_with_1 = filter_by_bit('1', i, lines)
    lines_with_0 = filter_by_bit('0', i, lines)
    if len(lines_with_1) >= len(lines_with_0):
        res += '1'
    else:
        res += '0'

print("Part 1:")
print(res, invert(res))
print(int(res, 2), int(invert(res), 2), int(res, 2) * int(invert(res), 2))

# Part 2
res1 = lines
for i in range(len(lines[0])):
    lines_with_1 = filter_by_bit('1', i, res1)
    lines_with_0 = filter_by_bit('0', i, res1)
    if len(lines_with_1) >= len(lines_with_0):
        res1 = lines_with_1
    else:
        res1 = lines_with_0

    if len(res1) == 1:
        break

res0 = lines
for i in range(len(lines[0])):
    lines_with_1 = filter_by_bit('1', i, res0)
    lines_with_0 = filter_by_bit('0', i, res0)
    if (len(lines_with_1) >= len(lines_with_0)):
        res0 = lines_with_0
    else:
        res0 = lines_with_1

    if len(res0) == 1:
        break

print("Part 2:")
print(res1, res0)
print(int(res1[0], 2), int(res0[0], 2), int(res1[0], 2) * int(res0[0], 2))
