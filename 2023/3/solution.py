import sys
import re


def flatten_list(xss):
    return [x for xs in xss for x in xs]

def is_symbol(xy):
    return xy in diagram and not diagram[xy].isdigit() and not diagram[xy] == '.' 

def adjecents8(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), 
            (x, y-1), (x+1, y+1), 
            (x-1, y-1), (x-1, y+1), (x+1, y-1)]

def parse_numbers(line, y): # return type: tuple(value, list[xy])
    acc = 0
    xys = []

    for x, c in enumerate(line):
        if c.isdigit():
            xys.append((x, y))
            acc = 10 * acc + int(c)
        else:
            yield(acc, xys)
            acc = 0
            xys = []

    if acc:
        yield(acc, xys)

def is_part(number):
    _, xys = number
    return any(map(is_symbol, flatten_list(map(adjecents8, xys))))

## PART 1
input_lines = open(sys.argv[1]).readlines()
diagram = { (x,y): c for y, line in enumerate(input_lines) for x, c in enumerate(line.strip()) }
numbers = flatten_list(parse_numbers(line, y) for y, line in enumerate(input_lines))
parts = [number for number in numbers if is_part(number)]

print(f'1: {sum(val for val, _ in parts)}')


## PART 2
stars = [xy for xy, c in diagram.items() if c == '*']
adj_parts_vals = [ [val for val, part_xys in parts if set(part_xys) & set(adjecents8(star))] for star in stars ]

print(f'2: {sum(v[0] * v[1] for v in adj_parts_vals if len(v) == 2)}')
