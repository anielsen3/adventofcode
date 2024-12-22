import sys
from functools import cmp_to_key

input = "".join(open(sys.argv[1]).readlines())
(rules, pages) = input.split("\n\n")

def find_val(page, count_sorted):
    p = [*map(int, page.split(","))]
    sort_p = sorted(p, key=cmp_to_key(lambda n1, n2: 1 if f"{n2}|{n1}" in rules else -1))
    return sort_p[len(p)//2] if count_sorted == (p == sort_p) else 0

print("1:", sum(find_val(page, True) for page in pages.split("\n")))
print("2:", sum(find_val(page, False) for page in pages.split("\n")))