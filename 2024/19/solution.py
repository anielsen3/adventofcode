import sys
from functools import cache

input = [*map(str.strip, open(sys.argv[1]).readlines())]
patterns = input[0].split(", ")
designs = input[2:]

@cache
def count_combos(d):
    return sum(count_combos(d[len(p):]) for p in patterns if d.startswith(p)) if d else 1

cs = [count_combos(d) for d in designs]
print("1:", len([c for c in cs if c]))
print("2:", sum(cs))