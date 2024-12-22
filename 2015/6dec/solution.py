import sys
import re

from collections import defaultdict

I = list(map(str.strip, sys.stdin.readlines()))

def do_ins1(XY, ins, xy):
    if ins == 'turn on':
        XY[xy] = 1
    elif ins == 'turn off':
        XY[xy] = 0
    elif ins == 'toggle':
        XY[xy] = abs(XY[xy] - 1)

def do_ins2(XY, ins, xy):
    if ins == 'turn on':
        XY[xy] += 1
    elif ins == 'turn off':
        XY[xy] = max(0, XY[xy]-1)
    elif ins == 'toggle':
        XY[xy] += 2

def exec(ins_fun):
    XY = defaultdict(lambda: 0)

    for line in I:
        ins, x1, y1, x2, y2 = re.match("(toggle|turn off|turn on) (\\d+),(\\d+) through (\\d+),(\\d+)", line).groups()
        for x in range(int(x1), int(x2)+1):
            for y in range(int(y1), int(y2)+1):
                ins_fun(XY, ins, (x, y))

    return XY

print("part1", sum(exec(do_ins1).values()))
print("part2", sum(exec(do_ins2).values()))

