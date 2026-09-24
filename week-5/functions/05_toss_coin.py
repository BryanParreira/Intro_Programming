from random import randint


def toss_coin(guess):
    value = randint(0, 1)  # picks a random integer. Either 0 or 1.
    if guess == value:
        return "Correct!"
    else:
        return "Incorrect!"


guess = int(input("Guess the coin flip (0 for heads, 1 for tails): "))
print(toss_coin(guess))
