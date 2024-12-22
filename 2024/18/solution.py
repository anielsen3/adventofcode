import sys

bytes_in = [tuple(map(int, l.strip().split(","))) for l in open(sys.argv[1]).readlines()]
sz = max(bytes_in)[0]

def adjs(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_ok(obstacles, xy):
    (x, y) = xy
    return not xy in obstacles and 0 <= x <= sz and 0 <= y <= sz

def bfs(obstacles, dist, layers):
    while edge := set(nxy for xy in layers[-1] 
                          for nxy in adjs(xy) if is_ok(obstacles, nxy) and nxy not in dist):
        dist.update({ xy: len(layers) for xy in edge })
        layers += [edge]

    return dist

def distance(obstacles, start = (0,0), end = (sz, sz)):
    return bfs(set(obstacles), { start: 0 }, [{start}]).get(end, 9999)

def binsearch(key, value_fn, low, high):
    while low < high:
        mid = (low + high)//2
        if value_fn(mid) < key:
            low = mid + 1
        else:
            high = mid

    return mid


print("1:", distance(bytes_in[:1024]))

j = binsearch(9998, lambda i: distance(bytes_in[:i]), 0, len(bytes_in))
print("2:", bytes_in[j])