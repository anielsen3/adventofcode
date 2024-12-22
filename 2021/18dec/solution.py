import sys
import re
import math

from functools import reduce

I = list(map(eval, map(str.strip, sys.stdin.readlines())))

def split(p):
    if isinstance(p, list):
        (l, r) = p
        nl = split(l)
        if nl == l:
            r = split(r)
        res = [nl, r]
        return res
    else:
        if (p >= 10):
            return [math.floor(p/2), math.ceil(p/2)] 
        else:
            return p

assert split(10) == [5,5]
assert split(11) == [5,6]
assert split(12) == [6,6]

def add_r_expl_rest(p, n):
    (l, r) = p
    if isinstance(l, int):
        return [l + n, r]
    else:
        return [add_r_expl_rest(l, n), r]

def add_l_expl_rest(p, n):
    (l, r) = p
    if isinstance(r, int):
        return [l, r + n]
    else:
        return [l, add_l_expl_rest(r, n)]


def d_explode(p, d = 0):
    if isinstance(p, list):
        (l, r) = p

        if (isinstance(l, int) and isinstance(r, int) and d >= 4):
            return { 'res': -1, 'expl': [l, r]}

        expl = []
        l_expl = d_explode(l, d+1)
        r_expl = { 'res': r }
        if 'expl' in l_expl and l_expl['expl']:
            l = l_expl['res'] # l exploded
            expl = l_expl['expl']
        else:
            r_expl = d_explode(r, d+1)
            r = r_expl['res']
            if 'expl' in r_expl:
                expl = r_expl['expl']

        # print (" " * d, l, r, d, "- E:", expl, " - le:", l_expl)
        if expl:
            if isinstance(l, int):
                if (l == -1):
                    l = 0
                elif expl:
                    l += expl[0]
                    expl[0] = 0

            if isinstance(r, int):
                if (r == -1):
                    r = 0
                elif expl:
                    r += expl[1]
                    expl[1] = 0

            elif 'expl' in l_expl and l_expl['expl'] and l_expl['expl'][1]:
                # print("r:", r, "expl:", expl)
                r = add_r_expl_rest(r, l_expl['expl'][1])
                l_expl['expl'][1] = 0

            elif 'expl' in r_expl and r_expl['expl'] and r_expl['expl'][0]:
                # print("l:", l, "expl:", expl)
                l = add_l_expl_rest(l, r_expl['expl'][0])
                r_expl['expl'][0] = 0


        return { 'res': [l, r], 'expl': expl }
    else:
        return { 'res': p }


assert d_explode([[[[[9,8],1],2],3],4])['res'] == [[[[0,9],2],3],4]
assert d_explode([7,[6,[5,[4,[3,2]]]]])['res'] == [7,[6,[5,[7,0]]]]
assert d_explode([[6,[5,[4,[3,2]]]],1])['res'] == [[6,[5,[7,0]]],3]
assert d_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])['res'] == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]

def explode(p):
    res = d_explode(p, 0)
    # print("exploded:", res['res'], "expl:", res['expl'])
    return res['res']

def add(p1, p2):
    if p1 == []:
        return p2
    if p2 == []:
        return p1
    else:
        return [p1, p2]

assert add([],[1,1]) == [1,1]
assert add([1,1],[]) == [1,1]
assert add([1,1],[2,2]) == [[1,1],[2,2]]

def d_reduce(p):
    while True:
        np = explode(p)
        if (np != p):
            p = np
            continue

        np = split(np)
        # print("split   :", np)

        if np == p:
            return np
        else:
            p = np            

def add_reduce(p1, p2):
    res = d_reduce(add(p1, p2))
    return res

def add_all(ps):
    return reduce(add_reduce, ps[1:], ps[0])

assert add_all([[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
assert add_all([[1,1],[2,2],[3,3],[4,4]]) == [[[[1,1],[2,2]],[3,3]],[4,4]]
assert add_all([[1,1],[2,2],[3,3],[4,4],[5,5]]) == [[[[3,0],[5,3]],[4,4]],[5,5]]
assert add_all([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]) == [[[[5,0],[7,4]],[5,5]],[6,6]]

assert add_all([[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]) == [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

def magnitude(p):
    if isinstance(p, int):
        return p
    else:
        [l, r] = p
        return 3 * magnitude(l) + 2 * magnitude(r)    

print("part1", magnitude(add_all(I)))

max_mag = 0
for i in range(len(I)):
    for j in range(len(I)):
        if i != j:
            mag = magnitude(add_reduce(I[i], I[j]))
            if (max_mag < mag):
                max_mag = mag

print("part2", max_mag)

