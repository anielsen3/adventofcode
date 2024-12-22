import sys

def sum_in_window(i, window_size, input_):
    return sum(input_[i-window_size+1:i+1])

window_size = 1
p = 0
c = 0

input_ = list(map(int, map(str.strip, sys.stdin)))

for idx in range(len(input_)):
    d = sum_in_window(idx, window_size, input_)
    if (p > 0 and d > p):
        c += 1
    
    p = d

print(c)