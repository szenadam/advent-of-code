
def main():
    data = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        for i in line.split(','):
            data.append(int(i))
    print(data)

    for i in range(1, 80 + 1):
        zero_count = 0
        for j, k in enumerate(data):
            data[j] = data[j] - 1
            if k == 0:
                zero_count += 1
                data[j] = 6
        if zero_count > 0:
            for i in range(zero_count):
                data.append(8)
        # print(data)

    print(len(data))

    return 0

if __name__ == '__main__':
    main()