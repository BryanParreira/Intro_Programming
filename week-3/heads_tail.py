from random import randint
value = randint(0, 1)  # picks a random integer. Either 0 or 1.

guess = int(input("Enter your guess (0 for Heads, 1 for Tails): "))

if value == 0:
    answer = "Heads"
else:
    answer = "Tails"

if guess == value:
    print("You guessed correctly!")
else:
    print("Sorry, that's not right.")
    print(f"The answer was: {answer}")
