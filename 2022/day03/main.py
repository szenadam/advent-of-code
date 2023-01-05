# Techniques used:
# - lookup table
# - chunking a list into sublists of n (here it's three) elements
# - common elements in multiple lists
# - split string into 2 parts

priority = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }

def main():
    with open('./input.txt', 'r') as f:
        ll = f.read().split('\n')

    part_one(ll)
    part_two(ll)
    return 0

def part_two(ll):
    chunked = [ll[i:i+3] for i in range(0, len(ll), 3)]
    # print(chunked)
    s = 0
    for ch in chunked:
        f, m, l = ch
        common_elements = list(set(f).intersection(m).intersection(l))
        for ce in common_elements:
            s += priority[ce]
        # print(common_elements)
    print(s)

def part_one(ll):
    s = 0
    for l in ll:
        first_half, second_half = l[:len(l)//2], l[len(l)//2:]
        # print(first_half, second_half)
        common_elements = list(set(first_half).intersection(second_half))
        for ce in common_elements:
            s += priority[ce]
        # print(common_elements)
    print(s)


if __name__ == "__main__":
    main()
