with open('./input.txt', 'r') as file:
    board = file.read().splitlines()

def tilt_north(line):
    mini_strings = line.split('#')
    result = []

    for mini in mini_strings:
        sorted_mini =  sorted(list(mini), key=lambda x: (x != 'O', x))

        result.append(''.join(sorted_mini))
    
    return '#'.join(result)

def part1():
    new_board = []

    for line in zip(*board):
        line = tilt_north(''.join(line))

        new_board.append(line)

    new_board = list(zip(*new_board))
    total_load = 0

    for i in range(len(new_board)):
        total_load += (new_board[i].count('O') * (len(new_board) - i))

    print(total_load)

part1()