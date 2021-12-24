import sys

def main():
    data = []
    input_file = 'sample_input.txt'
    input_file = 'input.txt'
    with open(input_file, 'r') as f:
        line = f.readline().strip()
        data = [int(i) for i in line.split(',')]
    print(data)

    lowest_pos = min(data)
    highest_pos = max(data)
    lowest = sys.maxsize

    for i in range(lowest_pos, highest_pos + 1):
        s = 0
        for j in data:
            fuel_consumption = abs(j - i)
            s += fuel_consumption
        if s < lowest:
            lowest = s
            lowest_pos = i

    print(lowest)
    print(lowest_pos)

    return 0


if __name__ == '__main__':
    main()
