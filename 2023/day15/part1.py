def hash_algorithm(hash_string):
    value = 0

    for char in hash_string:
        value += ord(char)

        value = (value * 17) % 256

    return value

def part1():
    with open('input.txt', 'r') as file:
        hashes = file.readline().split(',')

    total = 0

    for h in hashes:
        total += hash_algorithm(h)

    print(total)

part1()