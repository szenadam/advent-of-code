def main():
    infile = open('.\\input.txt', 'r')

    result = 0
    for i in infile.readlines():
        min_occurance = int(i.split()[0].split('-')[0])
        max_occurance = int(i.split()[0].split('-')[1])
        character = i.split()[1].replace(':', '')
        password = i.split()[2]
        print(i.strip())
        print(f'min_occurance: {min_occurance}, max_occurance: {max_occurance}, character: {character}, password: {password}')
        is_valid = is_valid_password(min_occurance, max_occurance, character, password)
        print('Is valid password:', is_valid)
        if is_valid:
            result = result + 1

    infile.close()
    print('-' * 30)
    print('Valid password count:', result)
    return 0

def is_valid_password(min_occurance: int, max_occurance: int, character: str, password: str):
    """Validate password."""
    password_characters = list(password)
    c = 0
    for i in password_characters:
        if i == character:
            c = c + 1
    if (c <= max_occurance and c >= min_occurance and part_2_condition(password[min_occurance - 1] == character, password[max_occurance - 1] == character)):
        return True
    return False

def part_2_condition(A, B):
    return bool(A) ^ bool(B)

if __name__ == "__main__":
    main()