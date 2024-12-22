import sys

from collections import defaultdict
from functools import reduce

(firstline, _, *image) = [str.strip(line) for line in sys.stdin.readlines()]
I = defaultdict(lambda: ".", {(x,y): c for y, line in enumerate(image) for x, c in enumerate(line)})

def read_area(xy):
    (x, y) = xy
    return [(x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),   (x,y),    (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)]
    
def read_area_string(xy, img):
    return "".join(img[n_xy] for n_xy in read_area(xy))

def binary(s):
    return int(s.translate(s.maketrans("#.", "10")), 2)

def outpixel(xy, img):
    return firstline[binary(read_area_string(xy, img))]

def get_default_value(img):
    big_xy = (-999999999, -9999999999)
    result = img[big_xy]
    del img[big_xy]
    return result

def new_default_char(img):
    return firstline[binary(get_default_value(img) * 9)]

def enhance(img):
    out = defaultdict(lambda: new_default_char(img))

    min_x = min(x for x,y in img)
    max_x = max(x for x,y in img)
    min_y = min(y for x,y in img)
    max_y = max(y for x,y in img)

    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            out[(x, y)] = outpixel((x, y), img)
    
    return out

def num_pixels(img):
    return len([pix for pix in img.values() if pix == '#'])

print("part1", num_pixels(reduce(lambda img, _: enhance(img), range(2), I)))
print("part2", num_pixels(reduce(lambda img, _: enhance(img), range(50), I)))
