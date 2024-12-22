import sys
import re

def ints(s):
    return list(map(int, re.findall("-?\\d+", s)))

robots = list(map(ints, open(sys.argv[1]).readlines()))
# sz_x = 11
# sz_y = 7
sz_x = 101
sz_y = 103

def get_state(steps):
    state = {}
    for (x, y, dx, dy) in robots:
        x = (x + dx * steps) % sz_x
        y = (y + dy * steps) % sz_y
        state[(x, y)] = state.get((x, y), 0) + 1 
    return state

def score_state(state):
    score = 1
    for quadrant in range(4):
        x_half = quadrant % 2
        y_half = quadrant // 2
        half_szx = int((sz_x-1)//2)
        start_x = (half_szx+1)*x_half
        xs = range(start_x, start_x+half_szx) 
        half_szy = int((sz_y-1)//2)
        start_y = (half_szy+1) * y_half
        ys = range(start_y, start_y+half_szy) 

        score_quad = 0
        for ty in ys:
            for tx in xs:
                score_quad += state.get((tx, ty), 0)

        score *= score_quad

    return score

print("1", score_state(get_state(100)))

# Part 2

def print_robots(state):
    for ty in range(sz_y):
        line = ""
        for tx in range(sz_x):
            count = state.get((tx, ty), 0)
            line += str(count) if count else "."

        print(line)

def cohesion_score(step, state):
    score = 0

    for ((x, y), count) in state.items():
        if 20 < x < sz_x - 20 and 20 < y < sz_y - 20:
            score += count

    return score

p2_step = next(s for s in range(10000) if cohesion_score(s, get_state(s)) > 300)
print("2", p2_step)

print_robots(get_state(p2_step))