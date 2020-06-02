import random

def rolling_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    return (a, b)

rolling_dice()