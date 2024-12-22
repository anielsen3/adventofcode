import sys

I = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                for x, c in enumerate(l) }

def pipe_ends(xy):
    c = I.get(xy, '.')
    north = (0, -1)
    south = (0, 1)
    east  = (1, 0)
    west  = (-1, 0)

    pipes = {'|': [north, south], 
             '-': [east, west], 
             'L': [north, east],
             'J': [north, west],
             '7': [south, west],
             'F': [south, east]}

    if c in pipes:
        return pipes[c]
    elif c == 'S': # check all directions for those that point back to S
        return [d for d, o in ((north, south), (south, north), (east, west), (west, east)) 
                      if o in pipe_ends(do_move(xy, d))]
    else:
        return []

def do_move(xy, d):
    return (xy[0] + d[0], xy[1] + d[1])

def follow_pipe(xy):
    return (do_move(xy, d) for d in pipe_ends(xy))

def flatten(xss):
    return (x for xs in xss for x in xs)

def bfs(adj_function, start):
    result = {}

    layers = [set([start])]
    while edge := set(flatten(map(adj_function, layers[-1]))).difference(result):
        result.update({ xy: len(layers) for xy in edge })
        layers.append(edge)

    return result

print("1:", max(bfs(follow_pipe, next(k for k, v in I.items() if v == 'S')).values()))