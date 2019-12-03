data = open('./input.txt', 'r')

first_wire_path = data.readline().strip().split(',')
second_wire = data.readline().strip().split(',')

first_line_coordinates = []
second_line_coordinates = []
inital_coor = [0, 0]

for d in first_wire_path:
    direction = d[0]
    length = int(d[1:])
    if direction == 'R':
        for i in range(length):
            inital_coor[0] += 1
            first_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'L':
        for i in range(length):
            inital_coor[0] -= 1
            first_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'U':
        for i in range(length):
            inital_coor[1] += 1
            first_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'D':
        for i in range(length):
            inital_coor[1] -= 1
            first_line_coordinates.append((inital_coor[0], inital_coor[1]))

inital_coor = [0, 0]

for d in second_wire:
    direction = d[0]
    length = int(d[1:])
    if direction == 'R':
        for i in range(length):
            inital_coor[0] += 1
            second_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'L':
        for i in range(length):
            inital_coor[0] -= 1
            second_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'U':
        for i in range(length):
            inital_coor[1] += 1
            second_line_coordinates.append((inital_coor[0], inital_coor[1]))
    elif direction == 'D':
        for i in range(length):
            inital_coor[1] -= 1
            second_line_coordinates.append((inital_coor[0], inital_coor[1]))


same_coordinates = list(set(first_line_coordinates).intersection(second_line_coordinates))
bar = set(map(frozenset, first_line_coordinates)) & set(map(frozenset, second_line_coordinates))

m_distances = []


def foo(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for i in same_coordinates:
    q = list(i)
    m_distances.append(foo(0, q[0], 0, q[1]))

print(min(m_distances))