import sys

I = map(str.strip, sys.stdin.readlines())

seen_nums = set() # visited nums
for n in I:
    n = int(n)
    seen_nums.add(n)

    if 2020-n in seen_nums:
        print ("part1", n * (2020-n))
        break

seen_nums = set() # visited nums
for n in I:
    n = int(n)
    seen_nums.add(n)

    for m in seen_nums:
        if (2020 - n - m) in seen_nums:
            print("part2", (2020 - n - m) * n * m)
            break
