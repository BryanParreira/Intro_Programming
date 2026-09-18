largest = -1

number = int(input("Enter a number: "))

while number >= 0:
    if number % 2 == 0 and number > largest:
        largest = number
    number = int(input("Enter a number: "))

print("largest =", largest)
