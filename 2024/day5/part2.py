from math import floor

with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

    rules = content[:content.index('')]
    updates = content[content.index('') + 1:]


def correct_update(update):
    corrected = [0] * len(update)

    for u in update:
        u_rule = list(filter(lambda r: u in r, rules))
        count = 0

        for n in update:
            if f"{u}|{n}" in u_rule:
                count += 1

        corrected[count] = u

    corrected.reverse()

    return corrected[floor(len(corrected) / 2)]


def check_update(update):
    corrected_list = []

    for [i, u] in enumerate(update):
        u_rule = list(filter(lambda r: u in r, rules))

        for n in update[i + 1:]:
            if f"{u}|{n}" not in u_rule:
                return correct_update(update)

        for p in update[:i]:
            if f"{p}|{u}" not in u_rule:
                return correct_update(update)

        corrected_list.append(u)

    return 0


result = 0
for update in updates:
    update_list = update.split(',')

    result += int(check_update(update_list))

print(result)
