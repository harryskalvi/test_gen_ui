import random

def generateRandomPunches():
    leftPunches = ["jab", "LHook", "LUpperCut"]
    rightPunches = ["cross", "RHook", "RUpperCut"]
    combination = [random.choice(leftPunches), random.choice(rightPunches)]
    return combination

def beginSparring():
    print("Sparring session started.")
    punches = generateRandomPunches()
    print(punches)

def beginCombination(combination, loop=False):
    print("Combination session started : ", combination)
    print("Loop ", loop)

def endWorkout():
    print("Workout session ended.") # This is a placeholder for the actual end workout logic.