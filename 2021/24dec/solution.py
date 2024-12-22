import sys
import re

reg = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

input = (int(c) for c in INPUT)

def readb(b):
    return int(b) if b[0] == '-' or b.isnumeric() else reg[b] 

for line in sys.stdin.readlines():
    (cmd, a, b) = re.match("^(\w+) (\S) ?(\S+)?", line).groups()

    if cmd == 'inp':
        reg[a] = next(input)
    elif cmd == 'add':
        reg[a] += readb(b)
    elif cmd == 'mul':
        reg[a] *= readb(b)
    elif cmd == 'div':
        reg[a] //= readb(b)
    elif cmd == 'mod':
        reg[a] %= readb(b)
    elif cmd == 'eql':
        reg[a] = 1 if reg[a] == readb(b) else 0

    # print(cmd, a, b, "- regs:", reg)

print(regs)