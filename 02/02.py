data = open('./input.txt', 'r')

def print_data(data):
    for line in data.readlines():
        print(line.strip())

def parse_opcode(data_matrix, opcode):
    if opcode[0] == 1:
        data_matrix[opcode[3]] = data_matrix[opcode[1]] + data_matrix[opcode[2]]
    elif opcode[0] == 2:
        data_matrix[opcode[3]] = data_matrix[opcode[1]] * data_matrix[opcode[2]]

def main():
    data_matrix = [int(i) for i in data.readline().strip().split(',')]
    data_matrix[1] = 12
    data_matrix[2] = 2

    for i in range(0, len(data_matrix) + 1, 4):
        # if 99 in data_matrix[i:i+4]: # You don't need this for some reason, althoug the description state 
        #     break                    # it should halt on code 99
        current_opcode = data_matrix[i:i+4]
        parse_opcode(data_matrix, current_opcode)

    print(data_matrix[0])

if __name__ == "__main__":
    main()