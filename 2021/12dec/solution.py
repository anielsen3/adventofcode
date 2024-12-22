import sys

from collections import defaultdict, Counter
from functools import reduce

G = defaultdict(lambda: list(), {})
for line in sys.stdin.readlines():
    (l, r) = line.strip().split("-")
    if l != 'end' and r != 'start': G[l].append(r)
    if r != 'end' and l != 'start': G[r].append(l)

def pred_part1(n, path):
    return n.isupper() or n not in path 

def pred_part2(n, path):
    return pred_part1(n,path) or max(Counter(filter(str.islower, path)).values()) == 1

def paths(current, path, pred):
    if current == 'end': 
        return [path]

    res = []
    for x in G[current]:
        if pred(x, path):
            res += paths(x, path + [x], pred)

    return res

print("part1", len(paths("start", [], pred_part1)))
print("part2", len(paths("start", [], pred_part2)))
