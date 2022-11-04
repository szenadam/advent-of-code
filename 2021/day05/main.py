from collections import Counter

def main():

    f = open("input.txt", "r")
    #f = open("sample_input.txt", "r")

    data = []

    for line in f.readlines():
        a = line.strip()
        b = a.split('->')
        (x1, y1) = b[0].split(',')
        (x2, y2) = b[1].split(',')
        data.append(((int(x1), int(y1)), (int(x2), int(y2))))

    horizontal_or_vertical_lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], data))

    xs = []
    ys = []
    for a in horizontal_or_vertical_lines:
        xs.append(a[0][0])
        xs.append(a[1][0])
        ys.append(a[0][1])
        ys.append(a[1][1])

    width = max(xs)
    height = max(ys)

    grid = []
    for i in range(width + 1):
        temp = []
        for j in range(height + 1):
            temp.append(0)
        grid.append(temp)


    for d in horizontal_or_vertical_lines:
        line_coords = calulate_line_coordinates(d)
        insert_line_into_grid(grid, line_coords)

    print(count_overlaps(grid))

def count_overlaps(grid):
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                c = c + 1
    return c


def insert_line_into_grid(grid, line):
    """
    Increase values in matrix (grid) for every point on the line.
    """
    for point in line:
        x, y = point
        grid[x][y] += 1

def calulate_line_coordinates(coords):
    """
    Get all point coordinates for a lined defined by starting point and ending ponits.
    For vertical or horizontal lines only.
    E.g.:
    ((1, 1), (1, 3)) -> [(1,1), (1,2), (1,3)]
    """
    start_x, start_y = coords[0]
    end_x, end_y = coords[1]

    result_coords = []
    result_coords.append(coords[0])


    # diagonal
    if (start_x == end_x and start_y == end_y) or (start_x == end_y and start_y == end_x):
        raise NotImplementedError()
    # X coordinates are equal so it is a vertical line
    elif start_x == end_x:
        delta = abs(start_y - end_y) - 1
        if start_y > end_y:
            for i in range(start_y - 1, end_y, -1):
                result_coords.append((start_x, i))
        else:
            for i in range(start_y + 1, end_y):
                result_coords.append((start_x, i))
    # Y coordinates are equal so it is a horizontal line
    elif start_y == end_y:
        delta = abs(start_x - end_x) - 1
        if start_x > end_x:
            for i in range(start_x - 1, end_x, -1):
                result_coords.append((i, start_y))
        else:
            for i in range(start_x + 1, end_x):
                result_coords.append((i, start_y))
    else:
        raise ValueError('somethings fucky')
    result_coords.append(coords[1])

    return result_coords


if __name__ == "__main__":
    main()
