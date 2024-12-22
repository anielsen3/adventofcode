import sys
from itertools import permutations

input = [*map(str.strip, open(sys.argv[1]).readlines())]

map_ = dict()
for l in input:
    lhs, rhs  = l.split(" = ")
    from_, to = lhs.split(" to ")
    map_[(from_, to)] = map_[(to, from_)] = int(rhs)

def length(route):
    return sum(map_[(from_, to)] for from_, to in zip(route, route[1:]))

cities = set(f for f, _ in map_.keys())
print("1:", min(length(route) for route in permutations(cities)))
print("2:", max(length(route) for route in permutations(cities)))