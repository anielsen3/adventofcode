import sys

INPUT = [l.strip() for l in open(sys.argv[1]).readlines()]

def contains(p1, p2):
    (l1, r1) = p1.split("-")
    (l2, r2) = p2.split("-")
    l1 = int(l1)
    r1 = int(r1)
    l2 = int(l2)
    r2 = int(r2)
    if ((l1 <= l2) and (r1 >= r2)) or ((l2 <= l1) and (r2 >= r1)):
        return True
    else:
        return False

def overlaps(p1, p2):
    (l1, r1) = p1.split("-")
    (l2, r2) = p2.split("-")
    l1 = int(l1)
    r1 = int(r1)
    l2 = int(l2)
    r2 = int(r2)
    if ((l1 <= l2 and r1 >= l2) or (l2 <= l1 and r2 >= l1)):
        return True
    else:
        return False

print("1:", sum([contains(*line.split(",")) for line in INPUT]))
print("2:", sum([overlaps(*line.split(",")) for line in INPUT]))


    