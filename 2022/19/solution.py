import re
import sys
import math

cost_types = ['ore', 'clay', 'obsidian']

def parse_input():
    costs = {}

    # ex: Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 3 ore and 9 obsidian.
    for line in open(sys.argv[1]).readlines():
        num, rest = re.match("Blueprint (\d+): (.*)", line).groups()
        costs[num] = {}
        for m in re.findall("Each (\w+) robot costs (\d+ \w+)( and \d+ \w+)?", rest):
            (robot_type, cost1, cost2) = m

            cost = [0, 0, 0]
            if (cost1):
                (value, cost_type) = cost1.split(" ")
                cost[cost_types.index(cost_type)] = -int(value)

            if (cost2):
                (_, value, cost_type) = cost2.strip().split(" ")
                cost[cost_types.index(cost_type)] = -int(value)

            costs[num][robot_type] = tuple(cost)

    return costs

def plus(ocb, ocb2, ocb3 = (0, 0, 0)):
    (o,  c,  b)  = ocb
    (o2, c2, b2) = ocb2
    (o3, c3, b3) = ocb3
    return (o+o2+o3, c+c2+c3, b+b2+b3)

def can_build(ocb, cost_f):
    (o, c, b) = ocb
    return o >= -cost_f[0] and c >= -cost_f[1] and b >= -cost_f[2]

def dfs(cost, ocb=(0, 0, 0), g=0, ocb_r=(0, 0, 0), g_r=0, t=0, bestg=0, skipof=False, skipcf=False, skipbf=False):
    if t == 0:
        return g
    elif bestg >= (g + t*(g_r + t-1)):
        return g
    else:
        if t > 0:
            if can_build(ocb, cost['geode']):
                bestg = max(bestg, dfs(cost, plus(ocb, cost['geode'], ocb_r), g+g_r, ocb_r, g_r+1, t-1, bestg))
            else:
                if can_build(ocb, cost['obsidian']) and not skipbf:
                    bestg = max(bestg, dfs(cost, plus(ocb, cost['obsidian'], ocb_r), g+g_r, plus(ocb_r, (0, 0, 1)), g_r, t-1, bestg))
                    skipbf = True

                if can_build(ocb, cost['clay']) and not skipcf:
                    bestg = max(bestg, dfs(cost, plus(ocb, cost['clay'], ocb_r), g+g_r, plus(ocb_r, (0, 1, 0)), g_r, t-1, bestg))
                    skipcf = True

                if can_build(ocb, cost['ore']) and not skipof:
                    if ocb_r[0] < max(-o for (o, _, _) in cost.values()):
                        bestg = max(bestg, dfs(cost, plus(ocb, cost['ore'], ocb_r), g+g_r, plus(ocb_r, (1, 0, 0)), g_r, t-1, bestg))
                        skipof = True

        return max(bestg, dfs(cost, plus(ocb, ocb_r), g + g_r, ocb_r, g_r, t-1, bestg, skipof, skipcf, skipbf))

# Part 1
costs = parse_input()
print("1:", sum(dfs(cost=costs[n], ocb_r=(1, 0, 0), t=24)*int(n) for n in costs.keys()))

# Part 2
print("2:", math.prod(dfs(cost=cost, ocb_r=(1, 0, 0), t=32) for cost in list(costs.values())[0:3]))

