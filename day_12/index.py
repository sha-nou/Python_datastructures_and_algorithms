import math 
import random


# calculate sine or cosine of an angle

def getTrigVal(angle):
    return math.sin(angle)

# generate random angle between 90 and 180
def genRandAng():
    angle = random.randint(90,180)
    getVal = getTrigVal(angle)
    
    print(f"the angle is ${angle}")
    print(f"the trigonometric value of the angle is ${getVal}")

genRandAng()