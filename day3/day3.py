
isTest = 1

if isTest:
    input = "testInput.txt"
else:
    input = "input.txt"

f = open(input, "r")
lines = f.readlines()

for line in lines:
    print(line, end="")