import sys
import re
from z3 import *
from collections import defaultdict

def create_line_segment(sx, sy, y, dist):
    dx = dist - abs(sy - y)
    return [sx - dx, sx + dx]

def coalesce(line_segment):
    line_segment.sort(key=lambda r: r[0])

    res = []
    cur = line_segment[0]
    for r in line_segment[1:]:
        if r[0] <= cur[1]:
            cur = [cur[0], max(cur[1], r[1])]
        else:
            res.append(cur)
            cur = r
    
    res.append(cur)
    return res

def read_line_segments(fixed_y = None):
    line_segments = defaultdict(lambda: [])
    for line in open(sys.argv[1]).readlines():
        (sx, sy, bx, by) = map(int, re.findall("-?\d+", line))
        dist = abs(sx - bx) + abs(sy - by)
        for y in range(sy - dist, sy + dist) if not fixed_y else [fixed_y]:
            line_segments[y].append(create_line_segment(sx, sy, y, dist))

    return line_segments


print("1:", sum(v[1] - v[0] for v in coalesce(read_line_segments(2000000)[2000000])))

# line_segments = read_line_segments()
# for y in line_segments:
#     ls = coalesce(line_segments[y])
#     if len(ls) > 1:
#         x = ls[0][1] + 1
#         print("2:", x * 4000000 + y)
#         break

# PART 2 with Z3
def z3abs(x):
    return If(x >= 0, x, -x)

s = Solver()
x = Int('x')
y = Int('y')
s.add(0 <= x)
s.add(x <= 4000000)
s.add(0 <= y)
s.add(y <= 4000000)
for line in open(sys.argv[1]).readlines():
    (sx, sy, bx, by) = map(int, re.findall("-?\d+", line))
    s.add(z3abs(x - sx) + z3abs(y - sy) > z3abs(sx - bx) + z3abs(sy - by))

s.check()
m = s.model()
print(f"2: x={m[x].as_long()} y={m[y].as_long()} freq={m[x].as_long() * 4000000 + m[y].as_long()}")
