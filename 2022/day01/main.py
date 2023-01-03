def main():
    elfs_records = open('./input.txt').read().strip().split("\n\n")
    elfs_values = [[int(y) for y in x.split("\n")] for x in elfs_records]
    elfs_sum = [sum(x) for x in elfs_values]
    print('Top elf:', max(elfs_sum))
    sum_of_top_three = sum(sorted(elfs_sum)[-3:])
    print('Sum of top three elf:', sum_of_top_three)
    return 0

if __name__ == "__main__":
    main()