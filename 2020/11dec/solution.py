import sys

from collections import defaultdict

I = { (x,y): c for y, line in enumerate(sys.stdin.readlines()) 
               for x, c in enumerate(line.strip()) }

def fst_los(xy, dx, dy, max_depth):
    (x, y) = xy
    for _ in range(max_depth):
        x += dx
        y += dy
        if (x, y) in I and I.get((x, y), '.') != '.' :
            return (x, y)

def adjecent_seat(xy, max_depth):
    return (fst_los(xy, dx, dy, max_depth) for dx in [-1, 0, 1]
                                           for dy in [-1, 0, 1] 
                                           if dx != 0 or dy != 0)

def adjecent_seats(xy, i, max_depth):
    return map(lambda xy: i.get(xy), adjecent_seat(xy, max_depth))

def is_occupied(seat):
    return seat == '#'

def is_empty(seat):
    return seat == 'L'

def count_seats(seats, pred):
    return len(list(filter(pred, seats)))

def count_occupied(seats):
    return count_seats(seats, is_occupied)


def step_seat_part1(xy, i):
    seat = i[xy]
    if is_empty(seat) and count_occupied(adjecent_seats(xy, i, 1)) == 0:
        return '#'
    elif is_occupied(seat) and count_occupied(adjecent_seats(xy, i, 1)) >= 4:
        return 'L'
    else:
        return seat

def step_seat_part2(xy, i):
    seat = i[xy]
    if is_empty(seat) and count_occupied(adjecent_seats(xy, i, 999)) == 0:
        return '#'
    elif is_occupied(seat) and count_occupied(adjecent_seats(xy, i, 999)) >= 5:
        return 'L'
    else:
        return seat


def show(i):
    i = defaultdict(lambda: ".", i)
    return "\n".join("".join(i[(x, y)] if (x, y) in i else "." 
                                    for x in range(120)) 
                                    for y in range(30))

def find_stable(step_seat, max_steps = 9999):
    i = I
    for steps in range(max_steps):
        # print(show(i))
        next_i = { xy: step_seat(xy, i) for xy in i }

        if next_i == i:
            return i

        i = next_i

print("part1", count_occupied(find_stable(step_seat_part1).values()))
print("part2", count_occupied(find_stable(step_seat_part2).values()))
