import sys

from collections import defaultdict
from functools import reduce

I = list(map(str.strip, sys.stdin.readlines()))

def parse_template(t):
    res = defaultdict(lambda: 0)

    for i in range(1, len(t)):
        res[t[i-1] + t[i]] += 1

    return res

template = parse_template(I[0])
rules = { p : i for p, i in (x.split(" -> ") for x in I[2:]) }

def expand(s, _):
    res = defaultdict(lambda: 0)

    for (a,b) in s.keys():
        res[a + rules[a + b]] += s[a + b]
        res[rules[a + b] + b] += s[a + b]

    return res

def count_elems(s):
    cnt = defaultdict(lambda: 0)

    for (a, b) in s:
        cnt[b] += s[a + b]

    return cnt


count = count_elems(reduce(expand, range(10), template))
print("part1", max(count.values()) - min(count.values()))

count = count_elems(reduce(expand, range(40), template))
print("part2", max(count.values()) - min(count.values()))