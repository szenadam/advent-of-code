

def main():

    #input = open('sample_input.txt', 'r')
    input = open('input.txt', 'r')

    data = []

    for line in input.readlines():
        data.append(int(line.strip()))

    part_one(data)
    part_two(data)

    input.close()
    return 0


def part_two(data):
    increases = 0
    nochange = 0
    decreases = 0

    windows = []

    for a, b, c in zip(data, data[1:], data[2:]):
        s = a + b + c
        windows.append(s)

    for previous, current in zip(windows, windows[1:]):
        a = previous
        b = current

        if a < b:
            increases += 1
        elif a == b:
            nochange += 1
        else:
            decreases += 1

    print(increases, nochange, decreases)

def part_one(data):
    increases = 0
    decreases = 0

    for previous, current in zip(data, data[1:]):
        a = previous
        b = current

        if a < b:
            increases += 1
        elif a > b:
            decreases += 1

    print(increases, decreases)

if __name__ == "__main__":
    main()