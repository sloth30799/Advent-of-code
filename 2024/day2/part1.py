import numpy as np

with open('./input.txt', 'r') as file:
    content = [list(map(int, line.split(' ')))
               for line in file.read().splitlines()]


def check(levels: list) -> bool:
    asOrder = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
    dsOrder = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))

    if not asOrder and not dsOrder:
        return False
    else:
        differences = np.diff(levels)
        return all(d >= 1 and d <= 3 for d in map(abs, differences))


safe_count = sum(1 for levels in content if check(levels))

print(safe_count)