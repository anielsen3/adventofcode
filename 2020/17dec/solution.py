import sys

from functools import reduce

C = { (x, y, 0) : c for y, line in enumerate(sys.stdin.readlines()) 
                    for x, c in enumerate(line.strip()) }
C2 = { (x, y, z, 0) : C[(x, y, z)] for x, y, z in C.keys() }

def neighbors(xyz):
    (x, y, z) = xyz

    return list((x+dx, y+dy, z+dz) for dx in [-1, 0, 1]
                                   for dy in [-1, 0, 1]
                                   for dz in [-1, 0, 1]
                                   if not dz == dy == dx == 0)

def neighbors2(xyzw):
    (x, y, z, w) = xyzw

    return list((x+dx, y+dy, z+dz, w+dw) for dx in [-1, 0, 1]
                                       for dy in [-1, 0, 1]
                                       for dz in [-1, 0, 1]
                                       for dw in [-1, 0, 1]
                                       if not dz == dy == dx == dw == 0)

def isactive(xyz, c):
    return c.get(xyz, '.') == '#'

def count_active(xyzs, c):
    return len(list(filter(lambda xyz: isactive(xyz, c), xyzs)))

def next_state_pt(pt, c, neighbor_fun):
    if isactive(pt, c):
        if count_active(neighbor_fun(pt), c) in [2,3]:
            return '#'
        else:
            return '.'
    else:
        if count_active(neighbor_fun(pt), c) == 3:
            return '#'
        else:
            return '.'

def next_state(c, neighbor_fun):
    nc = {}

    pts = set()
    for xyz in c:
        for pt in neighbor_fun(xyz) + [xyz]:
            pts.add(pt)
    
    for pt in pts:            
        nc[pt] = next_state_pt(pt, c, neighbor_fun)

    return nc

c1 = C
for _ in range(6):
    c1 = next_state(c1, neighbors) 
print("part1", count_active(c1.keys(), c1))

c2 = C2
for _ in range(6):
    c2 = next_state(c2, neighbors2) 
print("part2", count_active(c2.keys(), c2))
