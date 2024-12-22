import sys
import math

VAL = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }

def from_snafu(s):
    s = s.strip()
    return int(sum(VAL[s[-n]] * math.pow(5, n-1) for n in range(len(s), 0, -1)))

def to_snafu(rem):
    res = ""
    while rem > 0:
        d = rem % 5
        if d == 4:
            rem += 5
            res += "-"
        elif d == 3:
            rem += 5
            res += "="
        else:
            res += str(d)

        rem //= 5 

    return res[::-1] # reverse string

def read_input():
    return open(sys.argv[1]).readlines()

print("1", to_snafu(sum(from_snafu(l) for l in read_input())))