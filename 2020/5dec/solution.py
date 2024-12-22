import sys

I = map(str.strip, sys.stdin.readlines())

def seat_id(line):
    return int(line.translate(line.maketrans("FBLR", "0101")), 2)

seat_ids = set(map(seat_id, I))

print("part1", max(seat_ids))

for i in range(min(seat_ids), max(seat_ids)):
    if not i in seat_ids:
        print("part2", i)
