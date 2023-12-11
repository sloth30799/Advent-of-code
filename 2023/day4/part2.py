import re

pattern = r'Card\s+(\d+):\s+(.*)'

def check_card(line):
    card = re.match(pattern, line)
    card_data = card.group(2)

    [ winning_no, ur_no ] = card_data.split(' | ')
    winning_no = winning_no.split(' ')
    ur_no = ur_no.split(' ')

    match = 0
    for number in winning_no:
        if number.isdigit() and number in ur_no:
            match += 1

    return {
        "count": 1,
        "match": match
    }

def total_points():
    with open('./data.txt') as file:
        lines = [line.strip() for line in file.readlines()]

        total = []
        for line in lines:
            total.append(check_card(line))

        total_sum = 0

        for index, count_match in enumerate(total):
            if count_match['match'] > 0:
                for i in range(index + 1, index + count_match['match'] + 1):
                    total[i]['count'] += count_match['count']

            total_sum += count_match['count']

        print(total_sum)


total_points()
# 6189740