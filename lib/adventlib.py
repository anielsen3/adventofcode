import re
import sys

def input():
    return open(sys.argv[1]).readlines()

def input_2d():
    return I = { (x,y): c for y, line in enumerate(input()) 
                          for x, c in enumerate(line.strip()) }

def parse_digits(s):
    return list(map(int, re.findall("\d", s)))

def parse_ints(s):
    return list(map(int, re.findall("-?\d+", s)))

def irange(x, y):
    return range(min(x,y), max(x,y))

def imax(x, y):
    return y if not x else x if not y else max(x, y)

def adjecents4(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def adjecents8(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

def tplus(xy, xy2):
    (x, y) = xy
    (x2, y2) = xy2
    return (x+x2, y+y2)

def tminus(xy, xy2):
    (x, y) = xy
    (x2, y2) = xy2
    return (x2-x, y2-y)

def bfs(adj_function, dist, layers):
    edge = set(nxy for xy in layers[-1] 
                   for nxy in adj_function(xy) if nxy not in dist)

    dist.update({ xy: len(layers) for xy in edge })

    if edge:    
        bfs(adj_function, dist, layers + [edge])

def bfs_distance(start, end, adj_function):
    dist = { start: 0 }
    bfs(adj_function, dist, [{start}])
    return dist[end] if end in dist else 9999
