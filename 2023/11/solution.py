import sys

I = { (x, y): c for y, l in enumerate(open(sys.argv[1]).readlines()) 
                for x, c in enumerate(l) }

def expand():
    for x, y in I:
        print(x)

print(expand())