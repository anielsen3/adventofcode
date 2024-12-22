import sys

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def find_trails(xy, trail):
    if area[xy] == '9':
        return [trail]
    else:
        trails = []
        for d in directions:
            n_xy = (xy[0] + d[0], xy[1] + d[1])
            if int(area.get(n_xy, 0)) - int(area.get(xy)) == 1:
                trails += find_trails(n_xy, trail + [n_xy])
        return trails

trailheads = [xy for xy in area if area[xy] == '0']

# count reachable peaks by counting unique last positions in trails
print("1:", sum(len(set(trail[-1] for trail in find_trails(xy, []))) 
                                  for xy in trailheads))
print("2:", sum(len(find_trails(xy, [])) for xy in trailheads))