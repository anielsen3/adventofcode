import sys

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def adjecent(xy, direction):
    (x, y) = xy
    (dx, dy) = direction
    return (x + dx, y + dy)

def adjecents(xy):
    return [adjecent(xy, d) for d in directions]

def flood(area, region, layers = []):
    edge = set(nxy for xy in layers[-1] 
                   for nxy in adjecents(xy) if nxy not in region and area.get(nxy, '#') == area[xy])

    region |= edge

    if edge:    
        flood(area, region, layers + [edge])

    return region

def partition(area):
    regions = [] 

    for xy in area:
        if not any(xy in region for region in regions):
            regions += [flood(area, set([xy]), [[xy]])]

    return regions

def num_edges(xy):
    return sum(area.get(nxy, '#') != area[xy] for nxy in adjecents(xy))

def perimeter(region):
    return sum(num_edges(xy) for xy in region)

print("1", sum(perimeter(region)*len(region) for region in partition(area)))

# part 2

def find_neighbors(region, direction):
    return { xy: 1 for xy in region if adjecent(xy, direction) not in region }

def num_sides(region):
    return sum(len(partition(find_neighbors(region, d))) for d in directions)

print("2", sum(num_sides(region)*len(region) for region in partition(area)))