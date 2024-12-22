import sys
from itertools import permutations

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

antennas = {}
for xy, c in area.items():
    if c != '.':
        antennas[c] = antennas.get(c, []) + [xy]

def find_antinodes(steps_away_from_xy1):
    antinodes = set()
    for c in antennas:
        for ((x1, y1), (x2, y2)) in permutations(antennas[c], 2):
            for step in steps_away_from_xy1:
                antinodes.add((x1 + (x2-x1) * step, y1 + (y2-y1) * step))                

    return antinodes & area.keys()

print("1:", len(find_antinodes([-1, 2])))        # 280
print("2:", len(find_antinodes(range(-99, 99)))) # 958
