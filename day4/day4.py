import re

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def partOne(input):
    grandTotal = 0
    for line in lines:
        card = re.findall(r'\d+', line.split(":")[0])[0]
        winningNums = re.findall(r'\d+', line.split(":")[1].split("|")[0])
        cardNums = re.findall(r'\d+', line.split(":")[1].split("|")[1])
        
        prLightPurple("Card {}".format(card))
        
        commonMatches = list(set(winningNums).intersection(cardNums))
        nbMatches = len(commonMatches)
        totalForCard = 0
        prCyan("{} matches".format(nbMatches))
        if nbMatches==1:
            totalForCard = 1
        elif nbMatches>1:
            totalForCard = pow(2, nbMatches-1)
        
        grandTotal += totalForCard

    prYellow("Part 1 Result: {}".format(grandTotal))
    
def partTwo(input):
    nbScratches = 0
    
    copiesDictionnary = {}
    
    for line in lines:
        cardStr = line.split(":")[0]
        card = re.findall(r'\d+', cardStr)[0]
        winningNums = re.findall(r'\d+', line.split(":")[1].split("|")[0])
        cardNums = re.findall(r'\d+', line.split(":")[1].split("|")[1])
        
        copiesDictionnary[cardStr] = 1
        
        prLightPurple(cardStr)    
        print(copiesDictionnary)
        commonMatches = list(set(winningNums).intersection(cardNums))
    
    prYellow("Part 2 Result: {}".format(nbScratches))
    
day = "day4"
isTest = 1

if isTest:
    input = "{}/testInput.txt".format(day)
else:
    input = "{}/input.txt".format(day)

f = open(input, "r")
lines = f.readlines()

#partOne(input)
partTwo(input)


    