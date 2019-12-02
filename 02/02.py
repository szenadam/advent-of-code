data = open('./input.txt', 'r')


def print_data(data):
    for line in data.readlines():
        print(line.strip())


data_matrix = data.readline().strip().split(',')

for i in range(0, len(data_matrix) + 1, 4):
    print(data_matrix[i:i+4])
