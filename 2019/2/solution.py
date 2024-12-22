import sys

def read_input():
    return list(map(int, open(sys.argv[1]).read().split(',')))

def evaluate(p):
    preg = 0
    while p[preg] != 99:
        if p[preg] == 1:
            p[p[preg+3]] = p[p[preg+1]] + p[p[preg+2]]
        elif p[preg] == 2:
            p[p[preg+3]] = p[p[preg+1]] * p[p[preg+2]]
        else:
            raise IndexError(f"Unknown opcode {p[preg]} at pos {preg}, p = {p}")

        preg += 4

    return p

print(evaluate([1,0,0,0,99]))
print(evaluate([2,4,4,5,99,0]))
print(evaluate([1,1,1,4,99,5,6,0,99]))

p = read_input()
p[1] = 12
p[2] = 2
print("1", evaluate(p)[0])

p = read_input()
p[1] = 48
p[2] = 47
assert(evaluate(p)[0] == 19690720)
print("2", 4847)
