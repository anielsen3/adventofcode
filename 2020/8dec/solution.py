import sys

I = list(map(str.strip, sys.stdin.readlines()))

def terminates(P):
    acc = 0
    visited = set()
    i = 0
    while (i < len(P)):
        if i in visited: return (False, acc)
        visited.add(i)

        (op, val) = P[i].split(" ")
        val = int(val)

        if (op == 'acc'):
            acc += val
        if (op == 'jmp'):
            i += val - 1

        i += 1

    return (True, acc)

print("part1", terminates(I))

def replace_op(i):
    p_copy = I.copy()

    if (I[i][0:3] == 'jmp'):
        p_copy[i] = 'nop' + p_copy[i][3:]
    elif (I[i][0:3] == 'nop'):
        p_copy[i] = 'jmp' + p_copy[i][3:]

    return p_copy

for i in range(len(I)):
    t = terminates(replace_op(i))
    if (t[0]):
        print("part2", t)
