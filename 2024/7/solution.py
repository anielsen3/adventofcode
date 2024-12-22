import sys
from operator import add, mul

def cat(a, b):
    return int(f"{a}{b}")

def sums_to(target, current, digits, ops):
    if digits == []:
        return current == target

    return any(sums_to(target, op(current, digits[0]), digits[1:], ops) for op in ops)

def find_sum(l, ops):
    (target, digits) = (int(l.split(":")[0]), [*map(int, l.split(":")[1].split())])
    return target if sums_to(target, digits[0], digits[1:], ops) else 0

input = open(sys.argv[1]).readlines()

print("1:", sum(find_sum(l, [add, mul]) for l in input)) # 3598800864292
print("2:", sum(find_sum(l, [add, mul, cat]) for l in input)) # 340362529351427