from itertools import product

with open('./input.txt', 'r') as file:
    lines = [line.strip().split(' ') for line in file.readlines()]


replacement_options = ['.', '#']


def get_possible_arrangements(line):
    original_string = line[0]
    hash_counts = [int(i) for i in line[1].split(',')]

    needed_hash = sum(hash_counts) - original_string.count('#')

    all_patterns = [''.join(p) for p in product(
        replacement_options, repeat=original_string.count('?'))]

    # Print the result
    new_patterns = 0
    for pattern in all_patterns:
        if pattern.count('#') == needed_hash:
            new_pattern = original_string
            for char in pattern:
                new_pattern = new_pattern.replace('?', char, 1)

            if list(map(len, new_pattern.replace('.', ' ').split())) == hash_counts:
                new_patterns += 1

    return new_patterns


def total_possible_arrangements():
    total = 0
    for line in lines:
        total += get_possible_arrangements(line)

    print(total)


total_possible_arrangements()
