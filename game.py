import time
import random

def CalOverallScore(scores):
    pass

def Battle(power_a, power_b):
    d = power_a - power_b
    result = random.randrange(-100, 100) + d
    # time.sleep(2)
    return result

def PathToHappen():
    return random.choice(["TOP","MID","BTM"])