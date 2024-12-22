import sys
import re

from functools import cache

I = [re.match("(.*) x=(.+)\.\.(.+),y=(.+)\.\.(.+),z=(.+)\.\.(.+)", l).groups() for l in sys.stdin.readlines()]

def do_range(f, t, min_v, max_v):
    return range(max(int(f), min_v), min(int(t), max_v)+1)

def do_part1():
    c = set()
    for cmd, xfrom, xto, yfrom, yto, zfrom, zto in I:        
        for x in do_range(xfrom, xto, -50, 50):
            for y in do_range(yfrom, yto, -50, 50):
                for z in do_range(zfrom, zto, -50, 50):
                    xyz = (x, y, z)
                    if (cmd == 'on'):
                        c.add(xyz)
                    elif xyz in c:
                        c.remove(xyz)
    
    return len(c)

print("part1", do_part1())

def overlap_seg(seg1, seg2):
    (_, min_to), (max_from, max_to) = sorted((seg1, seg2))
    if min_to >= max_from:
        return (max_from, min(min_to, max_to))

@cache
def intersect(cube1, cube2):
    return (overlap_seg(cube1[0], cube2[0]), 
            overlap_seg(cube1[1], cube2[1]), 
            overlap_seg(cube1[2], cube2[2]))

def new_cubes(new_cmd_cube, cubes):
    new_cmd, new_cube = new_cmd_cube
    
    new_cubes = []
    for old_cmd, old_cube in cubes:
        if all(intersection := intersect(old_cube, new_cube)):
            new_cubes.append(('on' if old_cmd == 'off' else 'off', intersection))

    if (new_cmd == 'on'):
        new_cubes.append((new_cmd, new_cube))

    return new_cubes

def read_line(line):
    (cmd, *coords) = line
    (xfrom, xto, yfrom, yto, zfrom, zto) = map(int, coords)
    return (cmd, ((xfrom, xto), (yfrom, yto), (zfrom, zto)))

def calc_cubes():
    cubes = []
    for line in I:        
        cubes += new_cubes(read_line(line), cubes)
    
    return cubes

def volume(cube):
    ((x1, x2), (y1, y2), (z1, z2)) = cube
    return abs(x2 - x1 + 1) * abs(y2 - y1 + 1) * abs(z2 - z1 + 1)

print("part2", sum(volume(cube) if cmd == 'on' else -volume(cube) for cmd, cube in calc_cubes()))