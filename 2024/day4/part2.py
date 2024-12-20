from operator import add

with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

max_x = len(content) - 1
max_y = len(content[0]) - 1


def check_xmas(point):
    [x, y] = point

    if x >= max_x or y >= max_y or x < 1 or y < 1:
        return 0 

    surrounding_indexes = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    words = list(
        map(lambda w: content[w[0] + x][w[1] + y], surrounding_indexes))

    if words.count('M') == 2 and words.count('S') == 2 and words[0] != words[2]:
        return 1

    return 0


count = 0
for x, line in enumerate(content):
    for y, w in enumerate(line):
        if content[x][y] == 'A':
            count += check_xmas([x, y])

print("Total count:", count)
