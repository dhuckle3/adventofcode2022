from collections import defaultdict


def main():
    print("Day 05")
    with open("src/day05/input.txt", "r") as file:
        input = file.read()
        print("", part1(input))
        print("", part2(input))


def part1(input):
    [header, moves] = input.split("\n\n")
    stacks = defaultdict(list)
    for line in list(reversed(header.split("\n")))[1:]:
        # skip over the numbers
        for k, v in enumerate(range(1, len(line), 4)):
            # print("k,v", k + 1, line[v])
            stacks
            if line[v] != " ":
                stacks[k + 1].append(line[v])

    for line in moves.split("\n"):
        amount = int(line.split(" ")[1])
        source = int(line.split(" ")[3])
        destination = int(line.split(" ")[5])

        for i in range(amount):
            value = stacks[source].pop()
            stacks[destination].append(value)

    top = ""
    for i in range(len(stacks)):
        top = top + stacks[i + 1][-1]
    return top


def part2(input):
    [header, moves] = input.split("\n\n")
    stacks = defaultdict(list)
    for line in list(reversed(header.split("\n")))[1:]:
        # skip over the numbers
        for k, v in enumerate(range(1, len(line), 4)):
            # print("k,v", k + 1, line[v])
            stacks
            if line[v] != " ":
                stacks[k + 1].append(line[v])

    for line in moves.split("\n"):
        amount = int(line.split(" ")[1])
        source = int(line.split(" ")[3])
        destination = int(line.split(" ")[5])

        stacks[destination] = (
            stacks[destination] + stacks[source][len(stacks[source]) - amount :]
        )
        stacks[source] = stacks[source][0 : len(stacks[source]) - amount]

    top = ""
    for i in range(len(stacks)):
        top = top + stacks[i + 1][-1]
    return top


if __name__ == "__main__":
    main()
