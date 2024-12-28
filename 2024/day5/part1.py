from math import floor

with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

    rules = content[:content.index('')]
    updates = content[content.index('') + 1:]


def check_update(update):
    for [i, u] in enumerate(update):
        u_rule = list(filter(lambda r: u in r, rules))

        for n in update[i + 1:]:
            if f"{u}|{n}" not in u_rule:
                return False

        for p in update[:i]:
            if f"{p}|{u}" not in u_rule:
                return False

    return True


result = 0
for update in updates:
    update_list = update.split(',')
    
    if (check_update(update_list)):
        result += int(update_list[floor(len(update_list) / 2)])

print(result)
