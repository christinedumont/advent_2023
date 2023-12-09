import re

isTest = 0

gameRegex = r"(Game) (\d+)"
redRegex = r"(\d+) (red)"
blueRegex = r"(\d+) (blue)"
greenRegex = r"(\d+) (green)"

def gamePossible(nbR, nbG, nbB):
    maxR = 12
    maxB = 14
    maxG = 13

    if nbR>maxR or nbB>maxB or nbG > maxG:
        return False
    else:
        return True

if isTest:
    input = "testInput.txt"
else:
    input = "input.txt"

f = open(input, "r")
lines = f.readlines()

totalSum = 0
allPowers = 0
for line in lines:
   lineList = line.split(":")

   gameIdPart = lineList[0]
   sets = lineList[1].split(";")

   match = re.search(gameRegex, gameIdPart) 
   if match != None:
       gameId = int(match.group(2))

   setsValid = True
   maxR = 0
   maxG = 0
   maxB = 0
   for set in sets:
       nbR = 0
       nbG = 0
       nbB = 0

       matchR = re.search(redRegex, set)
       matchG = re.search(greenRegex, set)
       matchB = re.search(blueRegex, set)

       if matchR != None:
           nbR = int(matchR.group(1))
       if matchG != None:
           nbG = int(matchG.group(1))
       if matchB != None:
           nbB = int(matchB.group(1)) 
       
       if nbR != 0 and nbR>maxR:
           maxR = nbR
       if nbG != 0 and nbG>maxG:
           maxG = nbG
       if nbB != 0 and nbB>maxB:
           maxB = nbB
       
       if gamePossible(nbR, nbG, nbB)==False:
           setsValid = False
        
       power = maxR * maxG * maxB

   allPowers = allPowers+power 
   if setsValid == True:
       #print("game {} valid".format(gameId))
       totalSum = totalSum+gameId
    
print("Result: {}".format(totalSum))
print("Result P2: {}".format(allPowers))