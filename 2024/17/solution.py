import sys
import re

input = "".join(open(sys.argv[1]).readlines())

registers_in = { reg: int(val) for reg, val in re.findall("Register (\\w): (\\d+)", input.split("\n\n")[0]) }
instructions = re.findall("\\d+", input.split("\n\n")[1])

def combo_operand(registers, operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    else:
        raise Error()


def run_program(registers, instructions):
    registers = registers.copy()
    out = []
    i = 0
    while i < len(instructions):
        opcode = instructions[i]
        operand = int(instructions[i+1])

        if opcode == '0': #adv
            registers['A'] //= 2 ** combo_operand(registers, operand)
        elif opcode == '1': #bxl
            registers['B'] ^= operand
        elif opcode == '2': #bst
            registers['B'] = combo_operand(registers, operand) % 8
        elif opcode == '3': #jnz
            if registers['A']:
                i = operand
                continue
        elif opcode == '4': #bxc
            registers['B'] ^= registers['C']
        elif opcode == '5': #out
            out += f"{combo_operand(registers, operand) % 8}"
        elif opcode == '6': #bdv
            registers['B'] = registers['A'] // 2 ** combo_operand(registers, operand)
        elif opcode == '7': #cdv
            registers['C'] = registers['A'] // 2 ** combo_operand(registers, operand)

        i += 2

    return out

print("1", ",".join(run_program(registers_in, instructions))) 
print("1", ",".join(run_program(registers_in, instructions))) 

def cmp_instructions(i1, i2):
    if len(i1) > len(i2):
        return 1
    elif len(i1) == len(i2):
        for i in range(len(i1)):
            if i1[i] > i2[i]:
                return 1
            if i1[i] < i2[i]:
                return -1
        return 0
    else:
        return -1


def binary_search(instructions):
    low = 1
    high = 999999999999999
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        registers = {'A': mid, 'B': 0, 'C': 0}
        result = run_program(registers, instructions)
        print(instructions, mid, result)

        if cmp_instructions(result, instructions) == -1:
            low = mid + 1
        elif cmp_instructions(result, instructions) == 1:
            high = mid - 1
        else:
            print(low, high, mid)
            return low, mid, high
 
low, high, mid = binary_search(instructions)
