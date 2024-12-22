import sys
import functools
import math

def cmp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return 1 if l > r else -1 if l < r else 0
    else:
        if isinstance(r, int): r = [r]
        if isinstance(l, int): l = [l]

        # Use next(iter, default_value)
        return next((c for c in (cmp(le, re) for le, re in zip(l, r)) if c), cmp(len(l), len(r)))

def main():
    packets = [eval(l) for l in open(sys.argv[1]).readlines() if l.strip()]

    # Part 1
    print("1:", sum(idx+1 for idx, (l, r) in enumerate(zip(packets[::2], packets[1::2])) if cmp(l, r) < 0))

    # Part 2
    markers = [[[6]], [[2]]]
    packets_markers = sorted(packets + markers, key=functools.cmp_to_key(cmp))
    print("2:", math.prod(packets_markers.index(m)+1 for m in markers))

if __name__ == '__main__':
    main()