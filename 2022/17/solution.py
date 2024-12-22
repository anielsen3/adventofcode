import sys
import functools

shapes = [
['####'],

[' # ',
 '###',
 ' # '],

['  #',
 '  #',
 '###'],

['#',
 '#',
 '#',
 '#'],

['##',
 '##']]

class Rock:
    def __init__(self, shape):
        self.shape = shape
        self.xpos = 0
        self.ypos = 0

    def can_fall(self, cave):
        res = self.can_move(0, -1, cave)
        # print("can_fall", self, res)
        return res

    def can_move(self, dx, dy, cave):
        self.xpos += dx
        self.ypos += dy
        top_rocks = sorted(cave, key=lambda rock: rock.ypos, reverse=True)[0:30]
        collided = self.hit_floor() or self.hit_wall() or any(self.collides_with(rock) for rock in top_rocks if rock != self)
        self.xpos -= dx
        self.ypos -= dy
        return not collided

    def fall(self, cave):
        # print(f"{self} falls 1")
        self.ypos -= 1

    def hit_floor(self):
        res = any(y == 0 for (_, y) in self.pixels())
        # print("hit_floor", self, res)
        return res

    def hit_wall(self):
        res = any(x < 0 or x >= 7 for (x, _) in self.pixels())
        # print("hit_wall", self, res)
        return res

    def collides_with(self, other):
        return any(p for p in self.pixels() if p in other.pixels())

    def pixels(self):
        pixels = []
        for y, line in enumerate(reversed(self.shape)):
            for x, bit in enumerate(line):
                if bit == "#":
                    pixels.append((x + self.xpos, y + self.ypos))
        return pixels
        
    def jet_push(self, jet, cave):
        # print(f"{self} jet pushes {jet}")
        if jet == '<':
            if self.can_move(-1, 0, cave):
                self.xpos -= 1
        
        if jet == '>':
            if self.can_move(1, 0, cave):
                self.xpos += 1
        # print(f"{self} jet has been pushed {jet}")

    def __str__(self):
        return f"{self.xpos, self.ypos, self.shape}"

jets = open(sys.argv[1]).read()
cave = []

def top_of_tower(cave):
    top_rocks = sorted(cave, key=lambda rock: rock.ypos, reverse=True)[0:30]
    return max(max(y for (_, y) in rock.pixels()) for rock in top_rocks) if top_rocks else 0

def start_rock(i):
    rock = Rock(shapes[i % len(shapes)])
    rock.ypos = top_of_tower(cave) + 4
    rock.xpos = 2
    return rock

def draw_cave(cave):
    cave_pixels = {}
    for rock in cave:
        for p in rock.pixels():
            cave_pixels[p] = "#"

    res = ""
    for y in range(max(y for (x,y) in cave_pixels), 0, -1):
        res += str(y) 
        res += " " if y < 10 else ""
        for x in range(7):
            res += "#" if (x, y) in cave_pixels else "."
        
        res += "\n"
    
    print(res)

## simulate    
jet_num = 0
rock_num = 0

for rock_num in range(int(1e12)):
    h = top_of_tower(cave)

    if (rock_num == 2022):
        print("1:", h)

    falling_rock = start_rock(rock_num)
    cave.append(falling_rock)
    rock_num += 1

    while True:
        # jet pushes rock
        falling_rock.jet_push(jets[jet_num % len(jets)], cave)
        jet_num += 1

        if falling_rock.can_fall(cave):
            falling_rock.fall(cave)
        else:
            break

# PART 2 

# Do stuff