from random import randint


def guess_num(guess):
    value = randint(0, 9)  # picks a random integer between 0-9 inclusive
    if value % 2 == 0:
        answer = "even"
    else:
        answer = "odd"

    if guess.lower() == answer:
        return "Correct!"
    else:
        return "Incorrect!"


guess = input("Guess if the number is odd or even: ")
print(guess_num(guess))
