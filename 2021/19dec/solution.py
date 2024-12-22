import sys
import re
import math

I = map(str.strip, sys.stdin.readlines())

i = 0
scanners = [[]]
for line in I:
    if not line:
        i += 1
        scanners.append(list())

    if re.match("-?\d+,-?\d+,-?\d+", line):
        (x, y, z) = re.match("(-?\d+),(-?\d+),(-?\d+)", line).groups()
        scanners[i] += [(int(x), int(y), int(z))]

def dist(xyz1, xyz2):
    (x1, y1, z1) = xyz1
    (x2, y2, z2) = xyz2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) 

def distances(xyz, to_list):
    return (dist(xyz, to_xyz)
            for to_xyz in to_list)

beacons = {}
for scanner in scanners:            
    for beacon in scanner:
        dists = sorted(distances(beacon, scanner))
        beacons[tuple(dists[1:3])] = beacon

def manh_dist(xyz1, xyz2):
    (x1, y1, z1) = xyz1
    (x2, y2, z2) = xyz2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

print("part1", len(beacons))

max_dist = 0
for scanner in scanners:
    for b1 in scanner:
        for b2 in scanner:
            max_dist = max(max_dist, manh_dist(b1, b2))

print("part2", max_dist) 
