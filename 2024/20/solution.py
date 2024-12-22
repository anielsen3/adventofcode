import sys

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

def moves(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_ok(area, xy):
    (x, y) = xy
    return xy in area and area[xy] != '#'

def bfs(area, dist, layers):
    while edge := set(nxy for xy in layers[-1] 
                          for nxy in moves(xy) if is_ok(area, nxy) and nxy not in dist):
        dist.update({ xy: len(layers) for xy in edge })
        layers += [edge]

    return dist

S = next(xy for xy in area if area[xy] == 'S')
E = next(xy for xy in area if area[xy] == 'E')

def distance(area):
    return bfs(area, { S: 0 }, [{S}]).get(E, 999999)

def show_area(area):
    sz_x = max(x for (x, y) in area)
    sz_y = max(y for (x, y) in area)

    for y in range(sz_y+1):
        line = ""
        for x in range(sz_x+1):
            line += area[(x, y)]

        print(line)            

dist_map = bfs(area, { E: 0 }, [{E}])

def distance_upto(xy, distance):
    (x, y) = xy
    for dx in range(distance+1):
        for dy in range(distance-dx+1):
            yield (x + dx, y + dy)
            yield (x - dx, y + dy)
            yield (x + dx, y - dy)
            yield (x - dx, y - dy)


def count_savings(threshold, picosecs):
    count = 0
    for xy in dist_map:
        for nxy in set(distance_upto(xy, picosecs)):
            if nxy in dist_map:
                distance_to_nxy = picosecs # forkert
                if (dist_map[xy] - dist_map[nxy] - distance_to_nxy) >= threshold:
                    count += 1
    return count

print("74, 20", count_savings(74, 20)) # forvent 7 med test-input
print("76, 20", count_savings(76, 20)) # forvent 3 med test-input

print("1:", count_savings(100, 2)) 
print("2:", count_savings(100, 20)) # 1052680 wrong, 980322 wrong
