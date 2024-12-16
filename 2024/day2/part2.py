import numpy as np

with open('./input.txt', 'r') as file:
    content = [list(map(int, line.split(' ')))
               for line in file.read().splitlines()]


def cutout(seq, index):
    return seq[:index] + seq[index + 1:]


def check(levels: list) -> bool:
    asOrder = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
    dsOrder = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))

    if not asOrder and not dsOrder:
        return False
    else:
        differences = np.diff(levels)
        return all(d >= 1 and d <= 3 for d in map(abs, differences))


safe_count = 0
for levels in content:
    check_completed = False

    while (not check_completed):
        if check(levels):
            safe_count += 1
            check_completed = True
            break

        for i in range(len(levels)):
            newLevels = cutout(levels, i)

            if check(newLevels):
                check_completed = True
                safe_count += 1
                break

        check_completed = True


print(safe_count)
