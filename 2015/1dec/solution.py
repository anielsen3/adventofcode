import sys

I = sys.stdin.readline().strip()

num = 0
part2_idx = 0
for idx, c in enumerate(I):
    if c == '(':
        num += 1
    elif c == ')':
        num -= 1

    if num == -1 and part2_idx == 0:
        part2_idx = idx + 1

print("part1", num)
print("part2", part2_idx)