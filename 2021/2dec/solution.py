import sys

x = 0
y = 0
for line in sys.stdin:
    (cmd, num) = line.split()

    if (cmd == 'up'):
        y -= int(num)
    elif (cmd == 'down'):
        y += int(num)
    elif (cmd == 'forward'):
        x += int(num)

print(x, y)