import sys
import re
import math

from operator import mul
from functools import reduce

I = sys.stdin.readline().strip()

trans_table = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

b = ""
for i in I:
    b += trans_table[i]

def chomp_bits(n, s):
    return re.match("([01]{" + str(n) + "})(.*)", s).groups()

def chomp_bits_int(n, s):
   (bits, rest) = chomp_bits(n, s)
   return (int(bits, 2), rest)

def read_literal(s):
    num_bits = ""
    rest = s

    while True:
        (one_bit, rest) = chomp_bits(1, rest)
        (four_bits, rest) = chomp_bits(4, rest)
        num_bits += four_bits

        if (one_bit == '0'):
            break

    return (int(num_bits, 2), rest)

def read_op(rest):
    (length_type, rest) = chomp_bits(1, rest)

    if (length_type == '0'): # sum of length of subpackets
        (length, rest) = chomp_bits_int(15, rest)
        return (parse(rest[:length])[0], rest[length:])
    else: # num sub-packets
        (num, rest) = chomp_bits_int(11, rest)
        return parse(rest, num)        

def parse(s, max_num=9999):
    rest = s
    packets = []
    for _ in range(max_num):
        if not rest or int(rest, 2) == 0:
            return (packets, "")

        (v, t, rest) = re.match("([01]{3})([01]{3})(.*)", rest).groups()

        if (t == '100'): # literal
            (num, rest) = read_literal(rest)
            packets.append({'version': int(v,2), 'num': num})
        else:
            (subtree, rest) = read_op(rest)
            packets.append({'version': int(v,2), 'op': t, 'sub': subtree })

    return (packets, rest)

def sum_version(packets):
    res = 0
    for packet in packets:
        res += packet.get('version') + sum_version(packet.get('sub', []))
    return res

def calc_result(packet):
    if 'op' not in packet:
        return packet.get('num')
    else:
        op = packet.get('op')
        if (op == '000'):
            return sum(map(calc_result, packet.get('sub')))
        if (op == '001'):
            return reduce(mul, map(calc_result, packet.get('sub')), 1)
        if (op == '010'):
            return reduce(min, map(calc_result, packet.get('sub')), math.inf)
        if (op == '011'):
            return reduce(max, map(calc_result, packet.get('sub')), 0)
        if (op == '101'):
            (sub1, sub2) = packet.get('sub')
            return 1 if calc_result(sub1) > calc_result(sub2) else 0
        if (op == '110'):
            (sub1, sub2) = packet.get('sub')
            return 1 if calc_result(sub1) < calc_result(sub2) else 0
        if (op == '111'):
            (sub1, sub2) = packet.get('sub')
            return 1 if calc_result(sub1) == calc_result(sub2) else 0


(packets, _) = parse(b)
print("part1", sum_version(packets))
print("part2", calc_result(packets[0]))
# print(packets)