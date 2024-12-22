import sys
import re

from collections import defaultdict

I = map(str.strip, sys.stdin.readlines())

def parse_rules():
    rules = {}

    for line in I:
        (bag, contains) = line.split("s contain ")

        rules[bag] = {}
        for bstr in contains.split(", "):
            m = re.match("(\\d+) (.* bag)", bstr)
            if m:
                (b_num, b_type) = m.groups()
                rules[bag][b_type] = int(b_num)

    return rules

def add(dict1, dict2):
    for k in dict2.keys():
        dict1[k] += dict2[k]

    return dict1

def containees(bag, rules):
    result = defaultdict(lambda: 0, {})

    for b in rules[bag].keys():
        result[b] += rules[bag][b]
        add(result, containees(b, rules))

    return dict(result)

def count(bag, rules):
    return sum(num + num * count(b, rules) for b, num in rules[bag].items())

rules = parse_rules()
contain_map = { b: containees(b, rules) for b in rules.keys() }

print("part1:", len([b for b in rules.keys() if 'shiny gold bag' in contain_map[b]]))
print("part2:", count_contained('shiny gold bag', rules))
