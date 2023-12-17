def next_value_in_h(all_last_values, arr):
    difference = arr[2] - arr[1]
    last_difference = arr[len(arr) - 1] - arr[0]

    if difference != 0 and last_difference / difference == len(arr) - 1:
        all_last_values.append(arr[len(arr) - 1] + difference)

        return sum(all_last_values)

    new_arr = []
    for i, d in enumerate(arr):
        if i + 1 < len(arr):
            new_arr.append(arr[i + 1] - arr[i])

    all_last_values.append(arr[len(arr) - 1])

    return next_value_in_h(all_last_values, new_arr)


def part1():
    with open('./input.txt', 'r') as file:
        lines = [line.strip().split(' ') for line in file.readlines()]

    result = 0
    for line in lines:
        line = list(map(int, line))
        all_last_values = []

        result += next_value_in_h(all_last_values, line)

    print(result)


part1()
