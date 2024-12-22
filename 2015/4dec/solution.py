import sys
import hashlib

I = sys.stdin.readline().strip()

def find_first_nonce(numZeros):
    i = 0
    while True:
        msg = (I + str(i)).encode('utf-8')
        md5 = hashlib.md5(msg).hexdigest()
        if md5[:numZeros] == '0' * numZeros:
            return i
        else:
            i += 1


print("part1", find_first_nonce(5))
print("part2", find_first_nonce(6))