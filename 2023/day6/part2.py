file = open("./input.txt").read().strip().split("\n")

time = int(file[0].split(":")[1].replace(' ', ''))

distance = int(file[1].split(":")[1].replace(' ', ''))

def winning_ways(time, dis):
    ways = []
    for x in range(14, time):
        if x * (time - x) > dis:
            ways.append(x)

    return len(ways)

print(winning_ways(time, distance))