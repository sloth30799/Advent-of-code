import re
import math

with open('./input.txt', 'r') as file:
    content = file.read()

pattern = re.compile(r"(do\(\)|don't\(\)|mul\(\d{1,3},\s*\d{1,3}\))")
instructions: list[str] = pattern.findall(content)

result = 0
disable_enable_instructions = ["don't()", "do()"]
current_enabled = True

for i in instructions:
    if i in disable_enable_instructions:
        current_enabled = i == "do()"

    print(i, current_enabled)

    if current_enabled and i not in disable_enable_instructions:
        replaced_mul = i.replace('mul(', '').replace(')', '')

        result += math.prod(map(int, replaced_mul.split(',')))


print(result)
