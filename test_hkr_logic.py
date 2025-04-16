import random
from adafruit_servokit import ServoKit
import sys
import time

# Initialize PCA9685 with 16 channels
kit = ServoKit(channels=16)

servoAngles = {
    "Jab":          [(0,0) (4,45), (8,60), (12,180)],
    "Cross":        [(0,45) (4,0), (8,90), (12,45)],
    "LHook":        [(0,60) (4,60), (8,45), (12,60)],
    "RHook":        [(0,90) (4,90), (8,0), (12,135)],
    "LUpperCut":    [(0,135) (4,180), (8,135), (12,90)],
    "RUpperCut":    [(0,180) (4,135), (8,180), (12,0)]
}

def moveServo(servo, angle):
    kit.servo[servo].angle = angle
    print(f"Servo {servo} moved to angle {angle}")

def punch(punchType):
    angles = servoAngles[punchType]
    for angle in angles:
        moveServo(angle[0], angle[1])
        time.sleep(0.5)

def generateRandomPunches():
    leftPunches = ["Jab", "LHook", "LUpperCut"]
    rightPunches = ["Cross", "RHook", "RUpperCut"]
    combination = [random.choice(leftPunches), random.choice(rightPunches)]
    return combination

def beginSparring():
    print("Sparring session started.")
    punches = generateRandomPunches()
    for punch in punches:
        punch(punch)
        time.sleep(1)

def beginCombination(combination, loop=False):
    print("Combination session started : ", combination)
    for punch in combination:
        punch(punch)

def endWorkout():
    print("Workout session ended.") # This is a placeholder for the actual end workout logic.