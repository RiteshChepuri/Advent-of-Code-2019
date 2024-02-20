positions = list(map(int, open("2.in").read().split(",")))
positions[1] = 12
positions[2] = 2
i = 0

while True:
    opcode, a, b, out = positions[i : i + 4]

    if opcode == 99:
        break
    elif opcode == 1:
        positions[out] = positions[a] + positions[b]
    else:
        positions[out] = positions[a] * positions[b]

    i += 4


print(positions[0])


position = list(map(int, open("2.in").read().split(",")))


def get_output_for(position, a, b):
    position[1] = a
    position[2] = b
    i = 0

    while True:
        opcode, a, b, out = position[i : i + 4]

        if opcode == 99:
            return position[0]
        elif opcode == 1:
            position[out] = position[a] + position[b]
        else:
            position[out] = position[a] * position[b]

        i += 4


def find_answer():
    for a in range(100):
        for b in range(100):
            if get_output_for(list(position), a, b) == 19690720:
                return 100 * a + b


print(find_answer())
