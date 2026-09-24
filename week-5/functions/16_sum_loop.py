def sum_loop():
    total = 0
    number = int(input("Enter an integer: "))
    while number >= 0:
        total = total + number
        number = int(input("Enter an integer: "))
    return total


print(sum_loop())
