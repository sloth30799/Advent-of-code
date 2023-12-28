def tilt_to(line, direction):
    mini_strings = line.split('#')
    result = []

    for mini in mini_strings:
        if direction == 'front':
            sorted_mini = sorted(list(mini), key=lambda x: (x != 'O', x))
        else:
            sorted_mini = sorted(list(mini), key=lambda x: (x == 'O', x))

        result.append(''.join(sorted_mini))
    
    return '#'.join(result)

def tilt_vertical(board, direction):
    new_board = []

    for line in zip(*board):
        if direction == 'north':
            line = tilt_to(''.join(line), 'front')
        else:
            line = tilt_to(''.join(line), 'back')

        new_board.append(line)

    new_board = list(zip(*new_board))

    return new_board

def tilt_horizontal(board, direction):
    new_board = []

    for line in board:
        if direction == 'west':
            line = tilt_to(''.join(line), 'front')
        else:
            line = tilt_to(''.join(line), 'back')

        new_board.append(line)

    return new_board

def part2():
    with open('./input.txt', 'r') as file:
        grid = file.read().splitlines()

    one_circle = ['north', 'west', 'south', 'east']
    seen_states = list()
    cycles = 0
    
    while True:
        current_state = tuple(tuple(row) for row in grid)

        if current_state in seen_states:
            seen_index = seen_states.index(current_state)
            loop_time = len(seen_states) - seen_index
            remaining_cycles = 1_000_000_000 - cycles

            # Calculate the effective position in the loop after remaining cycles
            effective_position = (remaining_cycles % loop_time) + seen_index

            # Retrieve the grid state at the effective position
            grid = seen_states[effective_position]
            break


        seen_states.append(current_state)

        for i in one_circle:
            if i == 'north' or i == 'south':
                grid = tilt_vertical(grid, i)
            else:
                grid = tilt_horizontal(grid, i)

        cycles += 1
        
    total_load = 0

    for i in range(len(grid)):
        total_load += (grid[i].count('O') * (len(grid) - i))

    print(total_load)

part2()
# 94255