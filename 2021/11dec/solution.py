import sys

I = { (x,y): int(c) for y, line in enumerate(sys.stdin.readlines()) 
                    for x, c in enumerate(line.strip()) }

def in_bounds(xy):
    (x, y) = xy
    return x >= 0 and x < 10 and y >= 0 and y < 10    

def neighbours(xy):
    (x, y) = xy
    n = [(x-1, y-1), (x, y-1), (x+1, y-1),
         (x-1, y), (x+1, y),
         (x-1, y+1), (x, y+1), (x+1, y+1)]
    return filter(in_bounds, n)

assert (set(neighbours((0, 0))) == set([(0, 1), (1, 0), (1, 1)]))
assert (set(neighbours((1, 1))) == set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]))
assert (set(neighbours((9, 9))) == set([(8, 8), (8, 9), (9, 8)]))

def do_flashes(visited = set()):
    flashes = filter(lambda xy: I[xy] > 9 and xy not in visited, I)

    if not flashes:
        return

    for xy in flashes:
        for nb_xy in neighbours(xy):
            I[nb_xy] += 1

    do_flashes(visited.union(set(flashes)))


num_flashes = 0
for step in range(1000):
    for xy in I:
        I[xy] += 1

    do_flashes()

    for xy in filter(lambda xy: I[xy] > 9, I):
        num_flashes += 1
        I[xy] = 0

    if (step == 99):
        print("part1", num_flashes)

    if sum(I[xy] for xy in I) == 0:
        print("part2", step + 1)
        break
