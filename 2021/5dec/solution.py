import sys
import re

input_ = list(map(str.strip, sys.stdin))
map = {}

def mark_map(x,y):
    print("mark_map", x, y)
    coord = str(x) + "," + str(y)
    if (coord in map):
        map[coord] += 1
    else:
        map[coord] = 1

def get_stepx(p1x, p2x):
    if (p1x > p2x):
        return -1
    else:
        return 1

def get_stepy(p1y, p2y):
    if (p1y > p2y):
        return -1
    else:                
        return 1

def mark_vent(p1x, p2x, stepx, p1y, p2y, stepy):
    print("mark_vent", p1x, p2x, stepx, p1y, p2y, stepy)
    curx = p1x
    cury = p1y
    while (curx != p2x or cury != p2y):
        mark_map(curx, cury)
        curx += stepx
        cury += stepy
    mark_map(curx, cury)

def read_vent(p1, p2):
    print("read_vent", p1, p2)
    (p1x, p1y) = p1.split(",")
    (p2x, p2y) = p2.split(",")

    p1x = int(p1x)
    p1y = int(p1y)
    p2x = int(p2x)
    p2y = int(p2y)

    stepx = 0
    stepy = 0
    if (p1x == p2x):
        stepy = get_stepy(p1y, p2y)
    elif (p1y == p2y):
        stepx = get_stepx(p1x, p2x)
    elif abs(p1x-p2x) == abs(p1y-p2y):
        stepy = get_stepy(p1y, p2y)
        stepx = get_stepx(p1x, p2x)
    else:
        return

    mark_vent(p1x, p2x, stepx, p1y, p2y, stepy)

# read input
for row in input_:
    (p1, p2) = row.split(" -> ")
    read_vent(p1, p2)

# find output
cnt = 0
for item in map.items():
    print(item)
    if (item[1] >= 2):
        cnt += 1

print(cnt)