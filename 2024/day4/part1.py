from operator import add

with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

WORD = 'XMAS'

max_x = len(content) - 1
max_y = len(content[0]) - 1


def get_text(point, plus):
    text = content[point[0]][point[1]]
    for _ in range(3):
        point = list(map(add, point, plus))
        if point[0] >= 0 and point[0] <= max_x and point[1] >= 0 and point[1] <= max_y:
            text += content[point[0]][point[1]]
        else:
            return 0

    return 1 if text == WORD else 0


def check_xmas(point):
    [x, y] = point

    # Directions with boundary checks
    directions = {
        'left': (0, -1) if y >= 3 else False,
        'top': (-1, 0) if x >= 3 else False,
        'right': (0, 1) if y + 3 <= max_y else False,
        'bottom': (1, 0) if x + 3 <= max_x else False,
        'top-left': (-1, -1) if x >= 3 and y >= 3 else False,
        'top-right': (-1, 1) if x >= 3 and y + 3 <= max_y else False,
        'bottom-left': (1, -1) if x + 3 <= max_x and y >= 3 else False,
        'bottom-right': (1, 1) if x + 3 <= max_x and y + 3 <= max_y else False
    }

    count = 0
    for vector in directions.values():
        if vector:  # Only process valid directions
            count += get_text(point, vector)
    return count


# Main loop to traverse the grid and count occurrences
count = 0
for x, line in enumerate(content):
    for y, w in enumerate(line):
        if content[x][y] == 'X':
            count += check_xmas([x, y])

print("Total count of 'XMAS':", count)
