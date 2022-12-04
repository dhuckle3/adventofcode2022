def main():
    print("Day 04")
    with open("src/day04/input.txt", "r") as file:
        input = file.readlines()
        print("", part1(input))
        print("", part2(input))


def part1(input):
    sum = 0
    for line in input:
        [e1, e2] = line.strip().split(",")
        [e1s, e1f] = e1.split("-")
        e1s = int(e1s)
        e1f = int(e1f)
        [e2s, e2f] = e2.split("-")
        e2s = int(e2s)
        e2f = int(e2f)

        if (e1s <= e2s and e1f >= e2f) or (e2s <= e1s and e2f >= e1f):
            sum = sum + 1
    return sum


def part2(input):
    sum = 0
    for line in input:
        [e1, e2] = line.strip().split(",")
        [e1s, e1f] = e1.split("-")
        elf1 = set(range(int(e1s), int(e1f) + 1))
        [e2s, e2f] = e2.split("-")
        elf2 = set(range(int(e2s), int(e2f) + 1))
        overlap = elf1.intersection(elf2)
        if len(overlap) > 0:
            sum = sum + 1

    return sum


if __name__ == "__main__":
    main()
