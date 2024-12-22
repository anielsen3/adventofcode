import re
import sys
import itertools
import random

def flood(dist, layers, map):
    edge = set(nv for v in layers[-1] 
                  for nv in map[v] if nv not in dist)

    dist.update({ xy: len(layers) for xy in edge })

    if edge:    
        flood(dist, layers + [edge], map)

def distance_map_from(start, map):
    dist = { start: 0 }
    flood(dist, [{start}], map)
    return dist

def flow_from_moving_to(rate, distance, minutes_left):
    if distance == 0:
        return 0
    if distance > minutes_left:
        return 0 
    minutes_of_flow = minutes_left - distance - 1
    return minutes_of_flow * rate

def flow_of_path(path, distances, rates, minutes):
    sum_flow = 0
    cur_v = 'AA'
    for nv in path:
        distance = distances[cur_v][nv]
        sum_flow += flow_from_moving_to(rates[nv], distance, minutes)
        minutes -= 1
        minutes -= distance
        cur_v = nv

    return sum_flow

def shuffle_onces(path):
    neighbors = []

    for i in range(len(path)):
        for j in range(i+1, len(path)):
            neighbor = path.copy()
            neighbor[i] = path[j]
            neighbor[j] = path[i]
            neighbors.append(neighbor)

    return neighbors

def best_shuffle(path, distances, rates, cost_function):
    return max((cost_function(npath, distances, rates), npath) for npath in shuffle_onces(path))    

# Parse input
def parse_input():
    map = {}
    rates = {}
    distances = {}
    for line in open(sys.argv[1]).readlines():
        (name, rate, lead_to) = re.match("Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line.strip()).groups()
        map[name] = lead_to.split(", ")
        rates[name] = int(rate)

    for v in map:
        distances[v] = distance_map_from(v, map)

    return distances, rates

# Part 1
def random_path(rates):
    path = [v for v in rates if rates[v] > 0]
    random.Random().shuffle(path)
    return path

def optimize_random(distances, rates, cost_function, init_path):
    path = init_path
    flow = cost_function(path, distances, rates)
    while True:
        nflow, path = best_shuffle(path, distances, rates, cost_function)
        if nflow > flow:
            flow = nflow
        else:
            return flow

def optimize_random_n(distances, rates, cost_function, n = 100):
    return max(optimize_random(distances, rates, cost_function, random_path(rates)) for _ in range(n))

def part1_cost(path, distances, rates):
    return flow_of_path(path, distances, rates, 30)

distances, rates = parse_input()
print("1:", optimize_random_n(distances, rates, part1_cost))

# Part 2
def random_paths(rates):
    path = [v for v in rates if rates[v] > 0]
    random.Random().shuffle(path)
    path1 = path[0::2]
    path2 = path[1::2]
    return path1, path2

def shuffle_onces2(path, path2):
    neighbors = []

    for i in range(len(path)):
        for j in range(len(path2)):
            neighbor1 = path.copy()
            neighbor2 = path2.copy()
            neighbor1[i] = path2[j]
            neighbor2[j] = path[i]
            neighbors.append((neighbor1, neighbor2))

    return neighbors

def best_shuffle2(path, distances, rates, cost_function, path2):
    return max((cost_function(npath1, npath2, distances, rates), npath1, npath2) for (npath1, npath2) in shuffle_onces2(path, path2))    

def optimize_random2(distances, rates, cost_function, init_path, path2):
    path = init_path
    flow = cost_function(path, path2, distances, rates)
    while True:
        nflow, path, path2  = best_shuffle2(path, distances, rates, cost_function, path2)
        if nflow > flow:
            flow = nflow
        else:
            return flow

def optimize_random_n2(distances, rates, cost_function, n = 10000):
    max_flow = 0
    for _ in range(n):
        path1, path2 = random_paths(rates)
        max_flow = max(max_flow, optimize_random2(distances, rates, cost_function, path1, path2))

    return max_flow

def part2_cost(path, path2, distances, rates):
    return flow_of_path(path, distances, rates, 26) + flow_of_path(path2, distances, rates, 26)

print("2:", optimize_random_n2(distances, rates, part2_cost))
