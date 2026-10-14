from random import randint

def toss_coin(guess=0):
    value = randint(0, 1)
    if guess == value:
        return "Correct!"
    return "Incorrect!"