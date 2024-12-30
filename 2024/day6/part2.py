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


def find_start():
    for row_index, row in enumerate(content):
        for col_index, value in enumerate(row):
            if value == '^':
                return [row_index, col_index], (-1, 0)
    return None, None


def simulate_patrol(map_with_obstruction, start_point, start_direction):
    current_point = start_point[:]
    current_direction = start_direction
    visited_states = set()

    while True:
        state = (current_point[0], current_point[1], current_direction)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        next_point = [current_point[0] + current_direction[0],
                      current_point[1] + current_direction[1]]

        if (-1 in next_point or
            next_point[0] >= len(map_with_obstruction) or
                next_point[1] >= len(map_with_obstruction[next_point[0]])):
            return False  # Guard leaves the map

        if map_with_obstruction[next_point[0]][next_point[1]] == '#':
            current_direction = right_turns[current_direction]
        else:
            current_point = next_point


def count_valid_obstructions():
    start_point, start_direction = find_start()
    valid_positions = 0

    for row_index, row in enumerate(content):
        for col_index, value in enumerate(row):
            if value == '.':
                # Place obstruction temporarily
                map_with_obstruction = [list(row) for row in content]
                map_with_obstruction[row_index][col_index] = '#'

                if simulate_patrol(map_with_obstruction, start_point, start_direction):
                    valid_positions += 1

    return valid_positions


if __name__ == "__main__":
    result = count_valid_obstructions()
    print(result)
