def main():
    infile = open('.\\input.txt', 'r')
    data = []
    for i in infile.readlines():
        data.append(int(i.strip()))

    numbers = (0, 0)
    result = 0
    for i in data:
        r = 2020 - i
        if r in data:
            result = r * i
            numbers = (i, r)
            break

    print(numbers)
    print('Result:', result)


if __name__ == "__main__":
    main()
