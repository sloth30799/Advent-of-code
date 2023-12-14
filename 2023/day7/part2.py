import re
from collections import Counter
from functools import cmp_to_key

with open('./input.txt', 'r') as f:
    puzzle_input = f.read()

def get_type(hand):
    hand_without_j = list(filter(lambda x:x != 'J', hand))
    j_counts = hand.count('J')

    if j_counts == 5:
        return 6
    
    counts = sorted(Counter(hand_without_j).values(), reverse=True)

    if counts[0] + j_counts == 5:
        return 6
    if counts[0] + j_counts == 4:
        return 5
    if counts[0] + j_counts == 3 and counts[1] == 2:
        return 4
    if counts[0] + j_counts == 3:
        return 3
    if counts[0] + j_counts == 2 and counts[1] == 2:
        return 2
    if counts[0] + j_counts == 2:
        return 1
    return 0 

def compare(a, b):
    cards = 'J23456789TQKA'
    type_a = get_type(a[0])
    type_b = get_type(b[0])

    if type_a > type_b:
        return 1
    elif type_b > type_a:
        return -1

    for card_a, card_b in zip(a[0], b[0]):
        if card_a == card_b:
            continue
        a_wins = (cards.index(card_a) > cards.index(card_b))
        return 1 if a_wins else -1

def winning_total(puzzle_input):
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += (rank * int(bid))
    return total

print(winning_total(puzzle_input))

d_one = []
d_two = []

difference = list(set(d_one) - set(d_two))

print(difference)