import sys

I = list(map(int, map(str.strip, sys.stdin.readlines())))

def has_two_that_sums(nums, sum):
    visited = set()
    for n in nums:
        visited.add(n)
        if (sum - n) in visited:
            return True

    return False

def find_invalid_num_idx():
    for i in range(window_sz, len(I)):
        if not has_two_that_sums(I[i-window_sz:i], I[i]):
            return i

def find_set_that_sums(nums, total):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if sum(nums[i:j]) == total:
                return (i, j-1)

window_sz = 25
invalid_idx = find_invalid_num_idx()
print("part1", I[invalid_idx])

(i, j) = find_set_that_sums(I[0:invalid_idx], I[invalid_idx])
print("part2", sum((max(I[i:j]), min(I[i:j]))))