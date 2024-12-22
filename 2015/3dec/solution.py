import sys

I = sys.stdin.readline().strip()

def visit(s):
    x = y = 0
    visited = set()
    visited.add((x, y))

    for c in s:
        if c == '<':
            x -= 1
        elif c == '^':
            y -= 1
        elif c == '>':
            x += 1
        elif c == 'v':
            y += 1

        visited.add((x, y))

    return visited

print("part1", len(visit(I)))

robo_i = I[1::2]
santa_i = I[0::2]

visited = visit(robo_i)
visited = visited.union(visit(santa_i))

print("part2", len(visited))
