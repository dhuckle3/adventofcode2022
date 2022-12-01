def main():
    print("Day 01")
    with open("src/day01/input.txt", "r") as file:
        input = file.read()
        print("", part1(input))
        print("", part2(input))


def part1(input):
    return max(
        sum(int(v) for v in elf.strip().split("\n")) for elf in input.split("\n\n")
    )


def part2(input):
    return sum(
        sorted(
            (
                sum(int(v) for v in elf.strip().split("\n"))
                for elf in input.split("\n\n")
            ),
            reverse=True,
        )[0:3]
    )


if __name__ == "__main__":
    main()
