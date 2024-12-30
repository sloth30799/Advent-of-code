from itertools import product
from math import prod

with open('./input.txt', 'r') as file:
    content = [line.split(': ') for line in file.read().splitlines()]
    equations = [[int(line[0]), list(map(int, line[1].split()))]
               for line in content]


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


def check_valid_equation(target, numbers):
    operator_combinations = product(['+', '*'], repeat=len(numbers) - 1)
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == target:
            return True
    return False


total = 0
for target, numbers in equations:
    if check_valid_equation(target, numbers):
        total += target

print(total)
