import sys
import re

def parse_ints(s):
    return list(map(int, re.findall("\d+", s)))

input_ = open(sys.argv[1]).readlines()
times = parse_ints(input_[0])
distances = parse_ints(input_[1])

# PART 1
def calc_dist(hold_time, max_time):
    return (max_time - hold_time) * hold_time

part1 = 1
for max_time, record_dist in zip(times, distances):
    part1 *= sum(1 for hold_time in range(max_time) if calc_dist(hold_time, max_time) > record_dist)

print("1:", part1)


# PART 2
def solve(max_time, record_dist):
    x1 = 0
    x2 = max_time

    while x1 < x2 - 1:
        mid = (x2 + x1) // 2
        if calc_dist(mid, max_time) > record_dist:
            x2 = mid
        else:
            x1 = mid

    return max_time - (x1 * 2) - 1

time = int("".join(map(str, times)))
dist = int("".join(map(str, distances)))

print("2:", solve(time, dist))
