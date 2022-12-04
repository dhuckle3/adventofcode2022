def main():
    print("Day 03")
    with open("src/day03/input.txt", "r") as file:
        input = file.readlines()
        print("", part1(input))
        print("", part2(input))


def part1(input):
    sum = 0
    for i in input:
        bag = i.strip()
        compartmentA = set(bag[0 : len(bag) // 2])
        compartmentB = set(bag[len(bag) // 2 : len(bag)])
        item = compartmentA.intersection(compartmentB)
        if len(item) > 1:
            print("More than 1 item!")
            break
        item = item.pop()
        if item.islower():
            sum = sum + ord(item) - 96
        else:
            sum = sum + ord(item) - 38
    return sum


def part2(input):
    sum = 0
    for i in range(0, len(input), 3):
        elfA = set(input[i].strip())
        elfB = set(input[i + 1].strip())
        elfC = set(input[i + 2].strip())
        items = elfA.intersection(elfB).intersection(elfC)
        if len(items) > 1:
            print("More than 1 item!")
            break

        item = items.pop()
        if item.islower():
            sum = sum + ord(item) - 96
        else:
            sum = sum + ord(item) - 38
    return sum


if __name__ == "__main__":
    main()
