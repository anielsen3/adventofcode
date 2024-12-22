import sys

input = open(sys.argv[1]).readlines()
empty_line = next(i for i in range(len(input)) if input[i] == '\n')

area = { (x, y): c for y, l in enumerate(input[:empty_line]) 
                   for x, c in enumerate(l.strip()) }
moves = "".join(map(str.strip, input[empty_line+1:]))
robot = next(xy for xy in area if area[xy] == '@')

print(area)
print(moves)
print(robot)

def direction(move):
    if move == '^':
        return (0, -1)
    if move == '>':
        return (1, 0)
    if move == 'v':
        return (0, 1)
    if move == '<':
        return (-1, 0)

def find_first_empty(xy, dxy):
    (dx, dy) = dxy
    while True:
        (x, y) = xy
        xy = (x + dx, y + dy)
        if area[xy] == '#':
            return None
        if area[xy] == '.':
            return xy
        # if area[txy] == 'O':
        #     # do nothing
        #     pass    

def print_area(area):
    for y in range(max(y for x, y in area)+1):
        line = ""
        for x in range(max(x for x, y in area)+1):
            line += area[(x, y)]
        print(line)

for move in moves:
    # print(move)
    # print_area(area)
    dxy = direction(move)
    first_empty = find_first_empty(robot, dxy)
    # print(robot, first_empty)
    if first_empty:
        (rx, ry) = robot
        (dx, dy) = dxy
        one_step = (rx + dx, ry + dy)
        area[robot] = '.'
        if first_empty != one_step:
            area[first_empty] = area[one_step]
        area[one_step] = '@'
        robot = one_step

print("1", sum(x + y*100 for x,y in area if area[(x,y)] == 'O'))