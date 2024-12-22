import sys

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

start_pos = next((xy) for xy, c in area.items() if c == '^')
start_direction = (0, -1)

def do_walk(area):
    visits = dict()
    position = start_pos
    direction = start_direction
    while(True):
        if direction in visits.get(position, []):
            return {} # Looped

        visits[position] = visits.get(position, []) + [direction]

        x, y = position
        dx, dy = direction
        next_pos = (x+dx, y+dy)
        next_field = area.get(next_pos, "")

        if next_field in ['.', '^']:
            position = next_pos
        elif next_field == '#':
            direction = (-dy, dx)
        else:
            return visits

visited = do_walk(area)
print("1:", len(visited))

obstacle_placements = [p for p in visited.keys() if not do_walk({**area, **{p: '#'}})]
print("2:", len(obstacle_placements)) 
