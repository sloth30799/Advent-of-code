with open('./input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

def light_travel_expand():
    row_arr = set()
    col_arr = set()

    for x, line in enumerate(lines):
        for y, g in enumerate(line):
            if g == '#':
                row_arr.add(x)
                col_arr.add(y)

    new_lines = []

    for x, line in enumerate(lines):
        new_line = ''

        for y, g in enumerate(line):
            new_line += g
            if y not in col_arr:
                new_line += '.'

        new_lines.append(new_line)

        if x not in row_arr:
            added_line = '.' * len(new_line)
            new_lines.append(added_line)

    return new_lines

expanded = light_travel_expand()

def sum_lengths():
    galaxy_coordinates = []

    for x, line in enumerate(expanded):
        for y, g in enumerate(line):
            if g == '#':
                galaxy_coordinates.append([x,y])

    lengths = []

    for i, v1 in enumerate(galaxy_coordinates):
        for v2 in galaxy_coordinates[i+1:]:
            x_length = abs(v2[0] - v1[0])
            y_length = abs(v2[1] - v1[1])
            
            lengths.append(x_length + y_length)

    print(sum(lengths))

sum_lengths()

