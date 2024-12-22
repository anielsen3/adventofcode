import sys

def score_hand(hand):
    label_counts = [hand.count(label) for label in set(hand)]

    if 5 in label_counts:
        return 6 # Five of a kind
    
    if 4 in label_counts:
        return 5 # Four of a kind
    
    if 3 in label_counts:
        if  2 in label_counts:
            return 4 # Full House
        else:
            return 3 # Three of a kind
    
    if label_counts.count(2) == 2:
        return 2 # Two pair
    
    if label_counts.count(2) == 1:
        return 1 # One pair

    return 0 # High card

hands_bids = { hand: int(bid) for hand, bid in map(str.split, open(sys.argv[1]).readlines()) }

# Part 1
def sortkey_part1(hand):
    return [score_hand(hand)] + ['23456789TJQKA'.index(c) for c in hand]

print("1:", sum(hands_bids[h] * i for i, h in enumerate(sorted(hands_bids, key=sortkey_part1), 1)))

# Part 2
def flatten_list(xss):
    return [x for xs in xss for x in xs]

def possible_hands(hand):
    return flatten_list([possible_hands(hand.replace('J', card, 1)) for card in 'AKQT98765432']) if 'J' in hand else [hand]        

def sortkey_part2(hand):
    return [max(map(score_hand, possible_hands(hand)))] + ['J23456789TQKA'.index(c) for c in hand]

print("2:", sum(hands_bids[h] * i for i, h in enumerate(sorted(hands_bids, key=sortkey_part2), 1)))
