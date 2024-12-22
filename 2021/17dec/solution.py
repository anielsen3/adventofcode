import sys
import re 

(t_xrange, t_yrange) = re.match("target area: x=(.*), y=(.*)", sys.stdin.readline()).groups()
(from_x, to_x) = re.match("(.*)\.\.(.*)", t_xrange).groups()
(from_y, to_y) = re.match("(.*)\.\.(.*)", t_yrange).groups()

from_x = int(from_x)
to_x   = int(to_x)
from_y = int(from_y)
to_y   = int(to_y)

assert from_y < to_y 
assert from_x < to_x

def in_target(xy):
    (x, y) = xy
    return from_x <= x <= to_x and from_y <= y <= to_y

def trace_path(dx, dy):
    max_y = 0
    x = 0
    y = 0

    while True:
        # step
        x += dx
        y += dy

        if (dx > 0):
            dx -= 1
        elif (dx < 0):
            dx += 1

        dy -= 1

        if y > max_y:
            max_y = y

        # stopping conditions
        if (in_target((x, y))):
            return (True, max_y)

        if y < from_y < to_y and dy <= 0:
            return (False, max_y)

        if dx == 0 and (x < from_x or x > to_x):
            return (False, max_y) 


hits = 0
all_time_max_y = 0
for dx in range(0, to_x*2):
    for dy in range(-200, 200):
        (hit, max_y) = trace_path(dx, dy)
        if hit:
            if (all_time_max_y < max_y):
                all_time_max_y = max_y
            hits += 1



print("part1", all_time_max_y)
print("part2", hits)
