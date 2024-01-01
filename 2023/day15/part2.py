def hash_algorithm(hash_string):
    value = 0

    for char in hash_string:
        value += ord(char)

        value = (value * 17) % 256

    return value


def part2():
    with open('input.txt', 'r') as file:
        hashes = file.readline().split(',')

    seen_boxes = dict()

    for h in hashes:
        if '-' in h:
            [name, value] = h.split('-')

            if name in seen_boxes.keys():
                seen_boxes.pop(name)

        if '=' in h:
            [name, value] = h.split('=')

            seen_boxes[name] = 0 if h[-1] == '=' else h[-1]

    count = dict()
    total = 0

    for key, value in seen_boxes.items():
        box_number = hash_algorithm(key)

        if box_number in count.keys():
            count[box_number] += 1
        else:
            count[box_number] = 1

        total += ((box_number + 1) * count[box_number] * int(value))

    print(total)

part2()