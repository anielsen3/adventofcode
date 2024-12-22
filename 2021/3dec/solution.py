import sys

def rev_digit(c):
    return "1" if (c == "0") else "0"

def digit_for_count(count):
    return "1" if (count > num_lines / 2) else "0"

## calculate

input_ = list(map(str.strip, sys.stdin))
num_lines = len(input_)
num_ones = [0] * len(input_[0])

for line in input_:
    for i, c in enumerate(line):
        if c == '1': num_ones[i] += 1 

## result

res = "".join(map(digit_for_count, num_ones))
res_int = int(res, 2)
print(res, res_int)

inv_res = "".join(map(rev_digit, res))
inv_res_int = int(inv_res, 2)
print(inv_res, inv_res_int)

print(res_int * inv_res_int)

