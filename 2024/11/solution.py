import sys

input = str(open(sys.argv[1]).readline())

def blink(n):
    if n == '0':
        return ['1']
    elif len(n) % 2 == 0:
        return [str(int(n[:len(n)//2])), str(int(n[len(n)//2:]))]
    else:
        return [str(int(n)*2024)]

def solve(num_iterations):
    cur_step = { n: 1 for n in input.split() }

    for i in range(num_iterations):
        next_step = {}

        for num in cur_step:
            for n in blink(num):
                next_step[n] = next_step.get(n, 0) + cur_step[num]

        cur_step = next_step

    return sum(cur_step.values())

print("1:", solve(25))
print("2:", solve(75))
