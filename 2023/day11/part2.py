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

    expanded_x = [i for i in range(len(lines)) if i not in row_arr]
    expanded_y = [i for i in range(len(lines[0])) if i not in col_arr]

    return [expanded_x, expanded_y]

[expanded_x, expanded_y] = light_travel_expand()

def sum_lengths():
    galaxy_coordinates = []

    for x, line in enumerate(lines):
        for y, g in enumerate(line):
            if g == '#':
                galaxy_coordinates.append([x,y])

    lengths = []

    for i, v1 in enumerate(galaxy_coordinates):
        for v2 in galaxy_coordinates[i+1:]:
            x_length = abs(v2[0] - v1[0])
            y_length = abs(v2[1] - v1[1])

            for x in expanded_x:
                if x >= min(v2[0], v1[0]) and x <= max(v2[0], v1[0]):
                    x_length += (1000000 - 1)
                    
            for y in expanded_y:
                if y >= min(v2[1], v1[1]) and y <= max(v2[1], v1[1]):
                    y_length += (1000000 - 1)

            lengths.append(x_length + y_length)

    print(sum(lengths))

sum_lengths()

# 685038186836
