import sys
import re

from functools import reduce

I = list(map(str.strip, sys.stdin.readlines()))

empty_line = I.index("")
P = [pt.split(",") for pt in I[:empty_line]]
folds = I[empty_line+1:]

def fold_val(val, piv):
    return val if val < piv else (piv*2 - val)

def fold_pt(x, y, fold):
    (axis, piv) = re.match("fold along (.*)=(.*)", fold).groups(2)
    
    if axis == 'x':
        return (fold_val(x, int(piv)), y) 
    else:
        return (x, fold_val(y, int(piv)))  

def do_fold(fold, i):
    return set(fold_pt(int(x), int(y), fold) for (x, y) in i)
    
def show(i):
    return "\n".join("".join("#" if (x, y) in i else " " 
                                 for x in range(40)) 
                                 for y in range(8))

print("part1", len(do_fold(folds[0], P)))
print("part2")
print(show(reduce(lambda i, fold: do_fold(fold, i), folds, P)))