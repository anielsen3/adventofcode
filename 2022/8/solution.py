from itertools import takewhile
import math
import sys

forest = { (x, y): int(h) for y, line in enumerate(open(sys.argv[1]).readlines())
                          for x, h    in enumerate(line.rstrip()) }

max_x = max(x for (x, _) in forest)
max_y = max(y for (_, y) in forest)

def lines_of_sight(xy):
    (x, y) = xy
    return [[(nx, y) for nx in reversed(range(0, x))],
            [(nx, y) for nx in range(x+1, max_x+1)],
            [(x, ny) for ny in reversed(range(0, y))],
            [(x, ny) for ny in range(y+1, max_y+1)]]

def is_tallest(xy, los):
    return forest[xy] > max(forest[xy2] for xy2 in los) if los else True

def is_visible_from_edge(xy):
    return any(is_tallest(xy, los) for los in lines_of_sight(xy))

print("1:", len(list(filter(is_visible_from_edge, forest))))


def viewing_distance(xy, los):
    return min(len(list(takewhile(lambda xy2: forest[xy] > forest[xy2], los))) + 1, len(los))

def scenic_score(xy):
    return math.prod(viewing_distance(xy, los) for los in lines_of_sight(xy)) 

print("2:", max(map(scenic_score, forest)))