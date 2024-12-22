import sys
import re
import math
from functools import reduce
from itertools import cycle

input_ = open(sys.argv[1]).readlines()
instructions = input_[0].strip()
nodes = {m[0]: tuple(m[1:]) for m in (re.findall("\w+", l) for l in input_[2:])}

def num_steps(pos, end_pred):
    for i, inst in enumerate(cycle(instructions), 1):
        pos = nodes[pos][0 if inst == 'L' else 1]
        if end_pred(pos):
            return i

def lcm(a, b):
    return a * b // math.gcd(a, b)

print("1:", num_steps('AAA', lambda p: p == 'ZZZ'))
print("2:", reduce(lcm, (num_steps(p, lambda p: p.endswith('Z')) for p in nodes.keys() if p.endswith('A'))))