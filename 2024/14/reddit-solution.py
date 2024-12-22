import sys
from copy import deepcopy
from math import prod
from collections import defaultdict
import re
snre = re.compile(r'(-?\d+)')

L = sys.stdin.read().strip().split('\n')
PP = {}
V = {}
R = 103
C = 101
HR = 51
HC = 50

def CountSectors(P):
    cnw = cne = cse = csw = 0
    for px, py in P.values():
        #    continue
        if 0 <= px < HC and 0 <= py < HR:
            cnw += 1
        elif 0 <= px < HC and HR < py < R:
            csw += 1
        elif HC < px <= C and 0 <= py < HR:
            cne += 1
        elif HC < px <= C and HR < py < R:
            cse += 1
    return (cnw, cne, cse, csw)

def PrintGrid(G):
    for y in range(R):
        for x in range(C):
            print(G[(x,y)], end='')
        print()
    print()

for r, l in enumerate(L):
    nums = list(map(int, snre.findall(l)))
    PP[r] = (nums[0], nums[1])
    V[r] = (nums[2], nums[3])

P = deepcopy(PP)
for r in P.keys():
    px, py = P[r]
    vx, vy = V[r]
    px = (px + 100 * vx) % C
    py = (py + 100 * vy) % R
    P[r] = (px, py)

print(prod(CountSectors(P)))

n = 0
P = deepcopy(PP)
while True:
    n += 1
    G = defaultdict(lambda:' ')
    for r in P.keys():
        px, py = P[r]
        vx, vy = V[r]
        px = (px + vx) % C
        py = (py + vy) % R

        P[r] = (px, py)
        G[(px,py)] = '#'

    if any(x > 300 for x in CountSectors(P)):
        PrintGrid(G)
        print(n)
        break