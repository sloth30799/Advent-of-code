import re
import math

with open('./input.txt', 'r') as file:
    content = file.read().splitlines()

pattern = re.compile(r"mul\(\d{1,3},\s*\d{1,3}\)")

result = 0
for line in content:
    instructions: list[str] = pattern.findall(line)

    for m in instructions:
        replaced_mul = m.replace('mul(', '').replace(')', '')

        result += math.prod(map(int, replaced_mul.split(',')))


print(result)
