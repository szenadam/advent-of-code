def main():
    infile = open('.\\input.txt', 'r')
    data = []
    matrix = []
    for i in infile.readlines():
        data.append(i.strip())
    for i in data:
        matrix.append([0 if j == '.' else 1 for j in list(i)])
    row, column = 0, 0
    num_of_trees = 0
    number_of_columns = len(matrix[0])
    while row < len(matrix):
        if matrix[row][column] == 1:
            num_of_trees += 1
        row += 1
        column = (column + 3) % number_of_columns
    print(num_of_trees)
    return 0

if __name__ == "__main__":
    main()