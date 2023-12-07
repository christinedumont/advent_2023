day = "day1"
isTest = False

if isTest:
    input = "{}/testInput2.txt".format(day)
else:
    input = "{}/input.txt".format(day)

f = open(input, "r")
lines = f.readlines()

numList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "eightwo", "twone"]

grandTotal = 0
for line in lines:

    line = line.replace("twone", "21")
    line = line.replace("oneight", "18")
    line = line.replace("eightwo", "82")
    line = line.replace("sevenine", "79")
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    
    lineTotal = 0
    digitsArray = []
    for c in line:
        if c.isdigit():
            digitsArray.append(int(c))
    print(digitsArray)
    
    if len(digitsArray) == 1:
        lineTotal = int("{}{}".format(digitsArray[0], digitsArray[0]))
    else:
        lineTotal = int("{}{}".format(digitsArray[0], digitsArray[len(digitsArray)-1]))
    print(lineTotal)
    grandTotal = grandTotal + lineTotal

    
print("Result: {}".format(grandTotal))
