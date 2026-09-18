user_number = int(input("Enter an integer: "))

total = 0

for number in range(1, user_number + 1):
    total = total + number ** 2

print(total)
