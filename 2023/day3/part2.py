import re


def get_star_index(txt):
    pattern = r'\*'

    matches = re.finditer(pattern, txt)

    all_stars = []

    for match in matches:
        lindex = max(0, match.start() - 1)
        rindex = min(match.start() + 1, len(txt))

        all_stars.append([lindex, rindex])

    return all_stars if len(all_stars) > 0 else None


def get_num_indexes(txt):
    pattern = r'\d+'

    num_indexes = []
    matches = re.finditer(pattern, txt)

    for match in matches:
        number = match.group()
        start_index = match.start()
        end_index = match.end()

        indexes = list(range(start_index, end_index))

        num_indexes.append([number, indexes])

    return num_indexes


def get_gears(line, indexes):
    line_num_i = get_num_indexes(line)

    gears = []

    for i in range(indexes[0], indexes[1] + 1):
        for num_i in line_num_i:
            if i in num_i[1]:
                gears.append(int(num_i[0]))

    return list(set(gears))


def get_gears_ratio():
    with open('./data.txt') as file:
        lines = [line.strip() for line in file.readlines()]

    gear_ratios = []

    for index, line in enumerate(lines):
        star_indexes = get_star_index(line)

        if star_indexes is not None:
            for star_index in star_indexes:
                above_line_gear = get_gears(
                    lines[index - 1], star_index) if index > 0 else None

                line_gear = get_gears(line, star_index)

                below_line_gear = get_gears(
                    lines[index + 1], star_index) if index < len(lines) - 1 else None

                gears = above_line_gear + line_gear + below_line_gear
                gears = list(filter(lambda x: x is not None, gears))

                if len(gears) == 2:
                    gear_ratios.append(gears[0] * gears[1])

    return sum(gear_ratios)


print(get_gears_ratio())
# 66462651
# 73646890
