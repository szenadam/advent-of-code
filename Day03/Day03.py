data = open('./input.txt', 'r')

first_wire = data.readline().strip().split(',')
second_wire = data.readline().strip().split(',')

def calc_manhattan_distance(a1, a2, b1, b2):
    return abs(a1 - b1) + abs(a2 - b2)
