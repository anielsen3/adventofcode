import sys

I = list(map(str.strip, sys.stdin.readlines()))

def surface_box(box):
    (w, h, l) = sorted(map(int, box.split("x")))
    return 2*l*w + 2*w*h + 2*h*l + (w * h)

def ribbon_box(box):
    (w, h, l) = sorted(map(int, box.split("x")))
    return 2*w + 2*h + w * h * l    

print ("part1", sum(surface_box(box) for box in I))
print ("part2", sum(ribbon_box(box) for box in I))
