import sys

def input():
    return (list(map(int, l.split())) for l in open(sys.argv[1]).readlines())

def inject(op, pairs):
    return map(lambda ab: op(ab[0], ab[1]), pairs)

def pairwise(xs):
    return zip(xs[0:-1], xs[1:])

def is_safe(row):
    incr = all(inject(lambda a, b: a < b, pairwise(row)))
    decr = all(inject(lambda a, b: a > b, pairwise(row)))
    safe = all(inject(lambda a, b: 1 <= abs(a - b) <= 3, pairwise(row)))

    return (incr or decr) and safe

print("1:", sum(map(is_safe, input())))


### PART 2 

def problem_dampener(row):
    return any(map(is_safe, (row[0:i] + row[i+1:] for i in range(len(row)))))

print("2:", sum(map(problem_dampener, input())))  
