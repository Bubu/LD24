from constants import *
def generateElements():
    allElements = set()
    f = open(PATH + 'reactions.txt', mode = 'r')
    for line in f:
        (reactant,product) = [x.split()for x in line.split(';')]
        if len(reactant) == 0 or len(product) == 0:
            print("Error on: ",line)
            break
        allElements = allElements.union(set(reactant),set(product))
    [print("'", x, "':('", x.capitalize(), "',(0,0),0)", "," ,sep='') for x in allElements]

generateElements()
