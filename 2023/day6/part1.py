file = open("./input.txt").read().strip().split("\n")

times = file[0].split(":")[1].split(' ')
times = [int(x) for x in times if x.isdigit()]

distances = file[1].split(":")[1].split(' ')
distances = [int(x) for x in distances if x.isdigit()]

def winning_ways(time, dis):
    ways = []
    for x in range(1, time):
        if x * (time - x) > dis:
            ways.append(x)

    return len(ways)


def get_result():
    all_ways = 1
    for i in range(len(times)):
        ways = winning_ways(times[i], distances[i])
        all_ways *= ways

    print(all_ways)

get_result()