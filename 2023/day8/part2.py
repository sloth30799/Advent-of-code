import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def next_step(step, node):
    node = node[1:len(node) - 1].split(', ')

    return node[step]


def total_steps():
    with open('./input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    steps = lines[0]
    steps = [0 if step == 'L' else 1 for step in steps]
    nodes = {node.split(" = ")[0]: node.split(" = ")[1] for node in lines[2:]}

    nodes_with_a = list(filter(lambda x: x.endswith('A'), nodes))
    all_steps = []

    for i in range(len(nodes_with_a)):
        found_z = False
        steps_count = 0

        while found_z == False:
            for step in steps:
                nodes_with_a[i] = next_step(step, nodes[nodes_with_a[i]])

                steps_count += 1

                if nodes_with_a[i].endswith("Z"):
                    all_steps.append(steps_count)
                    found_z = True
                    break

    print(reduce(lcm, all_steps))


total_steps()