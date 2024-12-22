import sys

area = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                   for x, c in enumerate(l.strip()) }

def moves(xy_dxy):
    (xy, dxy) = xy_dxy
    x, y = xy
    dx, dy = dxy
    return {((x+dx, y+dy), dxy): 1,
             (xy, (-dy, dx))   : 1000,
             (xy, (dy, -dx))   : 1000}

def is_ok(xy):
    return xy in area and area[xy] != '#'

def bfs(edge, layers):
    prevs = {}
    dist = {}
    while edge:
        next_edge = set() 
        for score, xy_dxy in edge:
            for nxy_dxy, dscore in moves(xy_dxy).items():
                nxy, dxy = nxy_dxy
                nscore = dscore + score
                if is_ok(nxy):
                    if nxy_dxy not in dist or nscore < dist[nxy_dxy]:
                        next_edge.add((nscore, nxy_dxy))
                        dist[nxy_dxy] = score
        edge = next_edge


    return dist

S = next(xy for xy in area if area[xy] == 'S')
E = next(xy for xy in area if area[xy] == 'E')

start_xy_dxy = (S, (1, 0))
start = (1, start_xy_dxy) # score, xy, direction
dist = bfs({start}, [])

d, minE = min((d, (xy, dxy)) for (xy, dxy), d in dist.items() if xy == E)
print("1:", d)

def shortest_paths(dist):
    return []
    
#print(len(set(visited_squares(prevs, minE, start_xy_dxy))) + 1) # 777 too high

