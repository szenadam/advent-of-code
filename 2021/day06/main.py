
def main():
    data = []

    with open('input.txt', 'r') as f:
        line = f.readline()
        for i in line.split(','):
            data.append(int(i))

    # get the count of the fish with the same number of days left
    fish = [data.count(i) for i in range(9)]

    for i in range(256):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)

    print(sum(fish))

    return 0


if __name__ == '__main__':
    main()
