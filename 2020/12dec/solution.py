import sys
import re

lines = list(map(str.strip, sys.stdin.readlines()))

def turn_right(facing):
    if (facing == 'N'):
        return 'E'
    if (facing == 'E'):
        return 'S'
    if (facing == 'S'):
        return 'W'
    if (facing == 'W'):
        return 'N'

assert(turn_right('N') == 'E')
assert(turn_right('S') == 'W')

def turn_left(facing):
    res = facing
    for _ in range(3):
        res = turn_right(res)
    return res

assert(turn_left('E') == 'N')
assert(turn_left('S') == 'E')

pos_x = 0
pos_y = 0
facing = 'E'
for line in lines:
    (op, val) = re.match("(.)(\d+)", line).groups()
    
    if op == 'F':
        if facing == 'E':
            pos_x += int(val)
        if facing == 'N':
            pos_y += int(val)
        if facing == 'S':
            pos_y -= int(val)
        if facing == 'W':
            pos_x -= int(val)

    if op == 'E':
        pos_x += int(val)
    if op == 'N':
        pos_y += int(val)
    if op == 'S':
        pos_y -= int(val)
    if op == 'W':
        pos_x -= int(val)

    if op == 'R':
        for _ in range(int(val) // 90):
            facing = turn_right(facing)
    if op == 'L':
        for _ in range(int(val) // 90):
            facing = turn_left(facing)

print(pos_x, pos_y)
print("part1", abs(pos_x) + abs(pos_y))
