day = "day1"
isTest = False

if isTest:
    input = "testInput.txt".format(day)
else:
    input = "input.txt".format(day)

f = open(input, "r")
lines = f.readlines()

grandTotal = 0
for line in lines:
    
    print(line)
    
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
