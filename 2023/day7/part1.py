file = open("./example.txt").read().strip().split("\n")
lines = list(map(lambda x: x.split(' '), file))

strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def hand_type(hand):
    hand_set = set(hand)

    types = { 1: 'Five of a kind', 4: 'One pair', 5: 'High card' }

    if len(hand_set) == 2:
        char_count = {}
        for char in hand:
            char_count[char] = char_count.get(char, 0) + 1

        if len(char_count.keys()) == 2:
            return 'Full house'
        else:
            return 'Three of a kind'

    elif len(hand_set) == 3:
        char_count = {}
        for char in hand:
            char_count[char] = char_count.get(char, 0) + 1

        count_of_twos = sum(value == 2 for value in char_count.values())

        if count_of_twos == 2:
            return "Two pair"
        else:
            return "Three of a kind"

    return types[len(hand_set)]


all_hands = {
    'High card': [],
    'One pair': [],
    'Two pair': [],
    'Three of a kind': [],
    'Full house': [],
    'Four of a kind': [],
    'Five of a kind': []
}

for line in lines:
    all_hands[hand_type(line[0])].append(line)

print(all_hands)

for key in all_hands.keys():
    for i in all_hands[key]:
        print(i)

# check strength and sort
# calculate