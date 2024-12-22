import sys
import re
import functools
from collections import defaultdict

I = open(sys.argv[1]).readlines()

@functools.cache
def eval(lhs, part):
    v1, op, v3 = re.match("(\\S+)?(AND|LSHIFT|RSHIFT|OR|NOT)? ?(.*)", lhs).groups()
    if v1 == 'NOT':
        return 65536 + ~eval(v3, part)
    elif op == 'OR':
        return eval(v1, part) | eval(v3, part)
    elif op == 'AND':
        return eval(v1, part) & eval(v3, part)
    elif op == 'RSHIFT':
        return eval(v1, part) >> int(v3)
    elif op == 'LSHIFT':
        return eval(v1, part) << int(v3)
    elif not op:
        if v3.isnumeric():
            return int(v3)
        else:
            return eval(reg[v3], part)

reg = dict()
for line in reversed(I):
    lhs, rhs = line.strip().split(" -> ")
    reg[rhs] = lhs

print("1", eval(reg.get('a', '0'), 1))

reg['b'] = '3176'
print("2", eval(reg.get('a', '0'), 2))
