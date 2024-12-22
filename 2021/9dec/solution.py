import sys

from functools import reduce
from operator import mul
from collections import defaultdict

height = defaultdict(lambda: 10, { (x,y): int(c) for y, line in enumerate(sys.stdin.readlines()) 
                                                 for x, c in enumerate(line.strip()) })

def adjecents(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_minima(xy):
    return all(height[xy] < height[adj_xy] for adj_xy in adjecents(xy))

def lowpoints():
    return (xy for xy in height.keys() if is_minima(xy))

print("part1", sum(height[xy] + 1 for xy in lowpoints()))


def basin(xy):
    return reduce(set.union, 
                 (basin(adj_xy) for adj_xy in adjecents(xy) 
                                if 9 > height[adj_xy] > height[xy]), 
                  set([xy]))

print("part2", reduce(mul, sorted(map(len, map(basin, lowpoints())))[-3:], 1))