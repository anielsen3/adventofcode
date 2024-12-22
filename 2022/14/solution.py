import sys

def parse_cave():
    cave = {}

    for line in open(sys.argv[1]).readlines():
        coords = line.split(" -> ")
        for f, t in zip(coords[0::], coords[1::]):
            (fx, fy) = (int(n) for n in f.split(","))
            (tx, ty) = (int(n) for n in t.split(","))

            for x in range(min(fx, tx), max(fx, tx) + 1):
                cave[x, fy] = "#"

            for y in range(min(fy, ty), max(fy, ty) + 1):
                cave[fx, y] = "#"
                
    return cave

def bottom(cave):
    return max(y for (_, y), val in cave.items() if val == '#')

def drop_sand(cave):
    x = 500
    
    for y in range(bottom(cave)):
        if (x, y + 1) not in cave:
            pass
        elif (x - 1, y + 1) not in cave:
            x -= 1
        elif (x + 1, y + 1) not in cave:
            x += 1 
        else:
            cave[(x, y)] = "o"
            return (x, y) != (500, 0)
    
    return False

def add_floor(cave):
    bottom_y = bottom(cave)
    for x in range(-1000, 1000):
        cave[x, bottom_y + 2] = "#"

def do_simulation(bottom_is_abyss):
    cave = parse_cave()

    if not bottom_is_abyss:
        add_floor(cave)

    while drop_sand(cave):
        pass

    return cave

print("1:", sum(1 for v in do_simulation(True).values() if v == 'o'))
print("2:", sum(1 for v in do_simulation(False).values() if v == 'o'))


