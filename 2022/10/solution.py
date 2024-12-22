import sys

sum_signal = 0
cycle = 0
xreg = 1
screen = ""

def incr_cycle():
    global cycle, xreg, sum_signal

    draw_to_screen()    
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum_signal += cycle * xreg

def draw_to_screen():
    global xreg, cycle, screen

    screen +=  "#" if abs(xreg - cycle % 40) <= 1 else " "
    if cycle % 40 == 39:
        screen += "\n"

for line in open(sys.argv[1]).readlines():
    incr_cycle()
    if line.startswith("addx"):
        incr_cycle()
        xreg += int(line.split()[1])
    
print("1:", sum_signal)
print("2:", "\n" + screen)