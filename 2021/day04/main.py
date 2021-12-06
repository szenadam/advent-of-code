import numpy as np


numbers_called = set()


def main():

    #input = open('sample_input.txt', 'r')
    input = open('input.txt', 'r')

    #part_one(input)
    part_two(input)

    input.close()

    return 0


def part_two(input):
    numbers = get_numbers_from_input(input)
    boards = get_boards_from_input(input).tolist()

    def check_bingo(board, called_numbers):
        for i in range(5):
            if all(board[i][j] in called_numbers for j in range(5)):
                return True
            if all(board[j][i] in called_numbers for j in range(5)):
                return True

        return False

    def get_score(board, called_numbers):
        sum_of_unmarked = 0
        for i in range(5):
            for j in range(5):
                if board[i][j] not in called_numbers:
                    sum_of_unmarked += board[i][j]

        return sum_of_unmarked * called_numbers[-1]  # assume calls isn't longer than it needs to be

    order = {}

    for i in range(1, len(numbers)):
        for j, board in enumerate(boards):
            if j in order.keys():
                continue

            if check_bingo(board, numbers[:i]):
                order[j] = i

    last = max(order, key=order.get)

    print(get_score(boards[last], numbers[:order[last]]))


def part_one(input):

    def mark_number_on_board(boards, num):
        temp = boards
        for board in temp:
            for row in board:
                row[:] = [-1 if x == num else x for x in row]
        return temp

    def sum_unmarked_numbers_in_board(board):
        s = 0
        for row in board:
            for n in row:
                if n != -1:
                    s += n
        return s

    def check_board_for_bingo(board):
        b = np.array(board)
        for row in b:
            if all(x == row[0] for x in row):
                return True
        for row in b.T:
            if all(x == row[0] for x in row):
                return True
        return False

    numbers = get_numbers_from_input(input)
    boards = get_boards_from_input(input)

    winner_board = []
    last_number = 0

    for i in numbers:
        boards = mark_number_on_board(boards, i)
        for board in boards:
            if check_board_for_bingo(board):
                winner_board = board
                last_number = i
                break
        if len(winner_board) != 0:
            break

    s = sum_unmarked_numbers_in_board(winner_board)

    print(f"SCORE: {last_number * s}")


def get_numbers_from_input(input):
    return [int(n) for n in input.readline().strip().split(',')]


def get_boards_from_input(input):
    # read all lines, remove emply ones
    boards = []
    for line in input.readlines():
        boards.append(line.strip().strip())
    boards = list(filter(lambda x: x != '', boards))

    # convert raw string rows into int lists
    rows = []
    for d in boards:
        board_row = d.split()
        rows.append([int(y) for y in board_row])

    # assign every five rows to a board list and assign every board to a boards list, so it is a 3D array
    boards = []
    board = []
    index = 1  # for tracking number of rows aleady in a board
    for row in rows:
        if index == 5:
            board.append(row)
            boards.append(board)

            # reset index and board so we can start a new one
            index = 1
            board = []
            continue

        board.append(row)
        index = index + 1
    return np.array(boards)


if __name__ == "__main__":
    main()
