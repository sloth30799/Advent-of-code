import re

pattern = r':\s*(.*)'

def check_card(text):
    card =  re.search(pattern, text)
    card_data = card.group(1)

    [ winning_no, ur_no ] = card_data.split(' | ')
    winning_no = winning_no.split(' ')
    ur_no = ur_no.split(' ')

    points = 0
    for number in winning_no:
        if number.isdigit() and number in ur_no:
            if points >= 1:
                points *= 2
            else:
                points += 1

    return points

def total_points():
    with open('./data.txt') as file:
        lines = [line.strip() for line in file.readlines()]

        total = 0
        for line in lines:
            total += check_card(line)

        print(total)

total_points()