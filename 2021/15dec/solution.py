import sys
import math
import heapq

from collections import defaultdict
from functools import reduce


C = { (x, y) : int(d) for y, line in enumerate(sys.stdin.readlines()) 
                      for x, d in enumerate(line.strip()) }

def neighbors(xy):
    (x, y) = xy
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def x_size(c):
    return max(map(lambda key: key[0], c.keys())) + 1

def y_size(c):
    return max(map(lambda key: key[1], c.keys())) + 1

def traverse_cost(start, end, c):
    cost = { start: 0 }

    active = [(0, start)]
    heapq.heapify(active)

    while active:
        (_, current) = heapq.heappop(active)

        if current == end:
            return cost[current]

        for xy in neighbors(current):
            if xy in c:
                n_cost = cost.get(current, 0) + c[xy]
                if n_cost < cost.get(xy, math.inf):
                    cost[xy] = n_cost
                    heapq.heappush(active, (n_cost, xy))

c1 = C
start = (0, 0)
end   = (x_size(c1)-1, y_size(c1)-1)

print("part1", traverse_cost(start, end,C))

def inc(d, n):
    return d + 1 if d < 9 else 1

def tile_map(c, n):
    c2 = dict()

    x_sz = x_size(c)
    y_sz = y_size(c)
    for x, y in c:
        for dx in range(n):
            for dy in range(n):
                c2[(dx * x_sz + x, dy * y_sz + y)] = reduce(inc, range(dx+dy), c[(x,y)])

    return c2

c2 = tile_map(C, 5)
start = (0, 0)
end   = (x_size(c2)-1, y_size(c2)-1)

print("part2", traverse_cost(start, end, c2))
