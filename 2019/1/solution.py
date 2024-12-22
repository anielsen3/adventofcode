import sys

def read_input():
    return open(sys.argv[1]).readlines()

def fuel_cost(n):
    return int(n) // 3 - 2

def part1():
    return sum(fuel_cost(n) for n in read_input())

print("1", part1())

def part2():
    sum = 0

    for n in read_input():
        cost = 0
    
        while (d := fuel_cost(n)) > 0:
            cost += d
            n = d

        sum += cost

    return sum

print("2", part2())
    
