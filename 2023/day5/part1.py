def map_s_to_d(maps, values):
    updated_values = {}

    for m in maps:
        min_range = m[1]
        max_range = m[1] + m[2]

        for v in values:
            if v >= min_range and v <= max_range:
                source_difference = v - m[1]
                destination_value = m[0] + source_difference

                updated_values.setdefault(v, destination_value)

    destination_values = []

    for source_v in values:
        destination_values.append(updated_values.get(source_v, source_v))

    return destination_values


def get_lowest_location():
    with open('./data.txt') as file:
        lines = [line.strip() for line in file.readlines()]

    data = {}
    current_key = None
    current_map = []

    for line in lines:
        if ':' in line:
            key, values = line.split(':')
            current_key = key.strip().lower()
            current_map = list(map(int, values.strip().split()))
        elif line.strip():
            current_map.append(list(map(int, line.strip().split())))
        else:
            data[current_key] = current_map

    data[current_key] = current_map

    current_values = data['seeds']

    for k in data.keys():
        if k != 'seeds':
            current_values = map_s_to_d(data[k], current_values)

    print(min(current_values))


get_lowest_location()
