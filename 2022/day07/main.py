from collections import defaultdict

def main():
    with open('./input.txt', 'r') as f:
        ll = map(str.split, f.read().strip().split('\n'))
    # print(list(ll))
    path, dirs = [], defaultdict(int)

    for l in ll:
        if l[0] == "$":
            if l[1] == "cd":
                if l[2] == "..":
                    path.pop()
                else:
                    path.append(l[2])
        elif l[0] != "dir":
            for i in range(len(path)):
                dirs[tuple(path[: i + 1])] += int(l[0])
    # print(path)
    # print(dirs)
    # print(dirs.values())
    print(sum([size for size in dirs.values() if size <= 100_000]))
    required = 30_000_000 - (70_000_000 - dirs[("/",)])
    # print(required)
    print(min([size for size in dirs.values() if size >= required]))
    return 0

if __name__ == "__main__":
    main()