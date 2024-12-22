import sys

input_ = map(int, sys.stdin.readline().split(","))

def sum_cost(cost_closure):
    return sum(map(cost_closure, input_))

def min_sum_cost(cost_fun):
    return min((sum_cost(lambda x: cost_fun(x, i)), i) for i in range(max(input_)))

def part1_cost(x, goal):
    return abs(x-goal)

def part2_cost(x, goal):
    n = abs(x-goal)
    return  n * (n+1) / 2

print ("part1", min_sum_cost(part1_cost))
print ("part2", min_sum_cost(part2_cost))
