import re


def get_index_form_str(s):
    pattern = r'\d+'

    matches = re.finditer(pattern, s)

    indexes_and_numbers = []

    for match in matches:
        number = match.group()
        left_index = max(0, match.start() - 1)
        right_index = min(match.end(), len(s) - 1)

        indexes_and_numbers.append({
            "left_index": left_index,
            "right_index": right_index,
            "number": number
        })

    return indexes_and_numbers


def check_one_line_symbols(line, index_and_num):
    start = int(index_and_num['left_index'])
    end = int(index_and_num['right_index']) + 1

    for i in range(start, end):
        if not line[i].isdigit() and line[i] != '.':
            return index_and_num['number']


def check_symbols(above, below, index_and_num):
    start = int(index_and_num['left_index'])
    end = int(index_and_num['right_index']) + 1

    for i in range(start, end):
        if not above[i].isdigit() and above[i] != '.' or not below[i].isdigit() and below[i] != '.':
            return index_and_num['number']
    return None


def get_gear_number():
    with open('./data.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    gears = []

    for index, line in enumerate(lines):
        num_indexes = get_index_form_str(line)

        if num_indexes is not None:
            for num_index in num_indexes:
                lindex, rindex = num_index['left_index'], num_index['right_index']

                if lindex != 0 and line[lindex] != '.' or rindex != len(line) - 1 and line[rindex] != '.':
                    gears.append(num_index['number'])
                else:
                    if index == 0:
                        gear = check_one_line_symbols(
                            lines[index + 1], num_index)
                        gears.append(gear)

                    elif index == len(lines) - 1:
                        gear = check_one_line_symbols(
                            lines[index - 1], num_index)
                        gears.append(gear)

                    else:
                        gear = check_symbols(
                            lines[index - 1], lines[index + 1], num_index)
                        gears.append(gear)

    return sum(int(x) for x in gears if x is not None)


print(get_gear_number())
