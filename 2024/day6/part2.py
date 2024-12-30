with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

current_point = [0, 0]
current_direction = (-1, 0)

right_turns = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

walked_tiles = set()
visited_positions = {}
ob_positions = 0


def find_start():
    for row_index, row in enumerate(content):
        for col_index, value in enumerate(row):
            if value == '^':
                current_point[0] = row_index
                current_point[1] = col_index
                walked_tiles.add((tuple(current_point), current_direction))
                return True
    return False


def simulate_walk(point, direction):
    visited_path = set()
    c_point = list(point)
    c_direction = direction

    while True:
        next_point = (c_point[0] + c_direction[0], c_point[1] + c_direction[1])

        if next_point[0] < 0 or next_point[0] >= len(content) or \
           next_point[1] < 0 or next_point[1] >= len(content[next_point[0]]):
            return False

        if (next_point, c_direction) in visited_path:
            return False
        visited_path.add((next_point, c_direction))

        if content[next_point[0]][next_point[1]] == '#':
            c_direction = right_turns[c_direction]
        else:
            c_point = list(next_point)

        if (next_point, c_direction) in walked_tiles:
            return True


def walk():
    global current_direction, current_point, ob_positions

    while True:
        next_point = (current_point[0] + current_direction[0],
                      current_point[1] + current_direction[1])

        if next_point[0] < 0 or next_point[0] >= len(content) or \
           next_point[1] < 0 or next_point[1] >= len(content[next_point[0]]):
            break

        if content[next_point[0]][next_point[1]] == '#':
            current_direction = right_turns[current_direction]
        else:
            current_point[0], current_point[1] = next_point
            if content[current_point[0]][current_point[1]] in '.^':
                walked_tiles.add((tuple(current_point), current_direction))

                ob_direction = right_turns[current_direction]
                if simulate_walk(tuple(current_point), ob_direction):
                    ob_positions += 1


if find_start():
    walk()

print(ob_positions)
