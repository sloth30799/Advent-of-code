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

def find_start():
    for row_index, row in enumerate(content):
        for col_index, value in enumerate(row):
            if value == '^':
                current_point[0] = row_index
                current_point[1] = col_index
                
                walked_tiles.add(tuple(current_point))

                return True

    return None


def walk():
    global current_direction, current_point, result

    while True:
        next_point = [current_point[0] + current_direction[0],
                      current_point[1] + current_direction[1]]

        if (-1 in next_point) or len(content) == next_point[0] or len(content[next_point[0]]) == next_point[1]:
            print(len(walked_tiles))
            break  # Exit the loop

        if content[next_point[0]][next_point[1]] == '#':
            current_direction = right_turns[current_direction]
        else:
            current_point = next_point
            if content[current_point[0]][current_point[1]] == '.':
                walked_tiles.add(tuple(current_point))


if find_start():
    walk()
