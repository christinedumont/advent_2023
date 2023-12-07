day = "day2"
isTest = 1


def gamePossible(nbR, nbG, nbB):
    maxR = 12
    maxB = 14
    maxG = 13

    if nbR>maxR or nbB>maxB or nbG > maxG:
        return False
    else:
        return True

if isTest:
    input = "testInput.txt".format(day)
else:
    input = "input.txt".format(day)

f = open(input, "r")
lines = f.readlines()

totalSum = 0
for line in lines:
   lineList = line.split(":")


   gameIdPart = lineList[0]
   sets = lineList[1].split(";")
   
   print(lineList)
   print(sets)

   gameId = 0
   nbR = 1
   nbG = 1
   nbB = 1

   if gamePossible(nbR, nbG, nbB)==True:
      totalSum = totalSum + gameId
    
print("Result: {}".format(totalSum))