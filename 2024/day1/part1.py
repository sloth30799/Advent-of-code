with open('./input.txt', 'r') as file:
    content = [x.rstrip().split('   ') for x in file.readlines()]

sortedList1 = list(sorted([int(x[0]) for x in content]))
sortedList2 = list(sorted([int(x[1]) for x in content]))

part1 = sum([abs(a - b) for (a, b) in zip(sortedList1, sortedList2)])

print(part1)
