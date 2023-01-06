import re

def main():
    with open('./input.txt', 'r') as f:
        ll = f.readlines()
    # print(ll)
    part_one(ll)
    part_two(ll)

    return 0

def part_two(ll):
    orders = []
    stacks_lines = []

    for l in ll:
        if '[' in l:
            stacks_lines.append(l)
        if l[0] == 'm':
            orders.append(l)
    stacks = [[] for x in range(len(stacks_lines[0])//4)]

    for sl in stacks_lines:
        i = 1
        j = 0
        while i < len(sl):
            if sl[i] != ' ':
                stacks[j].append(sl[i])
            i += 4
            j += 1
    # print(stacks_lines)
    # print(orders)
    # print(stacks)
    for o in orders:
        matches = re.search(r'move (\d+) from (\d+) to (\d+)\n?', o)
        num, from_stack, to_stack = int(matches.group(1)), int(matches.group(2))-1, int(matches.group(3))-1
        # print(num, from_stack, to_stack)
        stack_slice = stacks[from_stack][:num]
        stacks[from_stack] = stacks[from_stack][num:]
        stacks[to_stack] = stack_slice + stacks[to_stack]
        # print(stacks)
    result = []
    for s in stacks:
        result.append(s[0])
    print(''.join(result))

def part_one(ll):
    orders = []
    stacks_lines = []

    for l in ll:
        if '[' in l:
            stacks_lines.append(l)
        if l[0] == 'm':
            orders.append(l)
    stacks = [[] for x in range(len(stacks_lines[0])//4)]

    for sl in stacks_lines:
        i = 1
        j = 0
        while i < len(sl):
            if sl[i] != ' ':
                stacks[j].append(sl[i])
            i += 4
            j += 1
    # print(stacks_lines)
    # print(orders)
    # print(stacks)
    for o in orders:
        matches = re.search(r'move (\d+) from (\d+) to (\d+)\n?', o)
        num, from_stack, to_stack = int(matches.group(1)), int(matches.group(2))-1, int(matches.group(3))-1
        # print(num, from_stack, to_stack)
        for i in range(num):
            if len(stacks[from_stack]) == 0:
                break
            stacks[to_stack].insert(0, stacks[from_stack].pop(0))
        # print(stacks)
    result = []
    for s in stacks:
        result.append(s[0])
    print(''.join(result))

if __name__ == "__main__":
    main()