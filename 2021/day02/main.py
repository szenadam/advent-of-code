def main():

    #input = open('sample_input.txt')
    input = open('input.txt')
    data = []

    for line in input.readlines():
        direction, units = line.strip().split(' ')
        data.append((direction, int(units)))

    print(data)

    part_two(data)

    return 0


def part_two(data):
    position, depth, aim = 0, 0, 0
    for movement in data:
        direction, units = movement
        if direction == 'forward':
            position += units
            if aim == 0:
                depth = depth
            else:
                depth += units * aim
        elif direction == 'up':
            aim -= units
        elif direction == 'down':
            aim += units

    print("Position: %s, Depth: %s" % (position, depth))
    print("Result:", position * depth)


def part_one(data):
    position, depth = 0, 0
    for movement in data:
        direction, units = movement
        if direction == 'forward':
            position += units
        elif direction == 'up':
            depth -= units
        elif direction == 'down':
            depth += units

    print("Position: %s, Depth: %s" % (position, depth))
    print("Result:", position * depth)


if __name__ == "__main__":
    main()
