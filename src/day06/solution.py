def main():
    print("Day 06")
    with open("src/day06/input.txt", "r") as file:
        input = file.read().strip()
        print("", part1(input))
        print("", part2(input))


def part1(input):
    return start_of_packet(input, 4)


def part2(input):
    return start_of_packet(input, 14)


def start_of_packet(data, unique):
    for i in range(unique, len(data)):
        if len(set(data[i - unique : i])) == unique:
            return i


if __name__ == "__main__":
    main()
