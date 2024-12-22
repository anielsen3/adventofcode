import sys

digit_map = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

input_ = map(str.strip, sys.stdin.readlines())

cnt = 0
for in_, out_ in map(lambda x: x.split("|"), input_):
    for seg in out_.split():
        if len(seg) in (len(digit_map[i]) for i in [1, 4, 7, 8]):
            cnt += 1 

print("part1", cnt)


def contains(seg1, seg2):
    return all(c in seg1 for c in seg2)

def find_remove(ps, pred):
    val = next(x for x in ps if pred(x))
    ps.remove(val)
    return val

def order_seg(seg):
    return "".join(sorted(seg))

res = 0
for in_, out_ in map(lambda x: map(str.strip, x.split("|")), input_):
    in_segs  = map(order_seg, in_.split())
    out_segs = map(order_seg, out_.split()) 
    segs = set(in_segs + out_segs)

    ## dekoder-algoritme
    ## 1 er 2 lang
    ## 4 er 4 lang
    ## 7 er 3 lang
    ## 8 er 7 lang
    ## 0 er 6 lang, indeholder 1 men ikke 4
    ## 9 er 6 lang, indeholder 7 og 4
    ## 6 er 6 lang, 
    ## 3 er 5 lang, indeholder 7
    ## 5 er 5 lang, og er indholdt i 9
    ## 2 er 5 lang,  
    code_for = {}
    code_for[1] = find_remove(segs, lambda c: len(c) == 2)
    code_for[4] = find_remove(segs, lambda c: len(c) == 4)
    code_for[7] = find_remove(segs, lambda c: len(c) == 3)
    code_for[8] = find_remove(segs, lambda c: len(c) == 7)
    code_for[0] = find_remove(segs, lambda c: len(c) == 6 and contains(c, code_for[1]) and not contains(c, code_for[4]))
    code_for[3] = find_remove(segs, lambda c: len(c) == 5 and contains(c, code_for[7]))
    code_for[9] = find_remove(segs, lambda c: len(c) == 6 and contains(c, code_for[7]) and contains(c, code_for[4]))
    code_for[6] = find_remove(segs, lambda c: len(c) == 6)
    code_for[5] = find_remove(segs, lambda c: len(c) == 5 and contains(code_for[9], c))
    code_for[2] = find_remove(segs, lambda c: len(c) == 5)

    decoder = { y: x for x, y in code_for.items() } # invert dict

    val = "".join(str(decoder[x]) for x in out_segs)
    res += int(val)

print("part2", res)