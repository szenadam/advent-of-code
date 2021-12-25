def main():
    data = []
    input_file = 'sample_input.txt'
    input_file = 'input.txt'
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pattern, output = line.strip().split(' | ')
            data.append((pattern, output))
    c = 0
    for pattern, output in data:
        values = output.split(' ')
        for v in values:
            if is_unique_number(v):
                c += 1
    print(c)
    return 0

def is_unique_number(pattern):
    l = len(pattern)
    if l == 2 or l == 4 or l == 3 or l == 7:
        return True
    else:
        return False

def return_possible_number(pattern):
    l = len(pattern)
    if l == 2:
        return 1
    elif l == 4:
        return 4
    elif l == 3:
        return 7
    elif l == 7:
        return 8
    else:
        return -1
    


if __name__ == "__main__":
    main()