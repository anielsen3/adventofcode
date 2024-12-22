import sys
import math

from collections import Counter

I = list(int(x.strip()) for x in sys.stdin.readlines())
I += [0, max(I)+3] # ground and device
I = sorted(I)

diffs = []
for i in range(1, len(I)):
    diffs.append(I[i] - I[i-1])

count_diffs = Counter(diffs)
print(count_diffs)
print("part1", count_diffs[1] * count_diffs[3])


def num_pos(diff_len):
    return [1, 1, 2, 4, 7, 11, 16, 22][diff_len]

i = 0
res = 1
print(diffs)
while i < len(diffs):
    j = i
    while j < len(diffs) and diffs[j] == 1:
        j += 1

    res *= num_pos(len(diffs[i:j]))

    i = j + 1

print(res)