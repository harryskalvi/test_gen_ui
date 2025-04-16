import random
from adafruit_servokit import ServoKit
import sys

# Initialize PCA9685 with 16 channels
kit = ServoKit(channels=16)

def generateRandomPunches():
    leftPunches = ["jab", "LHook", "LUpperCut"]
    rightPunches = ["cross", "RHook", "RUpperCut"]
    combination = [random.choice(leftPunches), random.choice(rightPunches)]
    return combination

def beginSparring():
    print("Sparring session started.")
    punches = generateRandomPunches()
    print(punches)
    kit.servo[4].angle = 45
    kit.servo[4].angle = 135

def beginCombination(combination, loop=False):
    print("Combination session started : ", combination)
    print("Loop ", loop)
    kit.servo[0].angle = 90
    kit.servo[0].angle = 45

def endWorkout():
    print("Workout session ended.") # This is a placeholder for the actual end workout logic.