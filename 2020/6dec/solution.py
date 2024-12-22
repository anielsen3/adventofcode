import sys

from collections import defaultdict
from functools import reduce

I = list(map(str.strip, sys.stdin.readlines() + [""]))

def score_part1(group):
    answers = set()
    for person in group:
        answers = answers.union(list(person))

    return len(answers)

def score_part2(group):
    answer_cnt = defaultdict(lambda: 0, {})
    for person in group:
        for answer in person:
            answer_cnt[answer] += 1

    return len([a for a in answer_cnt.keys() if answer_cnt[a] == len(group) ])

def sum_groups(sum_function):
    sum_count = 0
    cur_group = list()
    for line in I:
        if (line):
            cur_group += [line]
        else:
            sum_count += sum_function(cur_group)
            cur_group = list()

    return sum_count

print("part1", sum_groups(score_part1))
print("part2", sum_groups(score_part2))

