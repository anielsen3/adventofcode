import sys
import re

def input():
    return open(sys.argv[1]).readlines()

count = 0
for l in input():
    for muls in re.findall("mul\\((\\d+),(\\d+)\\)", l):
        count += int(muls[0]) * int(muls[1])

print("1:", count)


working = True
count2 = 0
for l in input():
    for muls in re.findall("(do\\(\\)|don't\\(\\)|mul\\((\\d+),(\\d+)\\))", l):
        if working and muls[0].startswith('mul'):
            count2 += int(muls[1]) * int(muls[2])

        if muls[0] == "do()":
            working = True

        if muls[0] == "don't()":
            working = False

print("2:", count2)