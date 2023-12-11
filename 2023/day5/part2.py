def reverse_map(maps, value):
    for map in maps:
        if value in range(map[0], map[0] + map[2]):
            difference = value - map[0]
            return map[1] + difference

    return value


def get_seed(data, value):
    for key in data.keys():
        value = reverse_map(data[key], value)

    return value


def get_lowest_location():
    with open('./example.txt') as file:
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

    seeds = data['seeds']
    data.pop('seeds', None)

    seeds_range = []
    seeds_start = []
    for index in range(0, len(seeds) - 1, 2):
        start, length = seeds[index:index+2]
        seeds_range.append(range(start, start+length))
        seeds_start.append(start)

    reversed_data = {}

    for key in reversed(data.keys()):
        reversed_data[key] = data[key]

    location = 0
    while True:
        seed = get_seed(reversed_data, location)

        if any(seed in s_range for s_range in seeds_range):
            for l in range(0, int(location / 2)):
                p_seed = get_seed(reversed_data, l)

                if any(p_seed in s_range for s_range in seeds_range):
                    print(location)
                    return

            for l in range(int(location / 2), location):
                p_seed = get_seed(reversed_data, l)

                if any(p_seed in s_range for s_range in seeds_range):
                    print(location)
                    return
            break

        location += 100


get_lowest_location()
# 37384987
# 67108864
