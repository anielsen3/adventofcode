import sys
import re

input = [*map(str.strip, open(sys.argv[1]).readlines())]

def decode(l):
    l = l.replace("\\\\", "#")
    l = l.replace('\\"', "#")
    l = re.sub("\\\\x[0-9a-f][0-9a-f]", "#", l)
    return l

def encode(l):
    l = l.replace("\\", "\\\\")
    l = l.replace('"', '\\"')
    return l

print("1:", sum(len(l) - len(decode(l)) + 2 for l in input))
print("2:", sum(len(encode(l)) - len(l) + 2 for l in input))
