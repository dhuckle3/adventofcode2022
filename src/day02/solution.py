def main():
    print("Day 02")
    with open("src/day02/input.txt", "r") as file:
        input = file.readlines()
        print(part1(input))
        print(part2(input))


def part1(input):
    score = 0
    for line in input:
        [a, x] = line.split(" ")
        opponent = ord(a.strip()) - 64
        player = ord(x.strip()) - 87

        diff = (player - opponent) % 3
        if diff == 0:
            # tie
            score = score + 3
        elif diff == 1:
            # win
            score = score + 6
        elif diff == 2:
            # lose
            score = score + 0
        score = score + player
    return score


def part2(input):
    score = 0
    for line in input:
        turnScore = 0
        [them, strategy] = line.strip().split(" ")
        them = ord(them) - 65
        strategy = ord(strategy) - 89
        turnScore = turnScore = 3 + (strategy * 3)
        us = (them + strategy + 3) % 3
        turnScore = turnScore + us + 1
        score = score + turnScore
    return score


if __name__ == "__main__":
    main()
