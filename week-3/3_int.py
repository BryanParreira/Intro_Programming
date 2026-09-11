number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter a third number: "))

if number1 != number2 and number1 != number3 and number2 != number3:
    print("All unique numbers.")
else:
    print("You repeated the same number.")
