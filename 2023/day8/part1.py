def next_step(step, node):
    step_map = { 'L': 0, 'R': 1 }
    node = node[1:len(node) - 1].split(', ')

    return node[step_map[step]]


def total_steps():
    with open('./input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    steps = lines[0]
    nodes = {node.split(" = ")[0]: node.split(" = ")[1] for node in lines[2:]}

    node = 'AAA'
    steps_count = 0

    while node != 'ZZZ':
        for step in steps:
            node = next_step(step, nodes[node])
            steps_count += 1

            if node == 'ZZZ':
                break

    print(node, steps_count)

total_steps()
# 16343