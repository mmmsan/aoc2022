# Takeaways:
# forgot max() exists

elfs = []

with open("input") as f:
    lines = f.readlines()


def countCalories(lines, elfs):
    i = 0
    for line in lines:
        while i >= len(elfs):
            elfs.append(0)
        if line and not line.isspace():
            elfs[i] += int(line)
        else:
            i += 1
    return elfs


def getMost(elfs):
    return max(elfs)


def runOut(elfs):
    i = 0
    most = getMost(elfs)
    for i in range(len(elfs)):
        if elfs[i] == most:
            elfs[i] = 0
    return elfs


countCalories(lines, elfs)
sum = getMost(elfs)
runOut(elfs)
sum += getMost(elfs)
runOut(elfs)
sum += getMost(elfs)
runOut(elfs)
print(sum)
