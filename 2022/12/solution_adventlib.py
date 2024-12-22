import sys
from lib.adventlib import *

I = { (x,y): c for y, line in enumerate(open(sys.argv[1]).readlines()) 
               for x, c in enumerate(line.strip()) }

def adjecents(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_possible_move(xy, nxy):
    return ord(I[nxy].replace("E", 'z')) - ord(I[xy].replace("S", "a")) <= 1 if nxy in I else False

def possible_adjecents(xy):
    return (nxy for nxy in adjecents(xy) if is_possible_move(xy, nxy))

def find_all(values):
    return (xy for (xy, v) in I.items() if v in values)

def find(value):
    return next(find_all(value))

def distance(start, end):
    return bfs_distance(start, end, possible_adjecents)

print("1:", distance(find("S"), find("E")))
print("2:", min(distance(start, find("E")) for start in find_all(['a', 'S'])))        