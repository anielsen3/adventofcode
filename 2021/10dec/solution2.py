import sys
import re

I = map(str.strip, sys.stdin.readlines())

corrupt_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def remove_valid_chunks(s):
    while True:
        (s, subs) = re.subn("\[]|\(\)|{}|<>", "", s)
        if not subs: return s

def find_closing_char(s):
    return re.search("[)\]}>]", s)

scrubbed_lines = map(remove_valid_chunks, I)
corrupt_lines = filter(find_closing_char, scrubbed_lines)
print("part1", sum(corrupt_points[find_closing_char(l).group(0)] for l in corrupt_lines))


incomplete_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4   
}

def incomplete_score(l):
    return reduce(lambda score, c: score * 5 + incomplete_points[c], reversed(l), 0)

def median(ns):
    return sorted(ns)[len(ns) // 2]

incomplete_lines = set(scrubbed_lines) - set(corrupt_lines)
print("part2", median([incomplete_score(l) for l in incomplete_lines]))