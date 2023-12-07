

day = "dayX"
isTest = 1


if isTest:
    input = "{}/testInput.txt".format(day)
else:
    input = "{}/input.txt".format(day)

f = open(input, "r")
lines = f.readlines()

for line in lines:
    print(line, end="")