def main():
    with open('./input.txt', 'r') as f:
        ll = f.read().split('\n')
    part_one(ll)
    part_two(ll)

    return 0


def part_two(ll):
    c = 0
    for l in ll:
        first, second = l.split(',')
        f_start, f_end = first.split('-')
        s_start, s_end = second.split('-')
        first_values = list(range(int(f_start), int(f_end) + 1))
        second_values = list(range(int(s_start), int(s_end) + 1))
        if any(x in first_values for x in second_values):
            # print('overlap')
            c += 1
    print(c)


def part_one(ll):
    c = 0
    for l in ll:
        first, second = l.split(',')
        # print(first, second)
        f_start, f_end = first.split('-')
        s_start, s_end = second.split('-')
        first_values = list(range(int(f_start), int(f_end) + 1))
        second_values = list(range(int(s_start), int(s_end) + 1))
        # print(first_values, second_values)
        if set(first_values) <= set(second_values) or set(second_values) <= set(first_values):
            # print('overlap')
            c += 1
    print(c)


if __name__ == "__main__":
    main()
