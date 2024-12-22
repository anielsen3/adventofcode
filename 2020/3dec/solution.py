import sys

from functools import reduce
from operator import mul

I = map(str.strip, sys.stdin.readlines())

def trace(slope):
    (dx, dy) = slope
    num_trees = 0
    x = 0
    y = 0
    while y < len(I):
        if I[y][x % len(I[y])] == "#":
            num_trees += 1
        x += dx
        y += dy
    return num_trees

print("part1", trace((3, 1)))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print("part2", reduce(mul, map(trace, slopes), 1))

