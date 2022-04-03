def main():
    data = []
    input_file = 'sample_input.txt'
    input_file = 'input.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pattern, output = line.strip().split(' | ')
            data.append((pattern, output))
    s = 0
    for pattern, output in data:
        displays = get_display_pattern(pattern)
        digits = ''
        for output in output.split(' '):
            n = set(output.strip())
            for index, key in enumerate(displays.values()):
                if n == key:
                    digits = digits + str(index)
        s = s + int(digits)
        print(pattern, '|', output, '|', digits)
    print(s)
    return 0


def get_display_pattern(patterns):
    displays = {0: '', 1: '', 2: '', 3: '',
                4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    left_tripple = []
    right_tripple = []

    for w in patterns.split(' '):
        l = len(w)
        if l == 2:
            displays[1] = set(w)
        if l == 3:
            displays[7] = set(w)
        if l == 4:
            displays[4] = set(w)
        if l == 5:
            left_tripple.append(set(w))
        if l == 6:
            right_tripple.append(set(w))
        if l == 7:
            displays[8] = set(w)

    for w in right_tripple:
        if displays[4].issubset(set(w)):
            displays[9] = set(w)
        else:
            if displays[7].issubset(set(w)):
                displays[0] = set(w)
            else:
                displays[6] = set(w)

    for w in left_tripple:
        if displays[7].issubset(set(w)):
            displays[3] = set(w)
        else:
            if len(set(w).intersection(displays[4])) == 3:
                displays[5] = set(w)
            else:
                displays[2] = set(w)
    return displays


if __name__ == "__main__":
    main()
