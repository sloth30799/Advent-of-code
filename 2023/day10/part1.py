with open('./input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def go_vertical():
    global x, y, prev_x, prev_y
    if x - 1 == prev_x:
        prev_x, prev_y = x, y
        x += 1
    else:
        prev_x, prev_y = x, y
        x -= 1


def go_horizontal():
    global x, y, prev_x, prev_y
    if y - 1 == prev_y:
        prev_x, prev_y = x, y
        y += 1
    else:
        prev_x, prev_y = x, y
        y -= 1


def go_n_e():
    global x, y, prev_x, prev_y
    if x - 1 == prev_x:
        prev_x, prev_y = x, y
        y += 1
    else:
        prev_x, prev_y = x, y
        x -= 1


def go_n_w():
    global x, y, prev_x, prev_y
    if x - 1 == prev_x:
        prev_x, prev_y = x, y
        y -= 1
    else:
        prev_x, prev_y = x, y
        x -= 1


def go_s_w():
    global x, y, prev_x, prev_y
    if y - 1 == prev_y:
        prev_x, prev_y = x, y
        x += 1
    else:
        prev_x, prev_y = x, y
        y = y - 1


def go_s_e():
    global x, y, prev_x, prev_y
    if x + 1 == prev_x:
        prev_x, prev_y = x, y
        y += 1
    else:
        prev_x, prev_y = x, y
        x += 1


maps = {'|': go_vertical, '-': go_horizontal,
        'L': go_n_e, 'J': go_n_w,
        '7': go_s_w, 'F': go_s_e, }


def part1():
    global x, y, prev_x, prev_y
    f_steps = {}

    for count in range(1, 5):
        start_index = []

        for i, line in enumerate(lines):
            if 'S' in line:
                start_index = [i, line.index('S')]

        [x, y] = [prev_x, prev_y] = start_index

        steps = 0

        if count == 1:
            y += 1

            if y >= len(lines[0]) or lines[x][y] == '.':
                f_steps['right'] = 0
                continue

            while True:
                if steps > 0 and lines[x][y] == 'S':
                    break

                steps += 1
                maps[lines[x][y]]()

            f_steps['right'] = (steps + 1) / 2

        if count == 2:
            y -= 1

            if y <= 0 or lines[x][y] == '.':
                f_steps['left'] = 0
                continue

            while True:
                if steps > 0 and lines[x][y] == 'S':
                    break

                steps += 1
                maps[lines[x][y]]()

            f_steps['left'] = (steps + 1) / 2

        if count == 3:
            x -= 1

            if x <= 0 or lines[x][y] == '.':
                f_steps['top'] = 0
                continue

            while True:
                if steps > 0 and lines[x][y] == 'S':
                    break

                steps += 1
                maps[lines[x][y]]()

            f_steps['top'] = (steps + 1) / 2

        if count == 4:
            x += 1

            if x >= len(lines) or lines[x][y] == '.':
                f_steps['bottom'] = 0
                continue

            while True:
                if steps > 0 and lines[x][y] == 'S':
                    break

                steps += 1
                maps[lines[x][y]]()

            f_steps['bottom'] = (steps + 1) / 2

    print(max(f_steps.items()))


part1()
