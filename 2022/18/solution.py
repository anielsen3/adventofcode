import sys

## parse input
lava = {tuple(map(int, line.split(","))) for line in open(sys.argv[1]).readlines()}

## Part 1
def neighbors(xyz):
    (x, y, z) = xyz
    return {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}

def num_lava_neighbors(xyz):
    return sum(nxyz in lava for nxyz in neighbors(xyz))

print("1:", sum(6 - num_lava_neighbors(xyz) for xyz in lava))

## Part 2
def faces_lava(xyz):
    return any(nxyz in lava for nxyz in neighbors(xyz))

def has_neighbor_facing_lava(xyz):
    return any(faces_lava(nxyz) for nxyz in neighbors(xyz))

def flood(visited, frontier, predicate):
    if not frontier:
        return visited

    nfrontier = { nxyz for xyz in frontier
                       for nxyz in neighbors(xyz) - visited - lava 
                       if predicate(nxyz) }

    return flood(visited|frontier, nfrontier, predicate)

def find_exterior():
    (minx, miny, minz) = min(lava)
    predicate = lambda nxyz: nxyz not in lava and (faces_lava(nxyz) or has_neighbor_facing_lava(nxyz))
    return flood(set(), {(minx-1, miny, minz)}, predicate)

print("2:", sum(num_lava_neighbors(xyz) for xyz in find_exterior()))