with open('./input.txt', 'r') as file:
    content = [x.rstrip().split('   ') for x in file.readlines()]


counts = {}

for [x, y] in content:
    if y not in counts:
        counts[y] = 1
    else:
        counts[y] += 1

result = sum([int(x) * (counts[x] if x in counts else 0)
             for [x, _] in content])

print(result)
