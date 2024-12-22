import sys
import re

I = map(str.strip, sys.stdin.readlines())

def valid_hgt(x):
    match = re.match("(\\d+)(cm|in)", x)
    if not match: return False
    (num, measure) = match.groups()
    if measure == 'cm':
        return 150 <= int(num) <= 193
    elif measure == 'in':
        return 59 <= int(num) <= 76

    return False

fields = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': valid_hgt,
    'hcl': lambda x: re.match("#[0-9a-f]{6}", x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match("\\d{9}", x),
    'cid': lambda x: True
}

def valid_part1(passport):
    errors = filter(lambda x: x not in passport.keys(), fields.keys())
    return not errors or errors == ['cid']

def validate_field(field):
    (key, val) = field
    return fields[key](val)

def valid_part2(passport):
    errors = filter(lambda x: not validate_field(x), passport.items())
    return not errors and valid_part1(passport)

def validate(valid_fun):
    num_valid = 0
    cur_pass = {}
    for line in I:
        if line:
            for field in line.split(" "):
                (name, val) = field.split(":")
                cur_pass[name] = val
        else:
            if (valid_fun(cur_pass)):
                num_valid += 1

            cur_pass = {}

    return num_valid

print("part1", validate(valid_part1))
print("part2", validate(valid_part2))