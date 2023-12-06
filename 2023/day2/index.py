import re

cubes = { "red": 12, "green": 13, "blue": 14 }
game_no_pattern = re.compile(r'Game (\d+):')
game_pattern = re.compile(r'Game (\d+): (.+)$')
pattern = re.compile(r'(\d+)\s*(\w+)') 

def check_game(text):
    game = game_pattern.search(text)
    game_number = int(game.group(1))
    game_data = game.group(2)

    arr = game_data.split(';')

    for line in arr:
        matches = pattern.findall(line)

        for match in matches:
            if int(match[0]) > cubes[match[1]]:
                return game_number


def get_possible_games_no():
    with open('./data.txt', 'r') as file:
        lines = file.readlines()

        result = list(map(check_game, lines))

        result_one = list(filter(None, result))
        
        return sum(result_one)

def sum_of_100_id():
    result = 0
    for i in range(100):
        result += i + 1

    print(result)
    return result

print(sum_of_100_id() - get_possible_games_no())
