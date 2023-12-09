import re

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

digitsRegex = r"(\d+)+"
special_characters = " !\"#$%&'()*+,-/:;<=>?@[]^_`{|}~"

isTest = 0

if isTest:
    input = "testInput.txt"
else:
    input = "input.txt"

f = open(input, "r")
lines = f.readlines()

totalSum = 0
for index, line in enumerate(lines):
    for enginePart in re.finditer(digitsRegex, line, re.S):
        print(enginePart)
        
        enginePartID = enginePart.group(0)
        #print("Part ID: {}".format(enginePartID))
    
        symbolFound = False
   
        #look left
        if enginePart.start() != 0:
            #prLightPurple("looking left")
            if any(c in special_characters for c in line[enginePart.start()-1]):
                prGreen(">>>>> Symbol found left")
                symbolFound = True

        #look right
        if enginePart.end() <= len(line):
            #prLightPurple("looking right")
            if any(c in special_characters for c in line[enginePart.end()]):
                prGreen(">>>>> Symbol found right")
                symbolFound = True

        #look up
        if index != 0:
           #prLightPurple("looking up")
           lineAbove = lines[index-1]

           startIDX = enginePart.start()
           if startIDX > 0:
               startIDX = startIDX-1
            
           endIDX = enginePart.end()
           if endIDX < len(lineBelow):
               endIDX = endIDX+1

           if any(c in special_characters for c in lineAbove[startIDX:endIDX]):
               prGreen(">>>>> Symbol found top")
               symbolFound = True

        #look down
        if index < len(lines)-1:
            #print("index:{} len:{}".format(index, len(lines)))
            #prLightPurple("looking down")
            lineBelow = lines[index+1]
            startIDX = enginePart.start()
            if startIDX > 0:
                startIDX = startIDX-1
            
            endIDX = enginePart.end()
            if endIDX < len(lineBelow):
                endIDX = endIDX+1

            #print("looking at: {}".format(lineBelow[startIDX:endIDX]))
            if any(c in special_characters for c in lineBelow[startIDX:endIDX]):
               prGreen(">>>>> Symbol found bottom")
               symbolFound = True

        if symbolFound == False:
            prRed("No symbol found for ID={}".format(enginePartID))
        else:
            totalSum = totalSum+int(enginePartID)

print("Result= {}".format(totalSum))