from random import randint

def guess(user_guess="even"):
    value = randint(0, 9)
    is_even = value % 2 == 0
    if (user_guess == "even" and is_even) or (user_guess == "odd" and not is_even):
        return "Correct!"
    return "Incorrect!"