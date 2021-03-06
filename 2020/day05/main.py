def main():

    infile = open('.\\example.txt', 'r')

    data = []

    for i in infile.readlines():
        data.append(i.strip())

    print(data)

    places = []

    for i in data:
        j = list(i)
        print(j)
        row_total = 127
        row_min = 0
        row_max = 127
        for k in range(7):
            if j[k] == 'F':
                
            else:
                row = row /

    return 0

if __name__ == "__main__":
    main()