def main():
    infile = open('.\\input.txt')

    raw_data = infile.read()

    data = raw_data.split('\n\n')

    data = list(map(lambda x: x.replace('\n', ' '), data))

    dict_data = []

    for i in data:
        props = i.split(' ')

        d = dict()
        for j in props:
            prop, value = j.split(':')
            d[prop] = value
        dict_data.append(d)

    result = 0
    for i in dict_data:
        if is_valid(i):
            result = result + 1

    print(result)

    infile.close()
    return 0


def is_valid(d: dict):
    req_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in req_props:
        if i not in d.keys():
            return False
    return True


if __name__ == "__main__":
    main()
