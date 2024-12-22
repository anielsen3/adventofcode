import sys

I = [list(map(int, n)) for n in map(str.split, open(sys.argv[1]).readlines())]

def calc_diffs(nums):
    return [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

def all_same(nums):
    return all(n == nums[0] for n in nums)

def ext_next(nums):
    return nums if all_same(nums) else nums + [nums[-1] + ext_next(calc_diffs(nums))[-1]]

print("1:", sum(s[-1] for s in map(ext_next, I)))


def ext_prev(nums):
    return nums if all_same(nums) else [nums[0] - ext_prev(calc_diffs(nums))[0]] + nums

print("2:", sum(s[0] for s in map(ext_prev, I)))
