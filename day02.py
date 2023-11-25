# Takeways:
# use rstrip() to get rid of any excess whitespace at the end of the line.

def part1():
    total = 0
    with open("input") as f:
        lines = f.readlines()
    for line in lines:
        match line.rstrip():
            # A X ROCK
            # B Y PAPER
            # C Z SCISSORS
            case "A X":
                total += 1+3
            case "B X":
                total += 1+0
            case "C X":
                total += 1+6
            case "A Y":
                total += 2+6
            case "B Y":
                total += 2+3
            case "C Y":
                total += 2+0
            case "A Z":
                total += 3+0
            case "B Z":
                total += 3+6
            case "C Z":
                total += 3+3
    return total


def part2():
    total = 0
    with open("input") as f:
        lines = f.readlines()
    for line in lines:
        match line.rstrip():
            # A ROCK       X LOSE
            # B PAPER      Y DRAW
            # C SCISSORS   Z WIN
            case "A X":
                total += 3+0
            case "B X":
                total += 1+0
            case "C X":
                total += 2+0
            case "A Y":
                total += 1+3
            case "B Y":
                total += 2+3
            case "C Y":
                total += 3+3
            case "A Z":
                total += 2+6
            case "B Z":
                total += 3+6
            case "C Z":
                total += 1+6
    return total


print(part2())
