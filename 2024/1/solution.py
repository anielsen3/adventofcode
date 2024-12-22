import sys
import re

def input():
    return open(sys.argv[1]).readlines()

def ints(s):
    return map(int, re.findall("-?\\d+", s))

(xs, ys) = zip(*(map(ints, input())))

print("1: ", sum(abs(y - x) for (x, y) in zip(sorted(xs), sorted(ys)))) # 2164381
print("2: ", sum(x * len(list(y for y in ys if y == x)) for x in xs)) # 20719933