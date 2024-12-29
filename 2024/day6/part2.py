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
memo_positions = {}
ob_positions = 0


def find_start():
    for row_index, row in enumerate(content):
        for col_index, value in enumerate(row):
            if value == '^':
                current_point[0] = row_index
                current_point[1] = col_index

                walked_tiles.add(tuple(current_point))

                return True

    return None


def simulate_walk(point, direction):
    key = f"{point}|{direction}"

    if key in memo_positions:
        return memo_positions[tuple(point, direction)]

    start_point = c_point = point
    c_direction = direction

    while True:
        next_point = [c_point[0] + c_direction[0],
                      c_point[1] + c_direction[1]]

        if (-1 in next_point) or len(content) == next_point[0] or len(content[next_point[0]]) == next_point[1]:
            memo_positions[key] = False
            return False

        if next_point == start_point:
            memo_positions[key] = True
            return True

        if content[next_point[0]][next_point[1]] == '#':
            c_direction = right_turns[c_direction]
        else:
            c_point = next_point


def walk():
    global current_direction, current_point, result, ob_positions

    while True:
        next_point = [current_point[0] + current_direction[0],
                      current_point[1] + current_direction[1]]

        if (-1 in next_point) or len(content) == next_point[0] or len(content[next_point[0]]) == next_point[1]:
            break  # Exit the loop

        if content[next_point[0]][next_point[1]] == '#':
            current_direction = right_turns[current_direction]
        else:
            current_point = next_point
            if content[current_point[0]][current_point[1]] in '.^':
                walked_tiles.add(tuple(current_point))

                ob_direction = right_turns[current_direction]

                if simulate_walk(current_point, ob_direction):
                    ob_positions += 1


if find_start():
    walk()

print(ob_positions)
