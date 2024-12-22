import sys

from collections import defaultdict, Counter

input_  = sys.stdin.readline().split(",")
fish_cnt = defaultdict(lambda: 0, Counter(input_))

for day in range(257):
    print("After " + str(day) + " days", sum(fish_cnt.values()))

    # save number of fish ready to spawn
    num_spawned = fish_cnt['0']

    # update fishes for day
    for i in range(8):
        fish_cnt[str(i)] = fish_cnt[str(i+1)]

    # update spawners
    fish_cnt['6'] += num_spawned # spawners
    fish_cnt['8'] = num_spawned # spawnees
