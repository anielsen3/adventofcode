import sys

def mix(numbers, n_times=1):
    result = numbers.copy()

    for _ in range(n_times):
        for (orig_pos, value) in numbers:
            idx = next(i for i, (p, _) in enumerate(result) if p == orig_pos)
            result.pop(idx)
            result.insert((idx + value) % len(result) or len(result), (orig_pos, value))

    return result

def grove_coords(numbers):
    idx_0 = [v for (_, v) in numbers].index(0)
    return sum(numbers[(idx_0 + n) % len(numbers)][1] for n in (1000, 2000, 3000)) 

def part1_input():
    return list(enumerate(map(int, open(sys.argv[1]).readlines())))

print("1:", grove_coords(mix(part1_input())))

def part2_input():
    return [(i, v*811589153) for (i, v) in part1_input()]

print("2:", grove_coords(mix(part2_input(), 10)))