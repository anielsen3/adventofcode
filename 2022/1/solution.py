INPUT = (line.strip() for line in open("input1.txt").readlines())

def split_list(ls, pred = lambda x: x):
    res = [[]]
    for l in ls:
        res[-1].append(l) if pred(l) else res.append([])
    return res

def sum_ints(str_ints):
    return sum(int(x) for x in str_ints)

sums = sorted(map(sum_ints, split_list(INPUT)), reverse=True)

print(sums[0]) 
print(sum(sums[0:3]))


## new solution

INPUT2 = open("input1.txt").read()
sums2 = sorted(sum(int(y) for y in x.split("\n")) 
                          for x in INPUT2.split("\n\n"))

print(sums2[-1])
print(sum(sums2[-3:]))