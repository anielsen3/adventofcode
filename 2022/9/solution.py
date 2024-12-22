import sys

def sign(x):
    return (x > 0) - (x < 0) # True = 1, False = 0

def move_tail_element(e1, e2):
    xdelta = e1[0] - e2[0]
    ydelta = e1[1] - e2[1]
    if abs(xdelta) > 1 or abs(ydelta) > 1:
        e2[0] += sign(xdelta)
        e2[1] += sign(ydelta)

def move_head(h, dir):
    h[0] += 1 if dir == 'R' else -1 if dir == 'L' else 0
    h[1] += 1 if dir == 'D' else -1 if dir == 'U' else 0

def move(rope, direction):
    move_head(rope[0], direction) # move head

    for i in range(1, len(rope)): # move tail
        move_tail_element(rope[i-1], rope[i])

    return tuple(rope[-1]) # return position of rope end

def simulate(rope):
    return { move(rope, direction) for direction, num in (line.split() for line in open(sys.argv[1])) 
                                   for _ in range(int(num)) }

print("1:", len(simulate([[0, 0] for n in range(2)])))
print("2:", len(simulate([[0, 0] for n in range(10)])))

# def visualize(hist):
#     # print("vis", hist)
#     min_x = min(x for (x, _) in hist)
#     max_x = max(x for (x, _) in hist)
#     min_y = min(y for (_, y) in hist)
#     max_y = max(y for (_, y) in hist)
#     str = ""
#     for y in range(min_y, max_y+1):
#         for x in range(min_x, max_x+1):
#             str += "s" if (x, y) == (0, 0) else "#" if (x,y) in hist else  "."
#         str += "\n"

#     return str

# hist = simulate(rope1)
# print("1:", len(hist))
# print(visualize(hist))

# hist = simulate(rope2)
# print("2:", len(hist))
# print(visualize(hist))
