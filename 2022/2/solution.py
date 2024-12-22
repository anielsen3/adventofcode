INPUT = open("input1.txt").readlines()

# A = Rock, B = Paper, C = Scissors
shape_score   = { 'A': 1, 'B': 2, 'C': 3 }
outcome_score = { ('A', 'A'): 3, ('A', 'B'): 6, ('A', 'C'): 0,
                  ('B', 'A'): 0, ('B', 'B'): 3, ('B', 'C'): 6,
                  ('C', 'A'): 6, ('C', 'B'): 0, ('C', 'C'): 3 }

def score_round(line, find_self_play):
    (l, r) = line.strip().split()
    self_play = find_self_play(l, r)
    return outcome_score[(l, self_play)] + shape_score[self_play]

def score(find_self_play):
    return sum(score_round(line, find_self_play) for line in INPUT)


def find_self_play1(l, r):
    return { 'X': 'A', 'Y': 'B', 'Z': 'C' }[r]

print(f"1: {score(find_self_play1)}")


def find_self_play2(l, r):
    for ((o, s), v) in outcome_score.items():
        if (o == l and v == { 'X': 0, 'Y': 3, 'Z': 6 }[r]):
            return s

print(f"2: {score(find_self_play2)}")
