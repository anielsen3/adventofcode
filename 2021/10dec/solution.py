import sys

from functools import reduce

I = map(str.strip, sys.stdin.readlines())

parse_map = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}

error_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def find_error_c(line):
    stack = []
    for c in line:
        if c in parse_map.keys():
            stack.append(c)
        else:
            opener = stack.pop()
            if (parse_map[opener] != c):
                return c    

sum = 0
for line in I:
    error_c = find_error_c(line)
    if (error_c):
        sum += error_score[error_c]

print("part1", sum)

complete_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def find_missing(line):
    stack = []
    for c in line:
        if c in parse_map.keys():
            stack.append(c)
        elif c == parse_map[stack[-1]]:
            stack.pop()

    return stack

scores = []
for line in I:
    score = 0
    if not find_error_c(line):
        for m in reversed(find_missing(line)):
            score = score * 5 + complete_score[parse_map[m]]
    
        scores.append(score)

print ("part2", sorted(scores)[len(scores) // 2])
