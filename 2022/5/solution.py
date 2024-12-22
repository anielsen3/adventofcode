import re
import sys

INPUT = open(sys.argv[1]).read()

def init_state(top):
    (*crates, numbers) = top.split("\n")

    num_crates = int(numbers.split()[-1])
    crates_array = [[] for n in range(num_crates)]

    for line in crates:
        for n in range(num_crates):
            char = line[1+n*4]
            if char != ' ':
                crates_array[n].insert(0, char) 

    return crates_array

def do_move(crates_array, move_line, crane_version):
    print(re.findall("\\d+", move_line))
    (count, from_num, to_num) = map(int, re.findall("\d+", move_line)[1:])
    
    gifts = [crates_array[from_num-1].pop() for _ in range(count)]
    for c in gifts if crane_version <= 9000 else reversed(gifts):
        crates_array[to_num-1].append(c)
                
def find_solution(crane_version):
    (top, bottom) = INPUT.split("\n\n")

    crates_array = init_state(top)

    for line in bottom.split("\n"):
        do_move(crates_array, line, crane_version)

    return "".join(crate.pop() for crate in crates_array)


print(f'1: {find_solution(9000)}')
print(f'2: {find_solution(9001)}')
