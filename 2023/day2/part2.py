import re

game_pattern = re.compile(r'Game (\d+): (.+)$')
pattern = re.compile(r'(\d+)\s*(\w+)') 

def check_game(text):
    game = game_pattern.search(text)
    game_data = game.group(2)

    arr = game_data.split(';')
    max_cubes = {}

    for line in arr:
        matches = pattern.findall(line)

        for match in matches:
            if match[1] not in max_cubes.keys() or max_cubes[match[1]] < int(match[0]):
                max_cubes[match[1]] = int(match[0])


    result = 1
    for value in max_cubes.values():
        result *= value

    return result


def get_possible_games_no():
    with open('./data.txt', 'r') as file:
        lines = file.readlines()

        result = list(map(check_game, lines))

        return sum(result)

print(get_possible_games_no())